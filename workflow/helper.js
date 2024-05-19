require("module-alias/register");

const config = require("@config/workflow");
const cliProgress = require("cli-progress");

const getAllRepos = async (octokit) => {
    const repos = [];

    for (let page = 0; ; page++) {
        const requestedRepos = await octokit.rest.repos.listForUser({
            username: config.user,
            per_page: 100,
            page: page,
        });

        if (requestedRepos.data.length === 0) break;
        repos.push(
            ...requestedRepos.data
                .filter(
                    (repo) =>
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
