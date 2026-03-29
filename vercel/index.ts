import path from "node:path";
import { projects } from "@config/vercel";
import {
  createPathIfNotExists,
  deletePathIfExists,
  generateRandomString,
  writeFile,
} from "@helpers";
import { deploy } from "@vercel/helper";
import { simpleGit } from "simple-git";

const storeFile = path.resolve(import.meta.dir, "../.github/vercel/ver.json");
const store: Record<string, string> = await Bun.file(storeFile).json();

const gitPath = path.join("/tmp", "git", generateRandomString());
if (!(await createPathIfNotExists(gitPath))) {
  console.log("Path already exists! Aborting...");
  process.exit(1);
}

for (const c of projects) {
  const gitRepoPath = path.join(gitPath, c.dest);
  await createPathIfNotExists(gitRepoPath);

  const git = simpleGit(gitRepoPath);

  await git.clone(c.repo, gitRepoPath, ["--depth", "1", "--branch", c.branch]);

  const commit = await git.log();
  const lastCommit = commit?.latest?.hash;
  if (lastCommit && lastCommit !== store[c.dest]) {
    console.log(`Deploying ${c.dest} with commit ${lastCommit}...`);

    const deployment = await deploy(
      path.join(gitRepoPath, c.path),
      c.dest,
      c.token || "VERCEL_TOKEN",
    );
    if (deployment?.readyState === "READY") {
      console.log(`Deployed ${c.dest} successfully!`);
      store[c.dest] = lastCommit;
    } else {
      console.log(`Failed to deploy ${c.dest}!`);
    }
  }

  await deletePathIfExists(gitRepoPath);
}

await deletePathIfExists(gitPath);

const stateString = JSON.stringify(store, null, 2);
console.log(`Writing state: ${stateString}`);
await writeFile(storeFile, store);
