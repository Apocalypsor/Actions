import path from "node:path";
import {
  client,
  createPathIfNotExists,
  deletePathIfExists,
  generateRandomString,
} from "@helpers";
import { simpleGit } from "simple-git";

interface GitHubRepo {
  name: string;
  clone_url: string;
  fork: boolean;
  archived: boolean;
  disabled: boolean;
  owner: { login: string };
}

const token = process.env.GH_TOKEN;
if (!token) {
  throw new Error("Missing environment variable: GH_TOKEN");
}

const user = process.env.GITLEAKS_USER;
if (!user) {
  throw new Error("Missing environment variable: GITLEAKS_USER");
}

const exclude = (process.env.GITLEAKS_EXCLUDE ?? "").split(",").filter(Boolean);

// Fetch all owned repos
const repos: GitHubRepo[] = [];
for (let page = 1; ; page++) {
  const page_repos: GitHubRepo[] = await client
    .get("https://api.github.com/user/repos", {
      headers: {
        Authorization: `token ${token}`,
        Accept: "application/vnd.github.v3+json",
      },
      searchParams: {
        affiliation: "owner",
        per_page: 100,
        page,
      },
    })
    .json();

  if (page_repos.length === 0) break;
  repos.push(
    ...page_repos.filter(
      (repo) =>
        repo.owner.login === user &&
        !repo.fork &&
        !repo.archived &&
        !repo.disabled &&
        !exclude.includes(repo.name),
    ),
  );
}

console.log(`Found ${repos.length} repos to scan`);

const tmpDir = path.join("/tmp", "gitleaks", generateRandomString());
const reportDir = path.resolve("reports");
await createPathIfNotExists(tmpDir);
await createPathIfNotExists(reportDir);

const leakedRepos: string[] = [];

for (let i = 0; i < repos.length; i++) {
  const repo = repos[i];
  const repoDir = path.join(tmpDir, repo.name);
  const authUrl = repo.clone_url.replace("https://", `https://${token}@`);

  try {
    const git = simpleGit();
    await git.clone(authUrl, repoDir, ["--depth", "1"]);

    const reportPath = path.join(reportDir, `${repo.name}_report.json`);
    const proc = Bun.spawn(
      ["gitleaks", "detect", "--source", repoDir, "--report-path", reportPath],
      { stdout: "ignore", stderr: "ignore" },
    );
    const exitCode = await proc.exited;

    if (exitCode !== 0) {
      leakedRepos.push(repo.name);
    }
  } catch (e) {
    console.error(`Failed to scan ${repo.name}: ${e}`);
  } finally {
    await deletePathIfExists(repoDir);
  }
}

await deletePathIfExists(tmpDir);

// Write summary
if (leakedRepos.length > 0) {
  const summary = [
    `Gitleaks Scan Summary - ${new Date().toISOString().split("T")[0]}`,
    "",
    `Scanned: ${repos.length} repos`,
    `Leaks found in ${leakedRepos.length} repo(s):`,
    "",
    ...leakedRepos.map((name) => `  - ${name}`),
    "",
    "See attached reports for details.",
  ].join("\n");

  await Bun.write("/tmp/gitleaks-summary.txt", summary);
  console.log(summary);
} else {
  console.log(`Scanned ${repos.length} repos, no leaks found.`);
}

// Set output for workflow
const outputFile = process.env.GITHUB_OUTPUT;
if (outputFile) {
  const fs = await import("node:fs");
  fs.appendFileSync(outputFile, `leaks_found=${leakedRepos.length > 0}\n`);
}
