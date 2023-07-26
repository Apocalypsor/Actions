require("module-alias/register");

const { Octokit } = require("@octokit/rest");
const { getAllRepos, deleteWorkflowRuns } = require("@workflowUtil/helper");

require("dotenv").config();

const octokit = new Octokit({
    auth: process.env.WORKFLOW_TOKEN,
});

(async () => {
    const repos = await getAllRepos(octokit);

    console.log(`Found ${repos.length} repos`);

    let i = 1;
    for (const repo of repos) {
        console.log(
            `[${i++}/${repos.length}] Deleting workflow runs for ${
                repo.owner
            }/${repo.name}`
        );

        await deleteWorkflowRuns(octokit, repo);
    }
})();
