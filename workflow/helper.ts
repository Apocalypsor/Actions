import * as config from "@config/workflow";
import { client } from "@helpers";
import type { Octokit } from "@octokit/rest";
import cliProgress from "cli-progress";

interface Repo {
  name: string;
  owner: string;
}

interface GitHubRepo {
  full_name: string;
  name: string;
  archived: boolean;
  disabled: boolean;
  owner: { login: string };
}

interface WorkflowAction {
  id: number;
  name: string;
  owner: string;
}

export const getAllRepos = async (): Promise<Repo[]> => {
  const repos: Repo[] = [];

  for (let page = 1; ; page++) {
    const requestedRepos: GitHubRepo[] = await client
      .get("https://api.github.com/user/repos", {
        headers: {
          Authorization: `token ${process.env.WORKFLOW_TOKEN}`,
          Accept: "application/vnd.github.v3+json",
        },
        searchParams: {
          per_page: 100,
          page: page,
        },
      })
      .json();

    if (requestedRepos.length === 0) break;
    repos.push(
      ...requestedRepos
        .filter(
          (repo) =>
            repo.full_name.startsWith(config.user) &&
            !repo.archived &&
            !repo.disabled &&
            !config.exclude.includes(repo.name),
        )
        .map((repo) => ({
          name: repo.name,
          owner: repo.owner.login,
        })),
    );
  }

  return repos;
};

export const deleteWorkflowRuns = async (
  octokit: Octokit,
  repo: Repo,
): Promise<void> => {
  const actions: WorkflowAction[] = [];
  for (let page = 0; ; page++) {
    const requestedActions = await octokit.rest.actions.listWorkflowRunsForRepo(
      {
        owner: repo.owner,
        repo: repo.name,
        per_page: 100,
        page: page,
      },
    );

    if (requestedActions.data.workflow_runs.length === 0) break;
    actions.push(
      ...requestedActions.data.workflow_runs
        .filter((run) => run.status === "completed")
        .map((run) => ({
          id: run.id,
          name: repo.name,
          owner: repo.owner,
        })),
    );
  }

  const actionBar = new cliProgress.SingleBar(
    {},
    cliProgress.Presets.shades_classic,
  );

  actionBar.start(actions.length, 0);
  for (const action of actions) {
    try {
      await octokit.rest.actions.deleteWorkflowRun({
        owner: action.owner,
        repo: action.name,
        run_id: action.id,
      });
    } catch (e) {
      console.error(`Failed to delete run ${action.id}: ${e}`);
    }
    actionBar.increment();
  }
  actionBar.stop();
};
