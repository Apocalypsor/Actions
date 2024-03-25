const { createDeployment } = require("@vercel/client");

const deploy = async (repoPath, projectName, token) => {
    let deployment;
    for await (const event of createDeployment(
        {
            token: process.env[token],
            path: repoPath,
            apiUrl: "https://api.vercel.com",
        },
        {
            name: projectName,
            target: "production",
        }
    )) {
        if (event.type === "ready") {
            deployment = event.payload;
            break;
        }
    }

    return deployment;
};

module.exports = {
    deploy,
};
