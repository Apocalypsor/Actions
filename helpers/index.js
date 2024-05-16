const fs = require("fs");
const path = require("path");
const axios = require("axios");

const client = axios.create(
    {
        headers: {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache"
        }
    }
);

const generateRandomString = (length = 10) => {
    return Math.random()
        .toString(36)
        .substring(2, length + 2);
};

const createPathIfNotExists = async (dir) => {
    if (!fs.existsSync(dir)) {
        await fs.promises.mkdir(dir, { recursive: true });
        return true;
    }

    return false;
};

const deletePathIfExists = async (dir) => {
    if (fs.existsSync(dir)) {
        await fs.promises.rm(dir, { recursive: true });
    }
};

const writeFile = async (filePath, data) => {
    const dir = path.dirname(filePath);
    try {
        await fs.promises.access(dir);
    } catch {
        await fs.promises.mkdir(dir, { recursive: true });
    }
    await fs.promises.writeFile(filePath, JSON.stringify(data, null, 2));
};

const validateIpv4 = (ip) => {
    return /^(\d{1,3}\.){3}\d{1,3}$/.test(ip);
};

const validateIpv6 = (ip) => {
    return /^(::)?[0-9a-fA-F]{1,4}(::?[0-9a-fA-F]{1,4}){0,7}(::)?$/.test(ip);
};

module.exports = {
    client,
    generateRandomString,
    createPathIfNotExists,
    deletePathIfExists,
    writeFile,
    validateIpv4,
    validateIpv6
};
