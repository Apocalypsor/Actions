const { validateIpv4, validateIpv6 } = require("@helpers");

class Ip {
    constructor() {
        this._ip = [];
    }

    add(ip, id) {
        this._ip.push({
            ip,
            id
        });
    }

    get ip() {
        return this._ip.map(record => record.ip);
    }

    get ipWithId() {
        return this._ip;
    }
}

class Record {
    constructor(domain) {
        this.domain = domain;
        this.ipv4 = new Ip();
        this.ipv6 = new Ip();
    }

    addRecord(ip, id = "") {
        if (validateIpv4(ip)) {
            this.ipv4.add(ip, id);
        } else if (validateIpv6(ip)) {
            this.ipv6.add(ip, id);
        }
    }

    addIpv4Record(ip, id = "") {
        this.ipv4.add(ip, id);
    }

    addIpv6Record(ip, id = "") {
        this.ipv6.add(ip, id);
    }

    get A() {
        return this.ipv4.ip;
    }

    get AAAA() {
        return this.ipv6.ip;
    }

    get AWithId() {
        return this.ipv4.ipWithId;
    }

    get AAAAWithId() {
        return this.ipv6.ipWithId;
    }
}

module.exports = {
    Record
};
