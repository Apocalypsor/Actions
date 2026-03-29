import { createDeployment } from "@vercel/client";

export const deploy = async (
  repoPath: string,
  projectName: string,
  token: string,
) => {
  let deployment: { readyState: string; [key: string]: unknown } | undefined;
  for await (const event of createDeployment(
    {
      token:
        process.env[token] ??
        (() => {
          throw new Error(`Missing environment variable: ${token}`);
        })(),
      path: repoPath,
      apiUrl: "https://api.vercel.com",
    },
    {
      name: projectName,
      target: "production",
    },
  )) {
    if (event.type === "ready") {
      deployment = event.payload;
      break;
    }
  }

  return deployment;
};
