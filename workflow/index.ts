import { Octokit } from "@octokit/rest";
import { deleteWorkflowRuns, getAllRepos } from "@workflow/helper";

const octokit = new Octokit({
  auth: process.env.WORKFLOW_TOKEN,
});

const repos = await getAllRepos();

console.log(`Found ${repos.length} repos`);

let i = 1;
for (const repo of repos) {
  console.log(
    `[${i++}/${repos.length}] Deleting workflow runs for ${repo.owner}/${repo.name}`,
  );

  await deleteWorkflowRuns(octokit, repo);
}
