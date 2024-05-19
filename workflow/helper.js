require("module-alias/register");

const config = require("@config/workflow");
const { default: axios } = require("axios");
const cliProgress = require("cli-progress");

const getAllRepos = async (octokit) => {
    const repos = [];

    for (let page = 1; ; page++) {
        const requestedRepos = await axios.get("https://api.github.com/user/repos",
            {
                headers: {
                    Authorization: `token ${process.env.WORKFLOW_TOKEN}`,
                    Accept: "application/vnd.github.v3+json"
                },
                params: {
                    per_page: 100,
                    page: page,
                },
            }
        );

        if (requestedRepos.data.length === 0) break;
        repos.push(
            ...requestedRepos.data
                .filter(
                    (repo) =>
                        repo.full_name.startsWith(config.user) &&
                        !repo.archived &&
                        !repo.disabled &&
                        !config.exclude.includes(repo.name)
                )
                .map((repo) => ({
                    name: repo.name,
                    owner: repo.owner.login,
                }))
        );
    }

    return repos;
};

const deleteWorkflowRuns = async (octokit, repo) => {
    const actions = [];
    for (let page = 0; ; page++) {
        const requestedActions =
            await octokit.rest.actions.listWorkflowRunsForRepo({
                owner: repo.owner,
                repo: repo.name,
                per_page: 100,
                page: page,
            });

        if (requestedActions.data.workflow_runs.length === 0) break;
        actions.push(
            ...requestedActions.data.workflow_runs.map((run) => ({
                id: run.id,
                name: repo.name,
                owner: repo.owner,
            }))
        );
    }

    const actionBar = new cliProgress.SingleBar(
        {},
        cliProgress.Presets.shades_classic
    );

    actionBar.start(actions.length, 0);
    for (const action of actions) {
        try {
            await octokit.rest.actions.deleteWorkflowRun({
                owner: action.owner,
                repo: action.name,
                run_id: action.id,
            });
        } catch (ignored) {}
        actionBar.increment();
    }
    actionBar.stop();
};

module.exports = {
    getAllRepos,
    deleteWorkflowRuns,
};
