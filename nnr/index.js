require("module-alias/register");
require("dotenv").config();

const { client, validateIpv4, validateIpv6 } = require("@helpers");
const { Record } = require("@nnrUtil/record");

const fetchNnr = async () => {
    const response = await client.post(
        "https://nnr.moe/api/servers",
        {},
        {
            headers: {
                "Content-Type": "application/json",
                token: process.env.NNR_TOKEN
            }
        }
    );

    const data = response.data;
    if (data.status !== 1) {
        throw new Error(data.message);
    }

    const servers = data.data;
    const records = {};
    servers.forEach(server => {
        if (!server.sid || !server.host) {
            return;
        }
        const domain = `${server.sid}.${process.env.NNR_DOMAIN_SUFFIX}`;
        const ips = server.host.split(",");
        const r = new Record(domain);
        ips.forEach(ip => {
            r.addRecord(ip);
        });
        records[domain] = r;
    });

    return records;
};

const fetchCloudflare = async () => {
    const response = await client.get(`https://api.cloudflare.com/client/v4/zones/${process.env.CLOUDFLARE_ZONE_ID}/dns_records`, {
        headers: {
            "Authorization": `Bearer ${process.env.CLOUDFLARE_TOKEN}`,
            "Content-Type": "application/json"
        },
        params: {
            type: "A,AAAA"
        }
    });

    const dnsRecords = response.data.result;
    const records = {};
    dnsRecords.forEach(record => {
        if (!record.name || !record.name.endsWith(process.env.NNR_DOMAIN_SUFFIX)) {
            return;
        }
        if (!records[record.name]) {
            records[record.name] = new Record(record.name);
        }
        if (record.type === "A") {
            records[record.name].addIpv4Record(record.content, record.id);
        } else if (record.type === "AAAA") {
            records[record.name].addIpv6Record(record.content, record.id);
        }
    });

    return records;
};

const addRecordFromNnr = async (domain, ips, type) => {
    for (let ip of ips) {
        await client.post(`https://api.cloudflare.com/client/v4/zones/${process.env.CLOUDFLARE_ZONE_ID}/dns_records`, {
            type: type,
            name: domain,
            content: ip,
            ttl: 1,
            proxied: false
        }, {
            headers: {
                "Authorization": `Bearer ${process.env.CLOUDFLARE_TOKEN}`,
                "Content-Type": "application/json"
            }
        });
    }
};

const updateRecordFromNnr = async (domain, ips, type, cloudflareRecord) => {
    let cr = null;
    if (type === "A") {
        cr = cloudflareRecord.AWithId;
    } else if (type === "AAAA") {
        cr = cloudflareRecord.AAAAWithId;
    } else {
        throw new Error("Invalid type");
    }

    const toAdd = ips.filter(ip => !cr.some(record => record.ip === ip));
    const toDelete = cr.filter(record => !ips.includes(record.ip));

    for (let ip of toAdd) {
        await client.post(`https://api.cloudflare.com/client/v4/zones/${process.env.CLOUDFLARE_ZONE_ID}/dns_records`, {
            type: type,
            name: domain,
            content: ip,
            ttl: 1,
            proxied: false
        }, {
            headers: {
                "Authorization": `Bearer ${process.env.CLOUDFLARE_TOKEN}`,
                "Content-Type": "application/json"
            }
        });
    }

    for (let record of toDelete) {
        await client.delete(`https://api.cloudflare.com/client/v4/zones/${process.env.CLOUDFLARE_ZONE_ID}/dns_records/${record.id}`, {
            headers: {
                "Authorization": `Bearer ${process.env.CLOUDFLARE_TOKEN}`,
                "Content-Type": "application/json"
            }
        });
    }
};

(async function() {
    const nnrRecords = await fetchNnr();
    const cfRecords = await fetchCloudflare();

    const toAdd = {};
    const toUpdate = {};

    Object.keys(nnrRecords).forEach(domain => {
        if (!cfRecords[domain]) {
            toAdd[domain] = nnrRecords[domain];
        } else {
            const nnrA = nnrRecords[domain].A || [];
            const nnrAAAA = nnrRecords[domain].AAAA || [];
            const cfA = cfRecords[domain].A || [];
            const cfAAAA = cfRecords[domain].AAAA || [];
            nnrA.sort();
            nnrAAAA.sort();
            cfA.sort();
            cfAAAA.sort();

            if (nnrA.join(",") !== cfA.join(",") || nnrAAAA.join(",") !== cfAAAA.join(",")) {
                toUpdate[domain] = nnrRecords[domain];
            }
        }
    });

    for (let domain in toAdd) {
        const record = toAdd[domain];
        await addRecordFromNnr(domain, record.A, "A");
        await addRecordFromNnr(domain, record.AAAA, "AAAA");
    }

    for (let domain in toUpdate) {
        const record = toUpdate[domain];
        await updateRecordFromNnr(domain, record.A, "A", cfRecords[domain]);
        await updateRecordFromNnr(domain, record.AAAA, "AAAA", cfRecords[domain]);
    }
})();
