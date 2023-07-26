const fs = require("fs");
const path = require("path");

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

module.exports = {
    generateRandomString,
    createPathIfNotExists,
    deletePathIfExists,
    writeFile,
};
