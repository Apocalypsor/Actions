import fs from "node:fs";
import path from "node:path";
import ky from "ky";

export const client = ky.create({
  timeout: 10000,
  headers: {
    "User-Agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    Accept: "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
  },
});

export const generateRandomString = (length = 10): string => {
  return Math.random()
    .toString(36)
    .substring(2, length + 2);
};

export const createPathIfNotExists = async (dir: string): Promise<boolean> => {
  if (!fs.existsSync(dir)) {
    await fs.promises.mkdir(dir, { recursive: true });
    return true;
  }
  return false;
};

export const deletePathIfExists = async (dir: string): Promise<void> => {
  if (fs.existsSync(dir)) {
    await fs.promises.rm(dir, { recursive: true });
  }
};

export const writeFile = async (
  filePath: string,
  data: unknown,
): Promise<void> => {
  const dir = path.dirname(filePath);
  try {
    await fs.promises.access(dir);
  } catch {
    await fs.promises.mkdir(dir, { recursive: true });
  }
  await fs.promises.writeFile(filePath, JSON.stringify(data, null, 2));
};
