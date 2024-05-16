require("module-alias/register");
require("dotenv").config();

const path = require("path");
const { simpleGit } = require("simple-git");
const {
    generateRandomString,
    createPathIfNotExists,
    deletePathIfExists,
    writeFile,
} = require("helpers");
const config = require("@config/vercel");
const store = require("@store/vercel/ver.json");
const { deploy } = require("@vercelUtil/helper");

(async () => {
    const gitPath = path.join("/tmp", "git", generateRandomString());
    if (!(await createPathIfNotExists(gitPath))) {
        console.log("Path already exists! Aborting...");
        return;
    }

    for (let c of config.projects) {
        const gitRepoPath = path.join(gitPath, c.dest);
        await createPathIfNotExists(gitRepoPath);

        const git = simpleGit(gitRepoPath);

        await git.clone(c.repo, gitRepoPath, [
            "--depth",
            "1",
            "--branch",
            c.branch,
        ]);

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
    await writeFile(require.resolve("@store/vercel/ver.json"), store);
})();
