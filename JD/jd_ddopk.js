/*
京享值PK
cron 15 2,7,18 * * * jd_joyscore.js
更新时间：2021-7-05
活动入口：京东APP-我的-京享值
已支持IOS双京东账号,Node.js支持N个京东账号
更新日志：直接延时，调整逻辑顺序，增加是否开宝箱选项。默认关闭
建议：12点过后运行一次，半小时后再运行一次。没有提交自己分享码将无法获取其他人的分享码。0-18时每2小时运行一次
脚本兼容: QuantumultX, Surge, Loon, JSBox, Node.js
============Quantumultx===============
[task_local]
#京享值PK
5,30 0-18/2 * * * https://raw.githubusercontent.com/hyzaw/scripts/main/ddo_pk.js, tag=京享值PK
================Loon==============
[Script]
cron "5,30 0-18/2 * * *" script-path=https://raw.githubusercontent.com/hyzaw/scripts/main/ddo_pk.js,tag=京享值PK
===============Surge=================
*/

const $ = new Env('京享值PK');
!function (n) { "use strict"; function r(n, r) { var t = (65535 & n) + (65535 & r); return (n >> 16) + (r >> 16) + (t >> 16) << 16 | 65535 & t } function t(n, r) { return n << r | n >>> 32 - r } function u(n, u, e, o, c, f) { return r(t(r(r(u, n), r(o, f)), c), e) } function e(n, r, t, e, o, c, f) { return u(r & t | ~r & e, n, r, o, c, f) } function o(n, r, t, e, o, c, f) { return u(r & e | t & ~e, n, r, o, c, f) } function c(n, r, t, e, o, c, f) { return u(r ^ t ^ e, n, r, o, c, f) } function f(n, r, t, e, o, c, f) { return u(t ^ (r | ~e), n, r, o, c, f) } function i(n, t) { n[t >> 5] |= 128 << t % 32, n[14 + (t + 64 >>> 9 << 4)] = t; var u, i, a, h, g, l = 1732584193, d = -271733879, v = -1732584194, C = 271733878; for (u = 0; u < n.length; u += 16)i = l, a = d, h = v, g = C, d = f(d = f(d = f(d = f(d = c(d = c(d = c(d = c(d = o(d = o(d = o(d = o(d = e(d = e(d = e(d = e(d, v = e(v, C = e(C, l = e(l, d, v, C, n[u], 7, -680876936), d, v, n[u + 1], 12, -389564586), l, d, n[u + 2], 17, 606105819), C, l, n[u + 3], 22, -1044525330), v = e(v, C = e(C, l = e(l, d, v, C, n[u + 4], 7, -176418897), d, v, n[u + 5], 12, 1200080426), l, d, n[u + 6], 17, -1473231341), C, l, n[u + 7], 22, -45705983), v = e(v, C = e(C, l = e(l, d, v, C, n[u + 8], 7, 1770035416), d, v, n[u + 9], 12, -1958414417), l, d, n[u + 10], 17, -42063), C, l, n[u + 11], 22, -1990404162), v = e(v, C = e(C, l = e(l, d, v, C, n[u + 12], 7, 1804603682), d, v, n[u + 13], 12, -40341101), l, d, n[u + 14], 17, -1502002290), C, l, n[u + 15], 22, 1236535329), v = o(v, C = o(C, l = o(l, d, v, C, n[u + 1], 5, -165796510), d, v, n[u + 6], 9, -1069501632), l, d, n[u + 11], 14, 643717713), C, l, n[u], 20, -373897302), v = o(v, C = o(C, l = o(l, d, v, C, n[u + 5], 5, -701558691), d, v, n[u + 10], 9, 38016083), l, d, n[u + 15], 14, -660478335), C, l, n[u + 4], 20, -405537848), v = o(v, C = o(C, l = o(l, d, v, C, n[u + 9], 5, 568446438), d, v, n[u + 14], 9, -1019803690), l, d, n[u + 3], 14, -187363961), C, l, n[u + 8], 20, 1163531501), v = o(v, C = o(C, l = o(l, d, v, C, n[u + 13], 5, -1444681467), d, v, n[u + 2], 9, -51403784), l, d, n[u + 7], 14, 1735328473), C, l, n[u + 12], 20, -1926607734), v = c(v, C = c(C, l = c(l, d, v, C, n[u + 5], 4, -378558), d, v, n[u + 8], 11, -2022574463), l, d, n[u + 11], 16, 1839030562), C, l, n[u + 14], 23, -35309556), v = c(v, C = c(C, l = c(l, d, v, C, n[u + 1], 4, -1530992060), d, v, n[u + 4], 11, 1272893353), l, d, n[u + 7], 16, -155497632), C, l, n[u + 10], 23, -1094730640), v = c(v, C = c(C, l = c(l, d, v, C, n[u + 13], 4, 681279174), d, v, n[u], 11, -358537222), l, d, n[u + 3], 16, -722521979), C, l, n[u + 6], 23, 76029189), v = c(v, C = c(C, l = c(l, d, v, C, n[u + 9], 4, -640364487), d, v, n[u + 12], 11, -421815835), l, d, n[u + 15], 16, 530742520), C, l, n[u + 2], 23, -995338651), v = f(v, C = f(C, l = f(l, d, v, C, n[u], 6, -198630844), d, v, n[u + 7], 10, 1126891415), l, d, n[u + 14], 15, -1416354905), C, l, n[u + 5], 21, -57434055), v = f(v, C = f(C, l = f(l, d, v, C, n[u + 12], 6, 1700485571), d, v, n[u + 3], 10, -1894986606), l, d, n[u + 10], 15, -1051523), C, l, n[u + 1], 21, -2054922799), v = f(v, C = f(C, l = f(l, d, v, C, n[u + 8], 6, 1873313359), d, v, n[u + 15], 10, -30611744), l, d, n[u + 6], 15, -1560198380), C, l, n[u + 13], 21, 1309151649), v = f(v, C = f(C, l = f(l, d, v, C, n[u + 4], 6, -145523070), d, v, n[u + 11], 10, -1120210379), l, d, n[u + 2], 15, 718787259), C, l, n[u + 9], 21, -343485551), l = r(l, i), d = r(d, a), v = r(v, h), C = r(C, g); return [l, d, v, C] } function a(n) { var r, t = "", u = 32 * n.length; for (r = 0; r < u; r += 8)t += String.fromCharCode(n[r >> 5] >>> r % 32 & 255); return t } function h(n) { var r, t = []; for (t[(n.length >> 2) - 1] = void 0, r = 0; r < t.length; r += 1)t[r] = 0; var u = 8 * n.length; for (r = 0; r < u; r += 8)t[r >> 5] |= (255 & n.charCodeAt(r / 8)) << r % 32; return t } function g(n) { return a(i(h(n), 8 * n.length)) } function l(n, r) { var t, u, e = h(n), o = [], c = []; for (o[15] = c[15] = void 0, e.length > 16 && (e = i(e, 8 * n.length)), t = 0; t < 16; t += 1)o[t] = 909522486 ^ e[t], c[t] = 1549556828 ^ e[t]; return u = i(o.concat(h(r)), 512 + 8 * r.length), a(i(c.concat(u), 640)) } function d(n) { var r, t, u = ""; for (t = 0; t < n.length; t += 1)r = n.charCodeAt(t), u += "0123456789abcdef".charAt(r >>> 4 & 15) + "0123456789abcdef".charAt(15 & r); return u } function v(n) { return unescape(encodeURIComponent(n)) } function C(n) { return g(v(n)) } function A(n) { return d(C(n)) } function m(n, r) { return l(v(n), v(r)) } function s(n, r) { return d(m(n, r)) } function b(n, r, t) { return r ? t ? m(r, n) : s(r, n) : t ? C(n) : A(n) } $.md5 = b }();
$.toObj = (t, e = null) => {
    try {
        return JSON.parse(t)
    } catch {
        return e
    }
}
$.toStr = (t, e = null) => {
    try {
        return JSON.stringify(t)
    } catch {
        return e
    }
}

const notify = $.isNode() ? require("./sendNotify") : "";
const jdCookieNode = $.isNode() ? require("./jdCookie.js") : "";
const sck = $.isNode() ? "set-cookie" : "Set-Cookie";
const APPID = "dafbe42d5bff9d82298e5230eb8c3f79";
const md5Key = "34e1e81ae8122ca039ec5738d33b4eee";
let cookiesArr = [],
    cookie = "",
    message;
let minPrize = 1;

let countlaunch = 0;
let countreceive = 0;
let bcomplate = false;
//是否开箱开关。true 为自动开箱，注意PK开箱豆子有时效性。有需要再开了用。默认关闭；
let kaixiang=false;
if ($.isNode()) {
    Object.keys(jdCookieNode).forEach((item) => {
        cookiesArr.push(jdCookieNode[item]);
    });
    if (process.env.JD_DEBUG && process.env.JD_DEBUG === "false") console.log = () => { };
} else {
    cookiesArr = [
        $.getdata("CookieJD"),
        $.getdata("CookieJD2"),
        ...jsonParse($.getdata("CookiesJD") || "[]").map((item) => item.cookie),
    ].filter((item) => !!item);
}
//采用闭包方式调用
var _0xodR='jsjiami.com.v6',_0x6478=[_0xodR,'WSB1JMOX','A8KdLsKmwoQ=','wqzCs0cpwpnDkMOgwprDt8KBw6LCvGdz','woXDpsKdwpTCpg==','asKCSBE+','w6LCqcK/w6HCow==','wq5jwqsVOg==','QHjDoA==','V8KOw7x+wrk=','XsOsZcOsBA==','L8OCwo87w7w=','RsKOcMKPQg==','CMKuB8KKwpQ=','cHvDuHsG','wpYtw6fCqcO/','KRjCsAk=','w4nCv8OQAjk=','IsOLw4E=','YRDDmicU','axXCry08w67CkgU=','ZcKUwrPDoh3CgSLCvxM=','XnzCksOaw5s=','wqIXw6M0wo0=','wqEKJsK5wpQ=','CxRIfcK5','Dy7Dth/Ctg==','UMOJwoHCoRM=','csKTwpnDoxw=','w78vw4XDnw==','wrXDmcKrwqrCvQ==','wrLDmMKFwofCvA==','wqcxw4/CgMOP','cGrCicObw7E=','UT1RPRw=','wrnCv3wCwpc=','CzzCh03Dgw==','w6MNwqLCocKs','McOpSMKhNQ==','w5sRw5o=','dUlaw6LDig==','w4rDrMO6w5hu','F8Ogw6dFJg==','F8KPDcK2wpo=','wpjDpcKbwoDCkA==','DRvDniDCpQ==','w63CpXE=','FwfCosOI','wqbCgMORRcKu','wr7CvcOgw77Duw==','ZMOhZcOLHg==','w4jCgVDDpsOb','w5PCosOBNhY=','Wh9BGsOH','f8KgU8K+TQ==','5Yyh6LSY6YOr6Kyq6KyE5rC15aaB6Le9Kw==','FcORwoc/w4c=','ThbDuwIc','GMOXw6dEAA==','w4DCvcK/w7PCjA==','RcKeacO1w6A=','VyjDuMOB','KMOWw5x9IA==','wqtUwo0dBw==','Ii9F','5Lq85L2V57i85p2O77+D','wrXCsUkNwpw=','woIdYyXCnA==','wqHCv1Q=','wofCjsO2w7XDmA==','O8Ocw7BGPw==','QkhFw4rDgg==','QkDCucO6w4E=','w7/Co8OgPAY=','w7Ymw7fDj8Os','cCHDucO4wrY=','CA7CqhwV','wrzCuXINwqg=','woZCwoQTPQ==','RkXDkBt8','wptUw47CuCY=','VsKUYg==','wodPwogbJw==','wq7CiMOSw6vDhA==','NzzCgcO1EMKT','w5nCkwwww6ZtMMOuLzU5DMOBw7ADwpM=','woTCm3U6wq0=','WWlew6PDhA==','YzbDr8OawrE=','w77DnGw=','V37Dp0EM','CQZtwrF3','SyjDrA==','wrfCklYMwoU=','YsKYwo7DmQY=','W2PDozh7','aGTCmg==','5LmE5L6E57m15p6t7723','c27DtQ==','woFiNsKsw5c=','ZAl/LBw=','wrRww5/CtjM=','bR9UKgs=','UMOBYsOIDQ==','wrYGQlAJ','w5HCo1TDr8OC','w7XCiyl6w7c=','wr7CvsOtw73DmXVxw6bCk8K4w7dAw4zDlsKRwpXChS3ClMO8SXhRwp1TwoM/w4JRMMO7IQvCrgQpw4fCkHPCkTbChyFkw5AoXsKPw7kfwro=','Ay9GNw80Lw==','OMODR8O2NcKmRsO+w7sJw7TCnXPChsOQwrw=','IR5Bd8OCw67CrcKTwr5j','AznClcOzNw==','wrHDjMKc','5Li95Yu56YCp6K6H5aW96LeA77y9','GRzDmi7CtQ==','w5HCpsO/Fxo=','wq7ClcOFacKB','w4fCmW/DmMO6','wrJBwpkHIg==','wrozw4k=','w73CiCd9w5k=','a27DnTFD','ecKpdMKmRA==','KMKqIsKOwqc=','w4/Dpm46w5s=','wqdFOcK9w5o=','woZRNsKSw7Q=','w5/CnsO1GT4=','IynChcO9','6I6e5Yy35Yi65Lmlfk3noJjvvLY=','5oi+5p6Rwpka5q6I5pWB5be/5a6H','5rCZ5p+q6I+S5Y+I5Yql5aWz5Y6J','wokMw4vCnMOZ','YMKQVMK9ZQ==','fMKnVsOjw5k=','5byB5Yq1E8Krwo3vvKnDsCDnoqLvvZ/vvIk=','5b6x5YiPw4TCoMOBLTDCm3HvvYg=','5omc55u95Lmo5LuDPMOM5Yu65YCEwpY=','wo7CvUU5wpE=','6L6W6KC15Lu/5YuA6YOs6K2wwqxz','w7PCjMKrw7/Ciw==','55Wm5om3csKLYVnDow==','5b225YiR5Yij5pSo772n','w4XDjUXDkjw=','5Lm85YugwqHDl+atn+aXnuW3ruWsgA==','woTDmAnDoig=','QcOvwonCgT0=','wqzDk8KrwrbCnA==','wqwHw4fCncOQ','6Laq5oqQ5Yq45pes5puL6aiI772s6L2R6KC56KKO5YutKcKI','woY/dwPCmQ==','V8KPQA0Q','5Luj5aeI5LiH6KGl5YqGVlLlnavltb7nlbjlrpc=','w6TCisKRw7fCgw==','5YW+5aek5qKl5rWV5pq65ZCo5Y6t5Lmi5b2f5a+c56+74oGA4oKD','5Y2t5b6p5a21562Dw6Q=','5a+U56+l5qGS5rSN57iM5p+v4oGf4oCT','Kw5uwpdD','5Lud5Yi06YO56K2c5aW86Let77y/','eFJRw7/Dog==','OsO+w4V+Dw==','bBhHECw=','w5/CpMOFFR4=','wrt/C8KLw4g=','wogXw6/ChMOt','6KG95YiB6YGo6KyF5aev6LeD77+l','wqNkO8Krw5U=','5YyH6LSr6KCF5YuowqjCpumDquitseaMuOaLvw==','bMKYwoXDqRfCoS7CjhnDqMOoRQjDlsO1esKnJsKB','5rCt5p6u6IyJ5Y2K5YiP6KG75YuI6YCK6K6C56Ck','w5c2w7LDtMON','VMKVVT4/','HQXCh8OfNw==','w4DCpzNvw5w=','VEDnuK7mnKLlharplIs=','wo7DnsKKwpbCuQ==','NMKow67CpXApI0HCqGMJw4V9','5o2z5Yyd6KCy5Yilw7oE5o2P5ouR','6YKn6K+q5oqE5Yqy6Z2K6Ke756+d5b6p5o2I5pWxVsKE772X','wpbCqMODdMKYAj0nSDhnwo3Dsw==','worCkksywro=','N8K9w7rCoVw=','cjZGLBg=','w4nClzJbw60=','wrrDucKEwqTCjQ==','TMO1woLCpwNKworDtMKVUw8=','w54kwoTCg8K3','UVLDnhld','Rm3DpEEjGcO1WMKEKGjDoCfCnMOKPA==','JcOBw4NBQFwsXWUs','JsOWw7nCqw==','wrtYG8KTw7EewpvDhUR8VmrDmyVxw5bCi8OvPQl8ZsKwwoUowrfCt8Onwpc4b0/CjjjDiVQff2DCgxwDDjfDvXLDvWRVH1cHw7YDw6/DkcOqfTBFwpvCuMOhwr1aw6guPldTScOnw6hgDRBsUWLDssKldsKkw51xwqHChsKsdhvDmsOrTsKGSgNSwoPDqw7Dv0BoV24Xw7PCpsKpG1HCk3g=','wrfCuB4DwpM=','5Y6D6LaP6YOj6Ky16KyU5rGj5aax6LWuwpk=','KDfCpiwN','aMOOwoXCmQY=','wqFPw43Ctig=','LCDCmMOkLg==','Z8KnUsORw5c=','6YGW6K2e5ou45Ymt6Z+e6KWn56625b+r5oyn5pW5clzvvqQ=','a8KWRcK/dw==','R8KedsOfw4Y=','fsOxwp3CvAA=','wr3CpcOTT8K7','w7LCqCFIw7g=','wrrDhsKP','5b+K5Yu0bCfCokYb776E','RjlmH8O7','wpk/w40swpU=','wpDCo8O3','wrk4dA==','woQXP8KJwqc=','XsOkwqTCgCM=','M3jCoDg5','BAxDwrhZ','wro3w7ovwpPCiAQ=','5ouh6KKC5Lm05LqZ5qCI5raB6ai76K2J','wq12w73CiTk=','d3TDug==','wpcgajrCtw==','IQDCmA==','wqMCc3Ig','wp3CuV0=','BAbDnQjCtw==','w5zDjsOQ','wrcxw43CucObIzbCmw==','w5nDuGfDsgU=','wqrDkz3DsTo=','TynDuDIA','wpwiYQ==','6I6x5Y6Hw7kb5Ymb6KKN','wqZhwqIWJQk=','5p6R5pS95o2o5aST55Ww','dMKlUQQA','wqx2w4PCtzo=','fFtOw5vDrMORbcK6JCIVwqvCmMKu','worDuR/DnwzCq0bCnVnDjMKUUB3DgsKV','VMKkZzMA','wqczw63CnsOd','wrnCvcOVScKx','PsKXBA==','w7Eew4HDh8Os','w6/Ct8OEADE=','woY1w4A=','ajTDhxc4wo0=','wqVQwoI9FA==','TGfDhhJ5','aMKBUTQJ','wojDlDbDqRo=','wqHCtV0HwonChQ==','RWRQw4bDig==','wr8PUmUB','wqnDni3DmhQ=','wpnDq8K8woPChw==','fnTDhl8O','w5bChsOmDz8=','w7bDucKjw5LDvuaLt+eZu+WJqOaXsnU=','HyFcbsKF','cS1HM8OX','aitvEgk=','BBXCkhsh','5Lm75L2J57il5p6k7769','w6DDgsOYw6hzwqUOw6kddS43wrYs','w7bCjH7DpcOE','woctOMKfwpA=','D27CmTQ9','w6nDkkotwrpWGcOq','X8OCRA==','by9QLgU=','6KGX5Ymk6YCQ6K+r5oup5Yuv6L6M5Zqr57u65p+K77yZ','w5PDjUM=','ChrCgDIU','wpDCm8Oyw6nDnA==','UyjDmMOBwoo=','w4jClhZ2','6LS25oiJ5Yiu5pef5pmU6am877yP6LyC6KCA5LmJ5YuWwrXCpg==','GhJK','IRLCkAcHw6LCkg==','w7XDln8=','S0DDogls','agFqF8Ok','fFFP','dEPDoBBm','w7bCmsOQ','w6rCocK/','6LyR6KGI6KGn5YuZ6YOR6K6WwpBx','HA7Dqi/CtQ==','c8KxwrDDiAQ=','w7crw5fDisOeKkrDtQNSwprDpsOEYXk=','PCzClUDDtg==','cnpYw6bDhQ==','wrEhTEY1','wqHDr8KAwqvCkQ==','wrtJw7DCjzY=','RcKOWw==','wqAEO8K0wp0=','wpEeE8KSwqY=','w5IXw5LDrMO5','BCDCpzoK','NsKZF8Kj','wpwADA==','aS90LTA=','X8KsV8Oww44=','Xkd+w4HDmg==','Q2fDg2Qf','wokOYmMi','w4srw7rDlcOP','Jh5Cc8Kuw6zCosKfwrhywp3DqsOqwoRi','wp0Yw4ETwpA=','wqMYY2MB','w6DDo0sPwq4=','Wn1ew5zDhw==','wofDg8KewobCuA==','FyHCnw==','w6DDjMOqw7NUwrUO','QVtlw4vDhw==','YsKfaCEf','GD7DpDLCuQ==','VMKtw7U=','RcKKaMKhRWN3','woRyM8K0w7E=','w4nCu8ORGD0=','NcOcSQ==','6LSi5ouz5Yqd5pW25piG6ai877226L6/6KGC6KK85YufX8Ko','w6DDjVzDpjQ=','wrEdWj/CpA==','Qw3DgsOBwrI=','W8OswoPCvhg=','5rCX5p286I2Y5YyE5Yup6KCb5Yil6YO86K6n56Gw','fsODTcOqKw==','worDsDbDrAg=','K8KrG8KAwqI=','5b265Yqs6IOg5Z+0FA==','dGDCr8Obw6NncHY=','QTXDpMOYwq9GNj4fVA==','YTBPChY=','wqAkaA==','wqzCp1ISwpnCng==','w5oQwoHCtcKtw5g=','OzHDsSPCtsOGHFE=','S8KKUSQ1','dMKZwqHDoATCtzg=','SMO5wpHCuidzwoDDqsKyVBtl','aj7Djg==','W2hPw73DpA==','w6DDiMOZ','YzZqCjU=','w7vCmx9cw7M=','w57DoVkAwo0=','EsO3wq4=','TsKESMKaR2t8','w7fCg3LDggUSSh/DiALCgsODB8KCwpdrw4lfFzwgK8KxLg==','wrjDmcKVCBfDpWNzVcKaasK6LQ==','Z8KMwqbDiBLDrg==','XkDCoTMOwo7ChSs=','w4DDsBLDvyLCo0DClhQ=','DMOvwpnCsxkh','Vx3Diw==','YUfCrMOPw4Q=','aGrCiMOQw7N6XmPDkhbDsMOu','wprDjsKuwoXCpg==','b8O3wpvCrT4=','RmlQw43Dlg==','dzbDqBch','awDDjsO5woo=','CMOWY8K8IQ==','NQ7Cv27Dgg==','EMONwo4ow5o=','5byt5YuV6ICV5Z2rwpM=','wrlKw6fChjs=','w7PCmFXDqMOe','w4/DpGHDjTk=','NyfCgsOo','dx5cB8OF','6YCM6K2W5oiD5Yi+6Z2x6Kea562n5b645o2X5pSNw77Cqu+9rw==','M8K7w4PClXs=','wqTDi8KQwrTCsg==','PMKYw4nCmHI=','woBtw5fCriA=','CsO3woYzw4M=','w5vDg1At','fsKsYQ==','w43DgFwKw5E=','wrxBw6PCtTU=','PBvCskHDgw==','Z8KwVcOxw7E=','VGnDtVkv','worDsx4=','w4vCnFvDrsOd','XsOeRA==','w7UCw77DlsO8','RzfDsQkp','VETDnF0B','cgFC','PCLDnBPCvQ==','w7LCocKLw7HCug==','S3LDsw==','woZsw5DCqhQ=','wqbCocOLw6jDmToywr0=','woLDnsKnwp/CkA==','CDNmfcKE','JsKXMMK2wpE=','JMO2wq4fw6w=','JTvDtQ==','5Y2X6La56YGY6K2y6Ky/5rKI5aaG6Latw6Y=','Gi/CrwkN','HQbCkQ==','Z8OuwrTCrRM=','5b+S5YqH6IOK5Z6GwrE=','dMKvw4ljwoHCkRYQ','CMO2T8K7AQ==','wpYVIMKKwrA=','QWfDn3oJ','w6Y+57i85p2O5YSj6Zap','w5rDvsOGw551','MsOwRcKQIg==','YChPGj8=','6KCx5Ymd6YC36K6N5omi5YiW6L+W5ZuZ57uv5p2p77ye','NEvCjAEm','bzhWFxA=','KsKiw6o=','ZA10LcOK','w7rDqHfDn8O/wpYFNU/DvsOqwpzCucOmwqo8HcOvw6HCmhE/w7LDog==','LzBSwotLXg==','ImfClsO7w4B7cj8=','dMKUCMKWwoxKw6Ulwp4=','NcKsb8Oiw60D','ATPCtg==','dXJ5w57DtA==','IQfDqDLCkQ==','AyFGwqlX','VVnDpEgA','wp7CmMOhw6PDkg==','w47Dj1ACwpE=','SsKzdsKAfg==','w6LCk8ObHjg=','b8OpwrzCnwQ=','5b2V5Yic6IG15Z2Kdg==','w5DDpk4Kw48=','w6nDlms8','CQTCkMOrHA==','csKzaMOQw5Y=','PTvDnSTCtQ==','HE3Cvhc=','w6g6w5DDisO6','wrFhMMKxw7o=','KcOHw55COA==','woFKw5bCtiA=','w7HCoUTDmcO4wqoNYw==','aAl3PBA=','YwjDnxEI','dsKuUz4v','MsKiw57CtGs=','F8OJYMKKHg==','wq0tVwfCuA==','woYeZBPCuw==','SsKbwpDDtg4=','H8Ovw6JFJw==','IiDCgWDDsg==','6KG95Yu06YCu6K635aeJ6LeI772w','alDDoSpF','w5DCr1vDmMOs','wpgYSgbCgA==','ADrCmW7DpQ==','bUDCtsOzw7w=','w7jCpXvDl8OE','woFWw5/CoQA=','G8KBGcKIwqQ=','w5HCosONKgQ=','VWHCi8OKw7Y=','w6jDjVbDtRM=','w6nChih6w7I=','IHbCmwYO','wolQwroEPA==','IRbCow==','OC3DtzbCjA==','UBfDsQkA','UwrDm8OwwpA=','w4DCq17DjMOe','woINw4cvwqI=','EDHCr3fDrg==','wosBw57CisOh','V0zCr8OIw6Q=','Qj7DuiUd','Xj7Dnj0p','wrpGMsKWw64=','wq/Cg8OSw5rDvA==','wqZAw4HCkQs=','BQlnRMK3','w5/ChhFKw7xjJw==','T8KdwqHDiT8=','w5nCkxVXw7Ez','w4DDsBLDrh3CoUvDhQ==','WMO0wqIFw4ZaaGXCgQ==','wqrDlMOXw7tRw60=','wogIJ8KXwp8=','wrprwr8F','wo7DmwzDkSY=','w5g5wpfCkMKa','wqUow480wp0=','wqd3wqs=','XcKOc8KsRA==','wpPDp8Kxwr/Clw==','woIbfg7Cvg==','TcKASMKv','ExDDuxLCug==','woM5Z2A9','WsO3wqLCsQRpwoPDsg==','wr5cw6rCkT8=','OhB2YsKcw7rCrcKO','LAlLasK4w6bCr8K0wr1r','eMKId8OSw5Y=','woAmVHErPGPCrQ==','w7M7wrbCn8KQ','ZxlXGcOo','aSDDhTYD','dA5rFRk=','XcKOb8K6XA==','w7fDk3YZw5A=','agF2AcO8','wpQscnU=','ScOVecOYPA==','wpYtw7vCv8On','AgvCqzoH','JTbCszw7','d3/CnMOKw7U=','bknDh3Uw','w47Dj0MJw6Q=','w5XCkAI=','wo/DlhbDmQw=','S8KMVxAqCFdt','6YGw6K6Y5om75YmC6Lyn5Zqp57mj5p2E77yL','R8OCcMOuLw==','UitzMSU=','wrpvwp4UIhTCrE4=','w7vDkMOow7Vn','L8OJd8KcLw==','wr5PwoEFJA==','wqnDhTXDkhg=','ZURmw6nDoQ==','w7TDnS0=','J8K8EMK0wqc=','fwjDu8OTwqs=','bk/Dhhpm','InnCqy4c','w5LDkXYpw7o=','w5bCtMKUw6zCqQ==','QQ7DkcO0wqk=','X8KNc8Oqw7Y=','GU/Cvj86w5rDkjDDi8OUXzFzasKNwrI=','IsKlw6t2wrvCgEc=','IMKQwr3DhCbCuiXDsQ==','In/DgA==','fsOEwrXCrTk=','fgPDsxo7','w73CkMOD','esK+YMOow60=','w6zCjUfDkcOk','w7HCq0TDsMOi','wpQVw7khwpo=','BQbCuVrDjQ==','6I6k5YyJ5YiA5Liuw5N156Kc772g','IiLChnTDhg==','asKTwrE=','FMOmf8KcJQ==','wphWw4/ClyA=','TR5BOMOd','O8Ogw5VHKQ==','c8K4wqXDtzI=','woFQwqY/Ng==','wqzCpcO+','wofCnFIawos=','w4fCgnrDtsO4','BjsejhCLiami.cAXoQXnzqm.v6ldGd=='];(function(_0x49716f,_0x31ddf3,_0x11814e){var _0x470078=function(_0x18c8d4,_0xab61d4,_0xc186cd,_0x53fc55,_0x498697){_0xab61d4=_0xab61d4>>0x8,_0x498697='po';var _0x2071e0='shift',_0x2eb2a9='push';if(_0xab61d4<_0x18c8d4){while(--_0x18c8d4){_0x53fc55=_0x49716f[_0x2071e0]();if(_0xab61d4===_0x18c8d4){_0xab61d4=_0x53fc55;_0xc186cd=_0x49716f[_0x498697+'p']();}else if(_0xab61d4&&_0xc186cd['replace'](/[BehCLAXQXnzqldGd=]/g,'')===_0xab61d4){_0x49716f[_0x2eb2a9](_0x53fc55);}}_0x49716f[_0x2eb2a9](_0x49716f[_0x2071e0]());}return 0x95a91;};return _0x470078(++_0x31ddf3,_0x11814e)>>_0x31ddf3^_0x11814e;}(_0x6478,0x80,0x8000));var _0x30c8=function(_0x518d99,_0x37dd93){_0x518d99=~~'0x'['concat'](_0x518d99);var _0x15c71c=_0x6478[_0x518d99];if(_0x30c8['GMuPtK']===undefined){(function(){var _0x57bcaf=typeof window!=='undefined'?window:typeof process==='object'&&typeof require==='function'&&typeof global==='object'?global:this;var _0x193f6d='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';_0x57bcaf['atob']||(_0x57bcaf['atob']=function(_0x22802a){var _0x5ec9ec=String(_0x22802a)['replace'](/=+$/,'');for(var _0xd9375d=0x0,_0x1a76e2,_0x50210c,_0x342102=0x0,_0x51ceb7='';_0x50210c=_0x5ec9ec['charAt'](_0x342102++);~_0x50210c&&(_0x1a76e2=_0xd9375d%0x4?_0x1a76e2*0x40+_0x50210c:_0x50210c,_0xd9375d++%0x4)?_0x51ceb7+=String['fromCharCode'](0xff&_0x1a76e2>>(-0x2*_0xd9375d&0x6)):0x0){_0x50210c=_0x193f6d['indexOf'](_0x50210c);}return _0x51ceb7;});}());var _0x48869b=function(_0x25edd0,_0x37dd93){var _0xb3c6a4=[],_0x1f2654=0x0,_0x57e192,_0x270407='',_0x427bfb='';_0x25edd0=atob(_0x25edd0);for(var _0x103ef4=0x0,_0x137363=_0x25edd0['length'];_0x103ef4<_0x137363;_0x103ef4++){_0x427bfb+='%'+('00'+_0x25edd0['charCodeAt'](_0x103ef4)['toString'](0x10))['slice'](-0x2);}_0x25edd0=decodeURIComponent(_0x427bfb);for(var _0x178dfa=0x0;_0x178dfa<0x100;_0x178dfa++){_0xb3c6a4[_0x178dfa]=_0x178dfa;}for(_0x178dfa=0x0;_0x178dfa<0x100;_0x178dfa++){_0x1f2654=(_0x1f2654+_0xb3c6a4[_0x178dfa]+_0x37dd93['charCodeAt'](_0x178dfa%_0x37dd93['length']))%0x100;_0x57e192=_0xb3c6a4[_0x178dfa];_0xb3c6a4[_0x178dfa]=_0xb3c6a4[_0x1f2654];_0xb3c6a4[_0x1f2654]=_0x57e192;}_0x178dfa=0x0;_0x1f2654=0x0;for(var _0x28d6f0=0x0;_0x28d6f0<_0x25edd0['length'];_0x28d6f0++){_0x178dfa=(_0x178dfa+0x1)%0x100;_0x1f2654=(_0x1f2654+_0xb3c6a4[_0x178dfa])%0x100;_0x57e192=_0xb3c6a4[_0x178dfa];_0xb3c6a4[_0x178dfa]=_0xb3c6a4[_0x1f2654];_0xb3c6a4[_0x1f2654]=_0x57e192;_0x270407+=String['fromCharCode'](_0x25edd0['charCodeAt'](_0x28d6f0)^_0xb3c6a4[(_0xb3c6a4[_0x178dfa]+_0xb3c6a4[_0x1f2654])%0x100]);}return _0x270407;};_0x30c8['AlScov']=_0x48869b;_0x30c8['FuWXaZ']={};_0x30c8['GMuPtK']=!![];}var _0x3ea40a=_0x30c8['FuWXaZ'][_0x518d99];if(_0x3ea40a===undefined){if(_0x30c8['DMDmYU']===undefined){_0x30c8['DMDmYU']=!![];}_0x15c71c=_0x30c8['AlScov'](_0x15c71c,_0x37dd93);_0x30c8['FuWXaZ'][_0x518d99]=_0x15c71c;}else{_0x15c71c=_0x3ea40a;}return _0x15c71c;};!function(_0x399b0e){var _0x43ad18={'txTTT':function(_0x9e8ddb,_0x54ee98){return _0x9e8ddb+_0x54ee98;},'XOpfS':_0x30c8('0','iCGG'),'kBrCO':function(_0x40dd5b,_0x1c07c5){return _0x40dd5b(_0x1c07c5);},'SNfbO':_0x30c8('1','aRZq'),'qpsjo':function(_0x510e3e,_0x2af53c){return _0x510e3e(_0x2af53c);},'BwyqY':function(_0x289c80,_0x239134){return _0x289c80(_0x239134);},'TApZE':_0x30c8('2','VjtX'),'Tmmhw':function(_0x52b7dc,_0x5bbc22){return _0x52b7dc===_0x5bbc22;},'AiCSB':_0x30c8('3','d[Xo'),'JKDVm':function(_0x292cfb){return _0x292cfb();},'XWCju':_0x30c8('4','iCGG'),'Occlm':_0x30c8('5','XcJ3'),'KTjNg':_0x30c8('6','L$hY'),'JLazv':_0x30c8('7','d[Xo'),'XSxKk':function(_0x3bb91f,_0x3df542,_0x2c071a){return _0x3bb91f(_0x3df542,_0x2c071a);},'SOufx':function(_0x3b6270,_0x468ba7,_0x5979b8){return _0x3b6270(_0x468ba7,_0x5979b8);},'MRONh':function(_0x3eb0d3,_0x401810){return _0x3eb0d3(_0x401810);},'UYtSt':function(_0x2dba70,_0x623105){return _0x2dba70(_0x623105);},'LODZw':function(_0x27becf,_0x1f9445){return _0x27becf>_0x1f9445;},'IxQBL':function(_0x424c94,_0x25007d){return _0x424c94-_0x25007d;},'OBTqY':function(_0x4d655b,_0x5edf97){return _0x4d655b+_0x5edf97;},'zpWkQ':_0x30c8('8','jxjg'),'YSFuh':function(_0x420954,_0x91a0b9){return _0x420954<=_0x91a0b9;},'oCbFY':function(_0x284bc9,_0x315669){return _0x284bc9!==_0x315669;},'EqEUH':_0x30c8('9','6kW9'),'xMnYY':_0x30c8('a','jxjg'),'jPpys':_0x30c8('b',']srM'),'UZxij':function(_0xd31cc2,_0x5e7e50){return _0xd31cc2(_0x5e7e50);},'oTNLE':function(_0x156197,_0x6e9eb0){return _0x156197===_0x6e9eb0;},'SfTAP':'PZWeQ','nHOBW':function(_0x46e071,_0x572417){return _0x46e071<_0x572417;},'YiRrD':function(_0x64b598,_0x3ead8b){return _0x64b598+_0x3ead8b;},'LsQuM':function(_0x2d2c8d,_0xe33c18){return _0x2d2c8d+_0xe33c18;},'yCdwz':_0x30c8('c','0G6v'),'tRWgL':_0x30c8('d','oi%f'),'OwJJt':_0x30c8('e','sIct'),'wFhYO':function(_0x34d1a8,_0x2496bd){return _0x34d1a8!==_0x2496bd;},'GANzm':function(_0x5068be,_0x400147,_0x344671,_0x2c27d0){return _0x5068be(_0x400147,_0x344671,_0x2c27d0);},'zecfr':_0x30c8('f','^JhI'),'uMfIr':function(_0x38e4db,_0x4a96c2){return _0x38e4db-_0x4a96c2;},'MEcxQ':function(_0x308e13,_0x3e2b2c){return _0x308e13===_0x3e2b2c;},'AlJRm':_0x30c8('10',']QoG'),'NluMd':_0x30c8('11','mljN'),'aqxOU':function(_0x90af7f,_0x2cbb16){return _0x90af7f>_0x2cbb16;},'IYcRf':_0x30c8('12','plRg'),'NyVnz':function(_0xf51dc6,_0x21fc1e){return _0xf51dc6+_0x21fc1e;},'dzWIU':function(_0x3367cb,_0x4fc5ef){return _0x3367cb+_0x4fc5ef;},'PeKkP':'\x20PK\x20\x20我的分数:','KDoSh':function(_0x463082,_0x1c5996){return _0x463082!==_0x1c5996;},'SUewY':_0x30c8('13','d[Xo'),'JCvsg':_0x30c8('14','Z8iK'),'Qjvtf':function(_0x4940df,_0x2debab,_0x98a1d4,_0x1b1ce4,_0x143161){return _0x4940df(_0x2debab,_0x98a1d4,_0x1b1ce4,_0x143161);},'QeMdg':function(_0x12e6eb,_0xba85ff){return _0x12e6eb===_0xba85ff;},'YxmTF':_0x30c8('15','O5Nw'),'llOGE':function(_0x1981e6,_0x28618c){return _0x1981e6!==_0x28618c;},'dJItJ':_0x30c8('16','U61e'),'Mnnpv':_0x30c8('17','iCGG'),'ySxBA':_0x30c8('18',']srM'),'DljRk':_0x30c8('19','VjtX'),'ZPTRM':function(_0x5e1eb1,_0x2540b8){return _0x5e1eb1(_0x2540b8);},'pmTQl':_0x30c8('1a','plRg'),'KVgRD':_0x30c8('1b','I92F'),'LgFwx':function(_0x4b0d16,_0x5a18c8){return _0x4b0d16+_0x5a18c8;},'EkkyI':'邀请成功返回结果：','rRCTU':function(_0x1a8d08,_0x3832b6){return _0x1a8d08!==_0x3832b6;},'VWxbv':_0x30c8('1c','0G6v'),'QKDtJ':_0x30c8('1d',']QoG'),'nUGys':_0x30c8('1e','gNHI'),'CErlH':_0x30c8('1f','RWFj'),'dnGGV':_0x30c8('20','oi%f'),'FjORH':function(_0x16cef8,_0x2db489){return _0x16cef8!==_0x2db489;},'CxzBf':_0x30c8('21','zlQ1'),'GXAHD':_0x30c8('22','X4rn'),'OZzmi':'发起挑战','eLQqT':function(_0x42ca4c,_0x434031,_0x2af3a4,_0x1d94ec){return _0x42ca4c(_0x434031,_0x2af3a4,_0x1d94ec);},'VYxBJ':function(_0xcad405,_0x155541){return _0xcad405!==_0x155541;},'kCkHd':_0x30c8('23','d[Xo'),'EtjBB':_0x30c8('24','plRg'),'JdsOm':_0x30c8('25','X4rn'),'zcQXD':_0x30c8('26','01Uj'),'hSztN':_0x30c8('27','@Sbm'),'CTvum':_0x30c8('28','Z8iK'),'SIwXU':function(_0x2539ad,_0x129d8e){return _0x2539ad>_0x129d8e;},'uQsyl':function(_0x362f4b,_0x195341){return _0x362f4b+_0x195341;},'qSoVB':_0x30c8('29','^jv6'),'lTHxI':_0x30c8('2a','U61e'),'tKMtu':function(_0x31fcb5,_0x291f95){return _0x31fcb5==_0x291f95;},'iKKMl':'当前胜场:','yomkO':_0x30c8('2b','^JhI'),'tsZcR':_0x30c8('2c','VjtX'),'wwViX':function(_0x25f374,_0x5e8946){return _0x25f374+_0x5e8946;},'KxrfF':_0x30c8('2d','7cE1'),'IyzJG':function(_0x4f14df,_0x5de4ae){return _0x4f14df!==_0x5de4ae;},'KWzPv':_0x30c8('2e','plRg'),'dlETb':_0x30c8('2f','MsV%'),'GlNmA':_0x30c8('30','uSx)'),'vzYDi':_0x30c8('31','luiN'),'iJorA':'WaQBR','qNTIO':function(_0x17d9fc,_0x5eb36c){return _0x17d9fc!==_0x5eb36c;},'OYLyU':'uzNFA','LRuou':function(_0x3832ab,_0xa8e72d,_0x232922,_0x32c123,_0x4f6185,_0x5b9b65){return _0x3832ab(_0xa8e72d,_0x232922,_0x32c123,_0x4f6185,_0x5b9b65);},'TXEyN':function(_0x3e78ae,_0x35ac12,_0x363af3,_0x3bb19b){return _0x3e78ae(_0x35ac12,_0x363af3,_0x3bb19b);},'xRZjw':_0x30c8('32','GV(W'),'SpdMS':function(_0x169ab7,_0x5ce320){return _0x169ab7+_0x5ce320;},'uDsvD':function(_0x31ec17,_0x90a05c){return _0x31ec17+_0x90a05c;},'ZUaXB':_0x30c8('33','6kW9'),'msReG':function(_0x31696b,_0x1282d5){return _0x31696b(_0x1282d5);},'HTLPH':function(_0x2943bd,_0x576670){return _0x2943bd!==_0x576670;},'PzLia':_0x30c8('34','MsV%'),'fIZAQ':_0x30c8('35','oi%f'),'FHlJs':function(_0x3d574f,_0x788aff){return _0x3d574f(_0x788aff);},'GNPQY':_0x30c8('36','VjtX'),'WyNwM':_0x30c8('37','plRg'),'IbzCI':_0x30c8('38','mljN'),'ZwodK':function(_0x1b47ad,_0x219966){return _0x1b47ad+_0x219966;},'MiYkO':'IJUPB','aFIdg':_0x30c8('39','rZKe'),'PhuPC':function(_0x9c1896,_0x53999a){return _0x9c1896!==_0x53999a;},'AolzV':_0x30c8('3a','(FUP'),'ewrMj':function(_0x304910,_0x51a1){return _0x304910(_0x51a1);},'FKDDQ':function(_0x118619,_0xe9bfe0){return _0x118619===_0xe9bfe0;},'YDAtK':'FwCdf','Ewnty':function(_0x11c1c9,_0x169de1){return _0x11c1c9!==_0x169de1;},'DOLfz':'NLsrN','ZLAYW':'api.scriptsjd.cf','hwysQ':_0x30c8('3b','luiN'),'WLFQC':_0x30c8('3c','RWFj'),'IKFZP':_0x30c8('3d','@Sbm'),'IWvLd':_0x30c8('3e','X4rn'),'DqdoI':_0x30c8('3f','6kW9'),'UpjMl':_0x30c8('40','L$hY'),'eVWFt':'PveXi','mhFqs':_0x30c8('41','jxjg'),'WfrMN':_0x30c8('42','mljN'),'MqQbE':_0x30c8('43','Y!%2'),'qiAmU':function(_0x4560be,_0x3111e9){return _0x4560be!==_0x3111e9;},'LFHbl':_0x30c8('44','^JhI'),'MKDjv':function(_0x446d74,_0x463f7a){return _0x446d74+_0x463f7a;},'xBKfn':'https://api.scriptsjd.cf/api/JoyScore/CheckPin?','Rvmeb':function(_0x3dfb4a,_0x102853){return _0x3dfb4a+_0x102853;},'clARP':function(_0x2e0507,_0x4b51b7){return _0x2e0507!==_0x4b51b7;},'hJihP':'KXtaY'};async function _0x1ebd8b(){var _0x465748={'Jsuvx':function(_0x4b5df9,_0x53121a){return _0x43ad18[_0x30c8('45','XcJ3')](_0x4b5df9,_0x53121a);},'GcDZx':function(_0x3e7167,_0x1056e6){return _0x3e7167+_0x1056e6;},'FQkdv':_0x30c8('46','plRg'),'rERNl':function(_0x2e4093,_0xb3e820){return _0x43ad18[_0x30c8('47','iCGG')](_0x2e4093,_0xb3e820);},'FdpBz':_0x43ad18[_0x30c8('48','XcJ3')]};if(_0x43ad18[_0x30c8('49','mljN')](_0x43ad18[_0x30c8('4a','GV(W')],_0x43ad18['AiCSB'])){let _0x4d1c82=await _0x43ad18[_0x30c8('4b','VjtX')](getToken);let _0x333fdb=[];let _0x1b992c=[];console[_0x30c8('4c','plRg')](_0x30c8('4d','k)C[')+_0x4d1c82);if(_0x4d1c82){if(_0x43ad18[_0x30c8('4e',')Fy0')]===_0x43ad18[_0x30c8('4f','01Uj')]){console[_0x30c8('50','GV(W')](resp);}else{let _0x2714e3;let _0x912427=await getPin();if(_0x912427['Pin']){console[_0x30c8('51','O5Nw')](_0x43ad18[_0x30c8('52','pBh@')](_0x43ad18[_0x30c8('53','mljN')](_0x43ad18['txTTT'](_0x43ad18[_0x30c8('54','lYBt')],_0x912427['Pin']),_0x43ad18[_0x30c8('55','0G6v')]),_0x912427[_0x30c8('56','01Uj')]));}console['log'](_0x30c8('57',']srM'));await _0x43ad18[_0x30c8('58','Y!%2')](_0x2c58f2,APPID,_0x912427['Pin']);await _0x544b94(APPID,_0x912427[_0x30c8('59','luiN')]);let _0x2cb598=await _0x43ad18[_0x30c8('5a','O5Nw')](getUserPkInfo,_0x912427[_0x30c8('5b','&RN0')]);let _0x2f05ef=await _0x43ad18[_0x30c8('5c','^)iL')](_0x45834e,_0x912427[_0x30c8('5d','6kW9')],_0x912427['lkToken']);let _0x271c0e=await _0x43ad18[_0x30c8('5e','I92F')](getScore,_0x912427[_0x30c8('5f','Z8iK')]);let _0x3304d4={'PkPin':_0x912427['Pin'],'PtPin':$[_0x30c8('60','d[Xo')],'RandomStr':_0x2f05ef,'Score':_0x271c0e};await _0x43ad18['UYtSt'](_0x44194a,_0x3304d4);countlaunch=0x0;countreceive=0x0;let _0x502c47=await _0x43ad18[_0x30c8('61','sIct')](_0x59da8a,$['UserName']);if(_0x43ad18[_0x30c8('62',']QoG')](_0x502c47,0x0)){countreceive=_0x43ad18[_0x30c8('63','jyag')](_0x502c47,0x1);countlaunch=0x1;}let _0x284b2c=await _0x1ad35d(0x28,_0x271c0e);console[_0x30c8('64','^)iL')](_0x30c8('65','jyag')+_0x284b2c[_0x30c8('66','*mqV')]+_0x30c8('67','^)iL'));console['log'](_0x43ad18[_0x30c8('68','U61e')](_0x43ad18['zpWkQ'],_0x271c0e));if(_0x43ad18[_0x30c8('69','Y!%2')](_0x2cb598[_0x30c8('6a','gNHI')],0x0)&&_0x2cb598[_0x30c8('6b',']QoG')]-countreceive<=0x0){if(_0x43ad18[_0x30c8('6c','U61e')](_0x43ad18[_0x30c8('6d','d[Xo')],_0x43ad18[_0x30c8('6e','GV(W')])){resolve(res);}else{console['log'](_0x43ad18['SNfbO']);}}else{console[_0x30c8('6f','L$hY')](_0x43ad18['xMnYY']);if(_0x2cb598['leftLunchPkNum']>0x0){if(_0x43ad18[_0x30c8('70','^jv6')]===_0x30c8('71','zlQ1')){_0x2714e3=await _0x43ad18['UZxij'](getFriendPinList,_0x912427[_0x30c8('72','01Uj')]);if(_0x2714e3[_0x30c8('73','jyag')]>0x0){if(_0x43ad18[_0x30c8('74','*mqV')](_0x43ad18[_0x30c8('75','(FUP')],_0x43ad18[_0x30c8('76','U61e')])){let _0x248674,_0x5ea82b;for(let _0x571bbc=0x0;_0x43ad18[_0x30c8('77',']QoG')](_0x571bbc,_0x2714e3[_0x30c8('78','6kW9')]);_0x571bbc++){_0x248674=_0x2714e3[_0x571bbc];_0x5ea82b=await _0x43ad18[_0x30c8('79','gNHI')](getScore,_0x248674);console['log'](_0x43ad18[_0x30c8('7a','^)iL')](_0x43ad18[_0x30c8('7b',']QoG')](_0x43ad18[_0x30c8('7c','plRg')](_0x43ad18[_0x30c8('7d','luiN')](_0x43ad18[_0x30c8('7e','zlQ1')](_0x43ad18['yCdwz'],_0x248674),_0x43ad18['tRWgL']),_0x5ea82b),_0x30c8('7f','plRg')),_0x271c0e));_0x43ad18[_0x30c8('80','d^%B')](sleep,0x1f4);if(_0x43ad18['nHOBW'](_0x5ea82b,_0x271c0e)){if(_0x43ad18[_0x30c8('81',')Fy0')](_0x43ad18[_0x30c8('82','oi%f')],_0x30c8('83','jxjg'))){console['log'](_0x30c8('84','&RN0')+res);}else{if(countlaunch<_0x2cb598[_0x30c8('85','Z8iK')]){if(_0x43ad18[_0x30c8('86','SGb#')](_0x30c8('87','pBh@'),_0x30c8('88','lYBt'))){if(data[_0x30c8('89','k)C[')]){countreceive++;console[_0x30c8('8a','HTYc')](_0x465748[_0x30c8('8b','oi%f')](_0x30c8('8c','GV(W'),$['toStr'](data)));}else{bcomplate=!![];console[_0x30c8('8d','q4xr')](_0x465748[_0x30c8('8e','jxjg')](_0x465748[_0x30c8('8f','uSx)')],$[_0x30c8('90','YZ*b')](data)));}}else{_0x333fdb[_0x30c8('91','VjtX')](_0x248674);console['log'](_0x30c8('92','gNHI'));await _0x43ad18['GANzm'](_0x32df41,_0x248674,_0x912427[_0x30c8('93','d^%B')],_0x912427[_0x30c8('94','jxjg')]);}}else{break;}}}else{continue;}}}else{if(res){let _0x5d9e30=$['toObj'](res);resolve(_0x5d9e30);}}}else{console[_0x30c8('95','k)C[')](_0x43ad18[_0x30c8('96','(FUP')]);}}else{data=$[_0x30c8('97',')Fy0')](res);data=data['data'];if(data){console[_0x30c8('98','gNHI')](_0x43ad18['txTTT'](_0x43ad18['XOpfS'],data));_0x43ad18[_0x30c8('99','(FUP')](resolve,data);}}}else{console[_0x30c8('9a','zlQ1')](_0x43ad18['zecfr']);}console[_0x30c8('9b',']srM')](_0x30c8('9c','*mqV'));_0x2cb598=await _0x43ad18[_0x30c8('9d','I92F')](getUserPkInfo,_0x912427[_0x30c8('93','d^%B')]);if(_0x43ad18['LODZw'](_0x43ad18[_0x30c8('9e','@Sbm')](_0x2cb598[_0x30c8('9f','^jv6')],countreceive),0x0)){if(_0x43ad18[_0x30c8('a0','&RN0')](_0x30c8('a1','gNHI'),_0x43ad18[_0x30c8('a2','^)iL')])){if(_0x284b2c){if(_0x43ad18[_0x30c8('a3','plRg')]('ksyUJ',_0x43ad18[_0x30c8('a4','Y!%2')])){console[_0x30c8('a5','iCGG')](e);}else{for(let _0x3fccc4=0x0;_0x3fccc4<_0x284b2c['length'];_0x3fccc4++){let _0x248674=_0x284b2c[_0x3fccc4][_0x30c8('a6','pBh@')];let _0x4e7eb4=_0x284b2c[_0x3fccc4]['RandomStr'];let _0x5ea82b=_0x284b2c[_0x3fccc4]['Score'];let _0x22af87=0x1;if(_0x43ad18[_0x30c8('a7','pBh@')](_0x333fdb['indexOf'](_0x248674),-0x1)){if(_0x43ad18['MEcxQ'](_0x43ad18[_0x30c8('a8','^jv6')],_0x43ad18[_0x30c8('a9','jxjg')])){continue;}else{score=data[_0x30c8('aa','L$hY')];}}if(_0x2714e3!=null&&_0x2714e3['indexOf'](_0x248674)==-0x1){_0x22af87=0x1;}else{_0x22af87=0x2;}sleep(0x3e8);console[_0x30c8('ab','pBh@')](_0x43ad18['LsQuM'](_0x43ad18[_0x30c8('ac','oi%f')](_0x43ad18[_0x30c8('ad','XcJ3')](_0x43ad18[_0x30c8('ae','gNHI')](_0x43ad18[_0x30c8('af','luiN')](_0x43ad18[_0x30c8('b0','^)iL')],_0x248674),_0x43ad18['tRWgL']),_0x5ea82b),_0x43ad18[_0x30c8('b1','^jv6')]),_0x271c0e));if(_0x43ad18['nHOBW'](_0x5ea82b,_0x271c0e)){if(countreceive<_0x2cb598[_0x30c8('b2','d^%B')]){if(_0x43ad18[_0x30c8('b3','01Uj')](_0x43ad18[_0x30c8('b4','^)iL')],_0x30c8('b5','k)C['))){console['log'](_0x43ad18[_0x30c8('b6','gNHI')]);await _0x43ad18[_0x30c8('b7','plRg')](_0x39cced,_0x4e7eb4,_0x912427[_0x30c8('b8','^JhI')],_0x912427[_0x30c8('b9','Z8iK')],_0x22af87);if(bcomplate){if(_0x43ad18[_0x30c8('ba','gNHI')](_0x43ad18[_0x30c8('bb','U61e')],_0x43ad18['YxmTF'])){sleep(0x3e8);await _0x43ad18[_0x30c8('bc','I92F')](_0x3424bd,_0x4e7eb4,_0x912427[_0x30c8('bd','WHyS')],_0x912427[_0x30c8('be','iCGG')],0x1);}else{_0x465748[_0x30c8('bf','X4rn')](resolve,res);}}}else{console['log'](_0x43ad18[_0x30c8('c0','zlQ1')]);}}else{break;}}else{continue;}}console[_0x30c8('c1','v]s$')](_0x30c8('c2','WHyS'));}}else{if(_0x43ad18[_0x30c8('c3','sIct')](_0x43ad18[_0x30c8('c4','O5Nw')],_0x43ad18[_0x30c8('c5','YZ*b')])){_0x43ad18[_0x30c8('c6','mljN')](resolve,score);}else{console[_0x30c8('98','gNHI')](_0x30c8('c7','rZKe'));}}}else{resolve(res);}}else{console['log'](_0x43ad18[_0x30c8('c8','HTYc')]);}}if(kaixiang){if(_0x43ad18[_0x30c8('c9',']QoG')](_0x43ad18[_0x30c8('ca','L$hY')],_0x43ad18['ySxBA'])){console[_0x30c8('8a','HTYc')](_0x465748['GcDZx'](_0x30c8('cb','iCGG'),data[_0x30c8('cc','7cE1')][_0x30c8('cd','YZ*b')]));}else{console[_0x30c8('51','O5Nw')](_0x43ad18[_0x30c8('ce','oi%f')]);let _0x3043c5=await _0x43ad18['ZPTRM'](getBoxRewardInfo,_0x912427[_0x30c8('cf','^)iL')]);if(_0x3043c5['awards']){for(let _0x268f9d=0x0;_0x268f9d<_0x3043c5[_0x30c8('d0','6kW9')][_0x30c8('d1','rZKe')];_0x268f9d++){let _0x4c081a=_0x3043c5['awards'][_0x268f9d];if(_0x4c081a[_0x30c8('d2','I92F')]==0x0){if(_0x3043c5['totalWins']>=_0x4c081a['wins']){console['log'](_0x43ad18['dzWIU'](_0x43ad18[_0x30c8('d3','U61e')],_0x4c081a[_0x30c8('d4','@Sbm')][0x0][_0x30c8('d5','mljN')]));await _0x43ad18['SOufx'](sendBoxReward,_0x4c081a['id'],_0x912427['Pin']);}}}}console[_0x30c8('d6','jyag')](_0x43ad18[_0x30c8('d7','gNHI')]);}}}}}else{console[_0x30c8('d8','Z8iK')](_0x465748['FdpBz']);}};function _0x32df41(_0x3fa897,_0x2456bf,_0x27d0e3,_0x2a62bb=0x2){if(_0x43ad18[_0x30c8('d9','oi%f')](_0x43ad18[_0x30c8('da','VjtX')],_0x43ad18[_0x30c8('db','k)C[')])){console[_0x30c8('dc','aRZq')](_0x43ad18['OZzmi']);var _0x140ebc=new Date()[_0x30c8('dd','iCGG')]();let _0x5aebb8=_0x30c8('de','sIct')+_0x3fa897+_0x30c8('df','zlQ1')+_0x2a62bb+'}';const _0x384698=_0x14f5e4(APPID,md5Key,_0x5aebb8,_0x140ebc);const _0x8d1e4f=_0x30c8('e0','@Sbm')+APPID+_0x30c8('e1','lYBt')+_0x2456bf+_0x30c8('e2',']QoG')+_0x27d0e3+_0x30c8('e3','mljN')+_0x384698+_0x30c8('e4','&RN0')+_0x140ebc;const _0x248d8a=_0x43ad18[_0x30c8('e5','7cE1')](getPostRequest,_0x30c8('e6','7cE1'),_0x8d1e4f,_0x5aebb8);return new Promise(_0x967960=>{var _0x3c7eec={'ipyrK':function(_0x34c7be,_0x1a096c){return _0x43ad18[_0x30c8('e7','plRg')](_0x34c7be,_0x1a096c);},'uvNUb':_0x43ad18[_0x30c8('e8','mljN')],'rbxFl':function(_0x229ad0,_0x2c5c7b){return _0x43ad18['rRCTU'](_0x229ad0,_0x2c5c7b);},'zUDXk':_0x43ad18[_0x30c8('e9','gNHI')],'uHRlr':_0x30c8('ea','jyag'),'Idfwg':_0x30c8('eb','YZ*b'),'JVMRV':_0x43ad18['QKDtJ'],'nLOhc':function(_0x47bd19,_0x539357){return _0x43ad18[_0x30c8('ec','v]s$')](_0x47bd19,_0x539357);},'AfXye':_0x30c8('ed','&RN0'),'sYHpK':_0x43ad18[_0x30c8('ee','aRZq')],'sIUhF':_0x30c8('ef','aRZq'),'TwOmN':_0x30c8('f0','Y!%2'),'BHBzk':'mIwgp','ZngNE':function(_0x41f67b,_0x207d04){return _0x41f67b(_0x207d04);},'VydID':'KEocE','fzKWC':function(_0x35815c,_0x43177c){return _0x35815c(_0x43177c);}};if(_0x43ad18[_0x30c8('f1','SGb#')](_0x43ad18[_0x30c8('f2','sIct')],_0x43ad18['dnGGV'])){$[_0x30c8('f3','^JhI')](_0x248d8a,(_0x2c7d52,_0x4f7322,_0x4a3761)=>{var _0xff1b73={'MrDyd':function(_0x39da88,_0x298288){return _0x3c7eec[_0x30c8('f4',')Fy0')](_0x39da88,_0x298288);},'zTggu':_0x30c8('f5','sIct'),'WVkaa':_0x3c7eec[_0x30c8('f6','MsV%')]};try{if(_0x3c7eec[_0x30c8('f7','plRg')](_0x3c7eec[_0x30c8('f8','MsV%')],_0x3c7eec[_0x30c8('f9','Y!%2')])){if(_0x4a3761){let _0x26fffd=$[_0x30c8('fa','aRZq')](_0x4a3761);if(_0x26fffd){_0x26fffd=_0x26fffd[_0x30c8('fb','q4xr')];if(_0x26fffd[_0x30c8('fc','XcJ3')]){if(_0x3c7eec[_0x30c8('fd','q4xr')](_0x3c7eec[_0x30c8('fe','Y!%2')],_0x3c7eec['Idfwg'])){console['log'](_0xff1b73[_0x30c8('ff','&RN0')](_0xff1b73['zTggu'],$[_0x30c8('100','XcJ3')](_0x26fffd)));}else{if(_0x26fffd[_0x30c8('101','luiN')]>0x2){console[_0x30c8('102',']QoG')](_0x3c7eec[_0x30c8('103','SGb#')]+_0x26fffd[_0x30c8('104','HTYc')]);}}}else{if(_0x26fffd['pkResult']){if(_0x3c7eec[_0x30c8('105','^jv6')](_0x3c7eec[_0x30c8('106','jyag')],_0x3c7eec[_0x30c8('107','luiN')])){console[_0x30c8('9a','zlQ1')](_0x4f7322);}else{countlaunch++;console[_0x30c8('108',')Fy0')](_0x3c7eec[_0x30c8('109','I92F')]+$[_0x30c8('10a',']srM')](_0x26fffd));console[_0x30c8('10b','luiN')](_0x3c7eec[_0x30c8('10c','Y!%2')]+_0x26fffd[_0x30c8('10d','uSx)')]['fromWinNum']);}}else{if(_0x3c7eec[_0x30c8('10e','plRg')]===_0x3c7eec[_0x30c8('10f','d^%B')]){console['log'](_0x4f7322);}else{console[_0x30c8('d8','Z8iK')]('邀请成功需要等待接收PK：'+$[_0x30c8('110','L$hY')](_0x26fffd));}}_0x3c7eec[_0x30c8('111','aRZq')](sleep,0x3e8);}}}else{console[_0x30c8('112','I92F')](_0x30c8('113',']srM')+_0x4a3761);}}else{countlaunch++;console['log'](_0xff1b73[_0x30c8('114','jxjg')]+$['toStr'](data));console[_0x30c8('115','&RN0')](_0xff1b73[_0x30c8('116','mljN')](_0x30c8('117','SGb#'),data[_0x30c8('118','WHyS')]['fromWinNum']));}}catch(_0xabc36a){console[_0x30c8('95','k)C[')](_0x4f7322);}finally{if(_0x3c7eec['nLOhc'](_0x30c8('119','v]s$'),_0x3c7eec['VydID'])){console[_0x30c8('102',']QoG')](e);}else{_0x3c7eec[_0x30c8('11a','pBh@')](_0x967960,_0x4a3761);}}});}else{_0x3c7eec[_0x30c8('11b','luiN')](_0x967960,res);}});}else{resolve(res);}};function _0x39cced(_0x3b3393,_0x568808,_0x26c6d6,_0x9ef823=0x2){var _0xddea04={'Madkx':_0x30c8('11c','rZKe'),'rDpeJ':function(_0x51125d,_0x2d5151){return _0x43ad18[_0x30c8('11d','Z8iK')](_0x51125d,_0x2d5151);},'HRxnx':_0x43ad18[_0x30c8('11e','v]s$')],'FoaFH':_0x43ad18[_0x30c8('11f','oi%f')],'xfldJ':function(_0x291295,_0x2e6c3a){return _0x291295+_0x2e6c3a;},'cRJNP':_0x30c8('120','zlQ1'),'bWHKu':'邀请成功需要等待接收PK：','EuLKs':function(_0x32af06,_0x36be46){return _0x43ad18[_0x30c8('121','lYBt')](_0x32af06,_0x36be46);},'tFEjD':function(_0x4dd52c,_0x123125){return _0x43ad18['QeMdg'](_0x4dd52c,_0x123125);},'oDjFr':_0x43ad18[_0x30c8('122','oi%f')]};console[_0x30c8('123','MsV%')](_0x43ad18[_0x30c8('124',')Fy0')]);var _0x484855=new Date()[_0x30c8('dd','iCGG')]();let _0x552d13=_0x30c8('125','SGb#')+_0x3b3393+_0x30c8('df','zlQ1')+_0x9ef823+'}';const _0x1455c4=_0x14f5e4(APPID,md5Key,_0x552d13,_0x484855);const _0x2c8551=_0x30c8('126','0G6v')+APPID+_0x30c8('127','7cE1')+_0x568808+_0x30c8('128','L$hY')+_0x26c6d6+_0x30c8('129','XcJ3')+_0x1455c4+_0x30c8('12a','YZ*b')+_0x484855;const _0x335997=_0x43ad18[_0x30c8('12b','gNHI')](getPostRequest,_0x43ad18[_0x30c8('12c','I92F')],_0x2c8551,_0x552d13);return new Promise(_0x20442=>{var _0xdb020={'NLawb':function(_0x1d4f6f,_0x118b8a){return _0x1d4f6f+_0x118b8a;},'alnUU':_0xddea04[_0x30c8('12d','0G6v')],'VJily':function(_0x5c111d,_0x55a649){return _0xddea04[_0x30c8('12e','luiN')](_0x5c111d,_0x55a649);},'skmtO':_0xddea04[_0x30c8('12f','uSx)')],'GVQKg':_0x30c8('130','k)C['),'sjmJC':_0xddea04['FoaFH'],'MURdm':function(_0x1e493b,_0x19aee0){return _0xddea04['xfldJ'](_0x1e493b,_0x19aee0);},'eYvaD':_0xddea04[_0x30c8('131','iCGG')],'MIVKv':_0xddea04['bWHKu'],'NzNRX':function(_0xbef562,_0x1f9566){return _0xddea04[_0x30c8('132','zlQ1')](_0xbef562,_0x1f9566);},'xzDLV':function(_0x674816,_0x4dc87){return _0xddea04[_0x30c8('133','mljN')](_0x674816,_0x4dc87);},'AFhic':_0x30c8('134','jyag')};if(_0xddea04['tFEjD']('USZQH',_0xddea04[_0x30c8('135','q4xr')])){$[_0x30c8('136','k)C[')](_0x335997,(_0x1fd776,_0xcf8495,_0x4ff500)=>{var _0x3f53f4={'gcxsU':function(_0xdcf56d,_0x5b6802){return _0xdb020[_0x30c8('137','^JhI')](_0xdcf56d,_0x5b6802);},'mZTMe':_0xdb020[_0x30c8('138','XcJ3')]};try{if(_0x4ff500){let _0x22cbc4=$[_0x30c8('139','I92F')](_0x4ff500);if(_0x22cbc4){_0x22cbc4=_0x22cbc4[_0x30c8('13a','lYBt')];if(_0x22cbc4['msg']){if(_0x22cbc4[_0x30c8('13b','^jv6')]>0x2){if(_0xdb020['VJily'](_0xdb020['skmtO'],_0xdb020[_0x30c8('13c','X4rn')])){console[_0x30c8('98','gNHI')](_0xdb020['sjmJC']+_0x22cbc4['msg']);bcomplate=![];}else{console[_0x30c8('51','O5Nw')](_0x3f53f4[_0x30c8('13d','RWFj')](_0x3f53f4['mZTMe'],$[_0x30c8('13e','Y!%2')](_0xcf8495)));}}}else{if(_0x22cbc4[_0x30c8('13f','SGb#')]){countreceive++;console['log'](_0xdb020[_0x30c8('140','oi%f')](_0xdb020[_0x30c8('141','jyag')],$['toStr'](_0x22cbc4)));}else{bcomplate=!![];console['log'](_0xdb020[_0x30c8('142','U61e')]+$[_0x30c8('143','MsV%')](_0x22cbc4));}}}}else{bcomplate=![];console['log'](_0xdb020[_0x30c8('144','v]s$')]('发起邀请请求失败:',_0x4ff500));}}catch(_0x237a1e){console['log'](_0xcf8495);}finally{_0x20442(_0x4ff500);}});}else{console[_0x30c8('115','&RN0')](_0xdb020[_0x30c8('145','O5Nw')](_0xdb020['AFhic'],data['pkResult']['toWinNum']));}});};function _0x3424bd(_0x13586a,_0x3a3b12,_0x1569ae,_0x53e263){var _0x2fa303={'hOwTW':function(_0x16ddee,_0x30d341){return _0x43ad18[_0x30c8('146','O5Nw')](_0x16ddee,_0x30d341);},'ITSXz':function(_0x2c3397,_0x1f191e){return _0x43ad18[_0x30c8('147','@Sbm')](_0x2c3397,_0x1f191e);},'qmgEY':_0x43ad18[_0x30c8('148','RWFj')],'iQZfA':function(_0x3e0149,_0x35c58d){return _0x43ad18[_0x30c8('149','&RN0')](_0x3e0149,_0x35c58d);},'qyepS':_0x30c8('14a','01Uj'),'VFXyL':function(_0x39975e,_0x5b4e30){return _0x43ad18[_0x30c8('14b','(FUP')](_0x39975e,_0x5b4e30);},'oKgNc':_0x30c8('120','zlQ1'),'OiRFH':function(_0x393e1f,_0x383e18){return _0x43ad18[_0x30c8('14c','SGb#')](_0x393e1f,_0x383e18);},'qjhot':_0x30c8('14d','O5Nw'),'tMPEh':_0x43ad18[_0x30c8('14e','&RN0')],'AaHpU':_0x43ad18['lTHxI'],'TQioZ':function(_0x219950,_0x47dc9c){return _0x43ad18['tKMtu'](_0x219950,_0x47dc9c);},'aXYOI':function(_0x237ae9,_0x206bfc){return _0x43ad18['tKMtu'](_0x237ae9,_0x206bfc);},'iCvAt':_0x43ad18[_0x30c8('14f','7cE1')],'SGRvt':_0x43ad18[_0x30c8('150','SGb#')],'DoSUQ':_0x43ad18[_0x30c8('151','Y!%2')],'XowMe':function(_0x2ca3ea,_0x18f558){return _0x43ad18['wwViX'](_0x2ca3ea,_0x18f558);},'gHSNN':_0x43ad18['KxrfF'],'LqSls':function(_0x3831af,_0x1baff5){return _0x3831af(_0x1baff5);},'yIKWV':function(_0x19c7d4,_0x565a6e){return _0x43ad18[_0x30c8('152','L$hY')](_0x19c7d4,_0x565a6e);},'SeDSY':_0x43ad18[_0x30c8('153','zlQ1')],'IawHI':function(_0xdf2ceb,_0x22c5ff,_0x14b55b,_0x652b65,_0x26cc3a){return _0x43ad18[_0x30c8('154','7cE1')](_0xdf2ceb,_0x22c5ff,_0x14b55b,_0x652b65,_0x26cc3a);},'xgLJl':_0x43ad18[_0x30c8('155','sIct')]};if(_0x43ad18[_0x30c8('156','VjtX')]('SUVUx',_0x30c8('157','lYBt'))){console[_0x30c8('10b','luiN')](_0x43ad18[_0x30c8('158','*mqV')]);}else{console[_0x30c8('159','jxjg')](_0x43ad18['GlNmA']);return new Promise(_0x5b1e8b=>{var _0x2655d1={'nLxBC':function(_0x40b80b,_0x174613){return _0x2fa303['iQZfA'](_0x40b80b,_0x174613);},'hrnKD':_0x2fa303[_0x30c8('15a','I92F')],'UhtVe':function(_0x221358,_0x244b33){return _0x2fa303[_0x30c8('15b','jyag')](_0x221358,_0x244b33);},'HqRUm':_0x2fa303['oKgNc'],'YOKMi':function(_0x165535,_0x3001f5){return _0x2fa303['OiRFH'](_0x165535,_0x3001f5);},'GbXLX':'ZCxrg','hGuzk':_0x2fa303['qjhot'],'ENYMI':function(_0x357b,_0x93e444){return _0x357b!==_0x93e444;},'WLmEP':_0x2fa303[_0x30c8('15c','YZ*b')],'WoNGF':_0x2fa303[_0x30c8('15d','SGb#')],'ZDiTe':function(_0x5cc9fe,_0x5bd39a){return _0x2fa303[_0x30c8('15e','01Uj')](_0x5cc9fe,_0x5bd39a);},'KyoSm':function(_0x309a1c,_0x3862dc){return _0x2fa303[_0x30c8('15f','&RN0')](_0x309a1c,_0x3862dc);},'kWqWU':_0x2fa303[_0x30c8('160','d[Xo')],'ywrlf':_0x2fa303[_0x30c8('161','7cE1')],'oqlFO':_0x2fa303[_0x30c8('162','jyag')],'QRNMd':function(_0x514b63,_0x5b79bf){return _0x2fa303['XowMe'](_0x514b63,_0x5b79bf);},'HPtQp':function(_0x27057f,_0x1655aa){return _0x2fa303[_0x30c8('163','jyag')](_0x27057f,_0x1655aa);},'zxZBa':_0x2fa303['gHSNN'],'OroRk':'rAobD','SvdaA':function(_0xc8b321,_0x5117b6){return _0x2fa303[_0x30c8('164','X4rn')](_0xc8b321,_0x5117b6);}};if(_0x2fa303[_0x30c8('165','uSx)')](_0x2fa303[_0x30c8('166','Y!%2')],_0x30c8('167','d^%B'))){var _0x3fd4fd=new Date()[_0x30c8('168','VjtX')]();let _0x5e91a3='{\x22actId\x22:9,\x22randomStr\x22:\x22'+_0x13586a+'\x22}';const _0x191676=_0x2fa303[_0x30c8('169','@Sbm')](_0x14f5e4,APPID,md5Key,_0x5e91a3,_0x3fd4fd);const _0x100c36=_0x30c8('16a','VjtX')+APPID+_0x30c8('16b',']QoG')+_0x3a3b12+_0x30c8('16c','aRZq')+_0x1569ae+_0x30c8('16d','Z8iK')+_0x191676+'&t='+_0x3fd4fd;const _0x335690=getPostRequest(_0x2fa303[_0x30c8('16e','pBh@')],_0x100c36,_0x5e91a3);$[_0x30c8('16f','*mqV')](_0x335690,(_0x41fa63,_0x15fd93,_0x1a3377)=>{try{if(_0x2655d1['YOKMi'](_0x2655d1['GbXLX'],_0x2655d1[_0x30c8('170',']QoG')])){if(_0x2655d1[_0x30c8('171','rZKe')](data[_0x30c8('172','01Uj')],0x2)){console['log'](_0x2655d1['hrnKD']+data[_0x30c8('173','*mqV')]);bcomplate=![];}}else{if(_0x1a3377){let _0x3aa3b5=$[_0x30c8('174','iCGG')](_0x1a3377);if(_0x3aa3b5){if(_0x2655d1[_0x30c8('175','plRg')](_0x2655d1[_0x30c8('176','O5Nw')],_0x2655d1['WoNGF'])){_0x3aa3b5=_0x3aa3b5[_0x30c8('177','iCGG')];if(_0x2655d1[_0x30c8('178','I92F')](_0x3aa3b5[_0x30c8('179','^)iL')],0x1)){if(_0x3aa3b5[_0x30c8('17a','mljN')]){if(_0x2655d1[_0x30c8('17b','Y!%2')](_0x53e263,0x0)){console['log']('当前胜场:'+_0x3aa3b5[_0x30c8('17c','d^%B')][_0x30c8('17d','d^%B')]);}else{console['log'](_0x2655d1[_0x30c8('17e','XcJ3')]+_0x3aa3b5[_0x30c8('17f','^)iL')]['toWinNum']);}}countreceive++;}else{if(_0x2655d1[_0x30c8('180','rZKe')](_0x2655d1[_0x30c8('181',')Fy0')],_0x2655d1[_0x30c8('182','jyag')])){console[_0x30c8('4c','plRg')](_0x2655d1[_0x30c8('183','oi%f')]('PK结果其他信息',$[_0x30c8('184','iCGG')](_0x3aa3b5)));}else{countreceive++;console[_0x30c8('9b',']srM')](_0x2655d1['UhtVe'](_0x2655d1[_0x30c8('185','q4xr')],$[_0x30c8('186',')Fy0')](_0x3aa3b5)));}}}else{score=_0x3aa3b5[_0x30c8('187','^)iL')];}}}}}catch(_0x39b723){console['log'](_0x2655d1['HPtQp'](_0x2655d1[_0x30c8('188','HTYc')],$[_0x30c8('189','d[Xo')](_0x15fd93)));}finally{if('rAobD'===_0x2655d1[_0x30c8('18a','jxjg')]){_0x2655d1['SvdaA'](_0x5b1e8b,_0x1a3377);}else{str=appId+'_'+appMD5Key+'__'+timestamp;}}});}else{if(_0x2fa303[_0x30c8('18b','jxjg')](data[_0x30c8('18c','7cE1')],0x2)){console['log'](_0x2fa303[_0x30c8('18d','luiN')](_0x2fa303[_0x30c8('18e','q4xr')],data[_0x30c8('18f','VjtX')]));}}});}}function _0x14f5e4(_0x1074e9,_0x12c812,_0x4e7c3f,_0x2d0a43,_0x69b49a=0x0){if(_0x43ad18[_0x30c8('190',']QoG')]!=='WaQBR'){if(data[_0x30c8('191','U61e')]){countlaunch++;console[_0x30c8('10b','luiN')](_0x30c8('192','pBh@')+$[_0x30c8('193','HTYc')](data));console['log'](_0x43ad18[_0x30c8('194','oi%f')]('当前胜场:',data[_0x30c8('195','*mqV')]['fromWinNum']));}else{console[_0x30c8('98','gNHI')](_0x43ad18[_0x30c8('196','Z8iK')](_0x43ad18[_0x30c8('197','v]s$')],$['toStr'](data)));}sleep(0x3e8);}else{let _0x43895f;if(_0x43ad18[_0x30c8('198','*mqV')](_0x69b49a,0x0)){_0x43895f=_0x1074e9+'_'+_0x12c812+'_'+_0x4e7c3f+'_'+_0x2d0a43;}else{if(_0x43ad18['qNTIO'](_0x43ad18[_0x30c8('199',']QoG')],_0x30c8('19a','gNHI'))){console[_0x30c8('ab','pBh@')](resp);}else{_0x43895f=_0x1074e9+'_'+_0x12c812+'__'+_0x2d0a43;}}return $[_0x30c8('19b','k)C[')](_0x43895f);}}function _0x45834e(_0x3ed9a0,_0x5ea2eb){var _0x293b12={'iafmn':function(_0x3ceb50,_0x33452c){return _0x43ad18[_0x30c8('19c','L$hY')](_0x3ceb50,_0x33452c);},'mGQmo':_0x43ad18[_0x30c8('19d','YZ*b')],'paRLi':function(_0x480d76,_0x250db3){return _0x43ad18[_0x30c8('19e','(FUP')](_0x480d76,_0x250db3);},'BIWab':_0x43ad18[_0x30c8('19f','lYBt')],'TgVXL':function(_0x27efc4,_0x57c9c2){return _0x27efc4+_0x57c9c2;},'SKpLa':function(_0x2860ba,_0x41f4a7){return _0x43ad18[_0x30c8('1a0','q4xr')](_0x2860ba,_0x41f4a7);}};if(_0x43ad18['HTLPH'](_0x43ad18[_0x30c8('1a1',']srM')],_0x43ad18[_0x30c8('1a2','YZ*b')])){return new Promise(_0x2468db=>{var _0x146f7f=new Date()['getTime']();const _0x275d9f=_0x43ad18[_0x30c8('1a3','XcJ3')](_0x14f5e4,APPID,md5Key,'',_0x146f7f,0x1);const _0x228ddb=_0x30c8('1a4','lYBt')+_0x5ea2eb+_0x30c8('1a5','WHyS')+APPID+_0x30c8('1a6','@Sbm')+_0x3ed9a0+'&sign='+_0x275d9f+_0x30c8('1a7','7cE1')+_0x146f7f;const _0x4e906b=_0x43ad18[_0x30c8('1a8','mljN')](getGetRequest,_0x43ad18[_0x30c8('1a9','jyag')],_0x228ddb,0x0);$[_0x30c8('1aa','zlQ1')](_0x4e906b,(_0x4be399,_0x32e014,_0x2526f8)=>{var _0x28dc2c={'MUQDc':function(_0x1a1a12,_0x486af8){return _0x293b12[_0x30c8('1ab','XcJ3')](_0x1a1a12,_0x486af8);},'msJUr':_0x293b12[_0x30c8('1ac','SGb#')]};let _0x5222f9;try{if(_0x2526f8){if(_0x293b12[_0x30c8('1ad','SGb#')]('efaNQ',_0x293b12[_0x30c8('1ae','01Uj')])){_0x5222f9=$[_0x30c8('1af','&RN0')](_0x2526f8);_0x5222f9=_0x5222f9['data'];if(_0x5222f9){console[_0x30c8('6f','L$hY')](_0x293b12['TgVXL'](_0x30c8('1b0','XcJ3'),_0x5222f9));_0x293b12[_0x30c8('1b1','&RN0')](_0x2468db,_0x5222f9);}}else{console[_0x30c8('1b2','@Sbm')](_0x28dc2c[_0x30c8('1b3','v]s$')](_0x28dc2c[_0x30c8('1b4','Y!%2')],_0x5222f9));_0x2468db(_0x5222f9);}}}catch(_0x4388af){console[_0x30c8('c1','v]s$')](_0x32e014);}finally{_0x293b12['SKpLa'](_0x2468db,_0x5222f9);}});});}else{console[_0x30c8('64','^)iL')](_0x43ad18[_0x30c8('1b5',')Fy0')](_0x43ad18[_0x30c8('1b6','RWFj')](_0x43ad18[_0x30c8('1b7','@Sbm')](_0x43ad18[_0x30c8('1b8','*mqV')],myinfo[_0x30c8('1b9','GV(W')]),_0x43ad18[_0x30c8('1ba','6kW9')]),myinfo['lkToken']));}}function _0x2c58f2(_0x2fb443,_0x147ded){var _0x2b129b={'SJgxK':function(_0x2c1a97,_0x499510){return _0x43ad18[_0x30c8('1bb','SGb#')](_0x2c1a97,_0x499510);},'mAFvY':_0x43ad18[_0x30c8('1bc',')Fy0')],'QZFjU':_0x43ad18['WyNwM'],'ooLAl':function(_0x17007f,_0x5e9ab5){return _0x43ad18[_0x30c8('1bd','L$hY')](_0x17007f,_0x5e9ab5);},'WflVL':'nNbuQ'};const _0xc58a93=_0x30c8('1be','6kW9')+_0x2fb443+'&lkEPin='+_0x147ded;const _0x22092f=_0x43ad18[_0x30c8('1bf','plRg')](getGetRequest,_0x43ad18['IbzCI'],_0xc58a93);return new Promise(_0x3994ff=>{if(_0x43ad18[_0x30c8('1c0','U61e')](_0x30c8('1c1',']srM'),_0x30c8('1c2','*mqV'))){$[_0x30c8('1c3','luiN')](_0x22092f,(_0x1c9d4a,_0x3b8723,_0x409d8f)=>{var _0xc785c1={'dkWRO':function(_0x142e95,_0x17eaf2){return _0x2b129b[_0x30c8('1c4','WHyS')](_0x142e95,_0x17eaf2);},'gAsWX':'主动PK次数已完'};if(_0x2b129b[_0x30c8('1c5','HTYc')]!==_0x2b129b[_0x30c8('1c6','aRZq')]){let _0x260ca5=0x0;try{if(_0x409d8f){if(_0x2b129b[_0x30c8('1c7','iCGG')](_0x30c8('1c8','L$hY'),_0x2b129b[_0x30c8('1c9','luiN')])){_0xc785c1['dkWRO'](_0x3994ff,_0x409d8f);}else{let _0x524fc4=$[_0x30c8('1ca','d[Xo')](_0x409d8f);if(_0x524fc4){_0x260ca5=_0x524fc4[_0x30c8('1cb','jxjg')];}}}}catch(_0x5a5dd5){console['log'](_0x3b8723);}finally{_0x2b129b[_0x30c8('1cc','zlQ1')](_0x3994ff,_0x260ca5);}}else{console[_0x30c8('1cd','RWFj')](_0xc785c1[_0x30c8('1ce','jyag')]);}});}else{frelation=0x2;}});}function _0x544b94(_0x5241c1,_0x1e781e){const _0x4145f2='actId=9&appId='+_0x5241c1+_0x30c8('1cf','jxjg')+_0x1e781e;const _0x26905a=getGetRequest(_0x30c8('1d0','@Sbm'),_0x4145f2);return new Promise(_0x30e4f8=>{var _0x3c139c={'cpCXc':function(_0x49dc88,_0x55d7b4){return _0x43ad18[_0x30c8('1d1','7cE1')](_0x49dc88,_0x55d7b4);},'dmnkm':'获取分享PK码：','dqmub':function(_0x59b5c7,_0x2d4188){return _0x43ad18['FHlJs'](_0x59b5c7,_0x2d4188);},'hZfys':function(_0x1ef676,_0x3bffd5){return _0x43ad18[_0x30c8('1d2','01Uj')](_0x1ef676,_0x3bffd5);},'zUqud':function(_0x413bce,_0xee7be3){return _0x43ad18[_0x30c8('1d3','pBh@')](_0x413bce,_0xee7be3);},'BtdmT':_0x43ad18['MiYkO'],'arPVe':_0x43ad18['aFIdg'],'EsgKZ':function(_0x5ca243,_0xf77d61){return _0x43ad18['PhuPC'](_0x5ca243,_0xf77d61);},'tatea':_0x43ad18[_0x30c8('1d4','d^%B')],'UxMsu':_0x30c8('1d5','I92F')};$['get'](_0x26905a,(_0x4f8582,_0xf67a7d,_0x271ed6)=>{let _0x4ae7f9=0x0;try{if(_0x3c139c[_0x30c8('1d6','mljN')](_0x3c139c['BtdmT'],_0x3c139c['arPVe'])){if(_0x271ed6){data=$[_0x30c8('1d7','@Sbm')](_0x271ed6);data=data[_0x30c8('1d8','^jv6')];if(data){console['log'](_0x3c139c[_0x30c8('1d9','plRg')](_0x3c139c['dmnkm'],data));_0x3c139c[_0x30c8('1da','plRg')](_0x30e4f8,data);}}}else{if(_0x271ed6){if(_0x3c139c[_0x30c8('1db','d[Xo')](_0x3c139c[_0x30c8('1dc','7cE1')],_0x3c139c[_0x30c8('1dd','oi%f')])){_0x30e4f8(data);}else{let _0x426c36=$[_0x30c8('1de','6kW9')](_0x271ed6);if(_0x426c36){_0x4ae7f9=_0x426c36['data'];}}}}}catch(_0x10d81b){if(_0x3c139c[_0x30c8('1df','&RN0')]('FzdYi',_0x3c139c[_0x30c8('1e0','rZKe')])){console[_0x30c8('d6','jyag')](_0xf67a7d);}else{let _0x2e0aef;if(_0x3c139c[_0x30c8('1e1','v]s$')](isGet,0x0)){_0x2e0aef=appId+'_'+appMD5Key+'_'+body+'_'+timestamp;}else{_0x2e0aef=appId+'_'+appMD5Key+'__'+timestamp;}return $[_0x30c8('1e2','rZKe')](_0x2e0aef);}}finally{_0x30e4f8(_0x4ae7f9);}});});}function _0x44194a(_0x30e27b){var _0x520eda={'VAopc':function(_0x753a9e,_0x424c3a){return _0x43ad18[_0x30c8('1e3','gNHI')](_0x753a9e,_0x424c3a);},'kINnn':function(_0x2bf5f9,_0x45ac08){return _0x2bf5f9!==_0x45ac08;},'HGRrP':'LCFsq','VsAum':function(_0x1759bd,_0x17e210){return _0x43ad18[_0x30c8('1e4','Z8iK')](_0x1759bd,_0x17e210);},'FsgvD':_0x43ad18[_0x30c8('1e5','RWFj')]};if(_0x43ad18[_0x30c8('1e6','L$hY')](_0x30c8('1e7','plRg'),_0x43ad18[_0x30c8('1e8','I92F')])){console[_0x30c8('1e9','SGb#')](resp);}else{const _0x409355='https://api.scriptsjd.cf/api/JoyScore/Update';const _0x11a27b=_0x30c8('1ea','^JhI');const _0x2449c7={'Host':_0x43ad18[_0x30c8('1eb','GV(W')],'Content-Type':_0x43ad18[_0x30c8('1ec','uSx)')],'Connection':_0x43ad18[_0x30c8('1ed','HTYc')],'Accept':_0x43ad18[_0x30c8('1ee','SGb#')],'User-Agent':_0x43ad18[_0x30c8('1ef','zlQ1')],'Accept-Language':_0x43ad18[_0x30c8('1f0',')Fy0')]};let _0x1876be={'url':_0x409355,'method':_0x11a27b,'headers':_0x2449c7,'body':$[_0x30c8('90','YZ*b')](_0x30e27b)};return new Promise(_0xf7cacd=>{var _0x411458={'frzLM':function(_0x680735,_0x8d2b81){return _0x520eda[_0x30c8('1f1','iCGG')](_0x680735,_0x8d2b81);},'aPAlV':_0x30c8('1f2','pBh@'),'enfNV':function(_0x4b9415,_0x4742a9){return _0x520eda[_0x30c8('1f3','aRZq')](_0x4b9415,_0x4742a9);},'xuPte':_0x520eda[_0x30c8('1f4','jyag')],'WuNyA':'kAGWw','NfCab':function(_0x43267d,_0x5b8eac){return _0x520eda[_0x30c8('1f5','RWFj')](_0x43267d,_0x5b8eac);},'WJpnr':_0x520eda[_0x30c8('1f6',']srM')],'uxVwR':function(_0x53026e,_0x4e2b2d){return _0x520eda[_0x30c8('1f7','XcJ3')](_0x53026e,_0x4e2b2d);}};$[_0x30c8('1f8','YZ*b')](_0x1876be,(_0xa0128a,_0x37d741,_0x340e44)=>{var _0x1438c2={'xazma':function(_0x57a56a,_0x527d35){return _0x411458[_0x30c8('1f9','RWFj')](_0x57a56a,_0x527d35);},'QDoxr':_0x411458[_0x30c8('1fa','*mqV')]};try{if(_0x411458['enfNV'](_0x411458['xuPte'],_0x411458['WuNyA'])){if(_0x340e44){console[_0x30c8('1fb','0G6v')](_0x30c8('1fc','rZKe')+_0x340e44);}}else{if(_0x340e44){_0x1438c2[_0x30c8('1fd','6kW9')](_0xf7cacd,_0x340e44);}}}catch(_0x777622){if(_0x411458['NfCab'](_0x411458[_0x30c8('1fe','O5Nw')],_0x411458['WJpnr'])){console[_0x30c8('1ff','6kW9')](_0x777622);}else{console['log'](_0x1438c2[_0x30c8('200','uSx)')]+_0x340e44);}}finally{_0x411458[_0x30c8('201','RWFj')](_0xf7cacd,_0x340e44);}});});}};function _0x59da8a(_0x5579cd){var _0x5a84dd={'YDBHU':function(_0x5dcc08,_0x2ea95e){return _0x43ad18[_0x30c8('202','gNHI')](_0x5dcc08,_0x2ea95e);},'nqKzt':'被动邀请失败：'};return new Promise(_0x555017=>{var _0x1cf917={'zBelx':function(_0x1d3b02,_0x3888f1){return _0x1d3b02+_0x3888f1;},'ddXXp':_0x43ad18['UpjMl'],'pcslF':function(_0x22746d,_0x1ed518){return _0x43ad18[_0x30c8('203','7cE1')](_0x22746d,_0x1ed518);},'YiskP':_0x43ad18[_0x30c8('204','zlQ1')],'GFOsX':_0x43ad18[_0x30c8('205','^jv6')],'DbqkR':function(_0x5866ba,_0x5b4333){return _0x5866ba!==_0x5b4333;},'WlZqL':_0x43ad18[_0x30c8('206','YZ*b')],'pqfnw':_0x43ad18['MqQbE'],'TudZM':function(_0x3f7c93,_0x518d6e){return _0x3f7c93(_0x518d6e);},'wUWVJ':function(_0x548519,_0x47afcc){return _0x43ad18[_0x30c8('207','jxjg')](_0x548519,_0x47afcc);},'AUZta':'NOBWd','HCqrv':function(_0xf07780,_0x36c9c0){return _0xf07780(_0x36c9c0);}};if(_0x43ad18[_0x30c8('208','6kW9')](_0x43ad18['LFHbl'],_0x43ad18[_0x30c8('209','*mqV')])){console[_0x30c8('d6','jyag')](_0x5a84dd[_0x30c8('20a','(FUP')](_0x5a84dd[_0x30c8('20b','Y!%2')],data[_0x30c8('20c','U61e')]));bcomplate=![];}else{let _0x2f56d0=_0x43ad18[_0x30c8('20d','*mqV')](_0x43ad18[_0x30c8('20e','uSx)')],_0x30c8('20f','^JhI'))+_0x5579cd;let _0x508292={'url':_0x2f56d0,'headers':{'Host':_0x30c8('210','VjtX'),'Connection':_0x43ad18['WLFQC'],'Accept':_0x43ad18[_0x30c8('211','6kW9')],'User-Agent':_0x43ad18[_0x30c8('212','gNHI')],'Accept-Language':_0x43ad18[_0x30c8('213','YZ*b')]}};$[_0x30c8('214','k)C[')](_0x508292,(_0x268704,_0x3a218d,_0x1be052)=>{if(_0x1cf917[_0x30c8('215','luiN')](_0x1cf917['YiskP'],_0x1cf917[_0x30c8('216','0G6v')])){bcomplate=![];console[_0x30c8('217','YZ*b')](_0x1cf917[_0x30c8('218','6kW9')](_0x1cf917[_0x30c8('219','@Sbm')],_0x1be052));}else{try{if(_0x1cf917[_0x30c8('21a','(FUP')](_0x1cf917['WlZqL'],_0x1cf917['pqfnw'])){if(_0x1be052){_0x1cf917['TudZM'](_0x555017,_0x1be052);}}else{if(_0x1be052){console[_0x30c8('21b','7cE1')](_0x30c8('21c','RWFj')+_0x1be052);}}}catch(_0x2c59f0){console[_0x30c8('21d','(FUP')](_0x2c59f0);}finally{if(_0x1cf917[_0x30c8('21e','X4rn')](_0x1cf917[_0x30c8('21f','oi%f')],_0x1cf917[_0x30c8('220','Y!%2')])){countreceive=userCount-0x1;countlaunch=0x1;}else{_0x1cf917[_0x30c8('221','oi%f')](_0x555017,_0x1be052);}}}});}});}function _0x1ad35d(_0x335645,_0x29a4e0){var _0x2770af={'PHHhj':function(_0xbcfe24,_0x5d4eb9){return _0x43ad18[_0x30c8('222','HTYc')](_0xbcfe24,_0x5d4eb9);},'gJFWQ':function(_0x40d0ba,_0x4e006b){return _0x43ad18[_0x30c8('223','^)iL')](_0x40d0ba,_0x4e006b);},'EkBcL':function(_0x531fce,_0x17a006){return _0x531fce(_0x17a006);},'KTfnd':_0x30c8('224','SGb#'),'QrXGG':_0x30c8('225','VjtX'),'pfWhi':_0x43ad18['hJihP']};return new Promise(_0x4602f2=>{let _0x406b2e=_0x30c8('226','uSx)')+_0x335645+_0x30c8('227','oi%f')+_0x29a4e0;let _0x5ab800={'url':_0x406b2e,'headers':{'Host':_0x30c8('228','v]s$'),'Connection':_0x30c8('229','d^%B'),'Accept':_0x43ad18['IKFZP'],'User-Agent':_0x43ad18['IWvLd'],'Accept-Language':_0x43ad18[_0x30c8('22a','^JhI')]}};$[_0x30c8('22b','plRg')](_0x5ab800,(_0x57f714,_0x2beb4b,_0x1583a7)=>{var _0x549838={'zRALD':function(_0x24e07b,_0x3aed34){return _0x24e07b+_0x3aed34;},'pDJvf':_0x30c8('22c','jyag')};try{if(_0x2770af[_0x30c8('22d','I92F')](_0x30c8('22e','zlQ1'),_0x30c8('22f','GV(W'))){if(_0x1583a7){if(_0x2770af['gJFWQ'](_0x30c8('230','SGb#'),_0x30c8('231','*mqV'))){console[_0x30c8('232','01Uj')](e);}else{let _0x249f1e=$['toObj'](_0x1583a7);_0x2770af[_0x30c8('233','VjtX')](_0x4602f2,_0x249f1e);}}}else{let _0x3cc3ca=$[_0x30c8('234','(FUP')](_0x1583a7);if(_0x3cc3ca){_0x29a4e0=_0x3cc3ca[_0x30c8('187','^)iL')];}}}catch(_0x4ddffc){if(_0x2770af[_0x30c8('235','iCGG')](_0x2770af['KTfnd'],_0x2770af['KTfnd'])){console[_0x30c8('1b2','@Sbm')](_0x549838[_0x30c8('236','L$hY')](_0x549838[_0x30c8('237','q4xr')],data['msg']));}else{console[_0x30c8('217','YZ*b')](_0x4ddffc);}}finally{if(_0x2770af[_0x30c8('238','X4rn')]!==_0x2770af[_0x30c8('239','X4rn')]){_0x2770af[_0x30c8('23a','zlQ1')](_0x4602f2,_0x1583a7);}else{if(_0x1583a7){let _0x12ad7c=$['toObj'](_0x1583a7);if(_0x12ad7c){_0x29a4e0=_0x12ad7c[_0x30c8('23b','^JhI')];}}}}});});}_0x399b0e['main']=_0x1ebd8b;}($);;_0xodR='jsjiami.com.v6';

!(async () => {

    if (!cookiesArr[0]) {
        $.msg(
            $.name,
            "【提示】请先获取京东账号一cookie\n直接使用NobyDa的京东签到获取",
            "https://bean.m.jd.com/", {
            "open-url": "https://bean.m.jd.com/"
        }
        );
        return;
    }
    for (let i = 0; i < cookiesArr.length; i++) {
        if (cookiesArr[i]) {
            cookie = cookiesArr[i];
            $.UserName = decodeURIComponent(
                cookie.match(/pt_pin=([^; ]+)(?=;?)/) && cookie.match(/pt_pin=([^; ]+)(?=;?)/)[1]
            );
            $.index = i + 1;
            message = "";
            console.log(`\n******开始【京东账号${$.index}】${$.UserName}*********\n`);
            //await $.updatefriend();
            await $.main();
        }
    }
})()
    .catch((e) => {
        $.log("", `❌ ${$.name}, 失败! 原因: ${e}!`, "");
    })
    .finally(() => {
        $.done();
    })


//已改


//获取京享值分数
function getScore(fpin) {
    const mquery = `actId=9&appId=${APPID}&lkEPin=${fpin}`;
    const myRequest = getGetRequest('getScore', mquery);
    return new Promise((resolve) => {
        $.get(myRequest, (err, resp, res) => {
            let score = 0;
            try {
                if (res) {
                    let data = $.toObj(res);
                    if (data) {
                        score = data.data;
                    }
                }
            } catch (e) {
                console.log(resp);
            } finally {
                //  console.log("查询"+fpin+"分数  " + score );
                resolve(score);
            }
        });
    });
}



//获取用户PK余量信息
function getUserPkInfo(pin) {
    const mquery = `actId=9&appId=${APPID}&lkEPin=${pin}`;
    const myRequest = getGetRequest('getUserPkInfo', mquery);
    return new Promise((resolve) => {
        $.get(myRequest, (err, resp, res) => {

            try {
                if (res) {
                    let data = $.toObj(res);
                    data = data.data;
                    if (data) {
                        console.log(`${data.nickName}今天剩余主动邀请PK次数：${data.leftLunchPkNum} 被动邀请PK次数：${data.leftAcceptPkNum}`);
                        resolve(data);
                    }
                }
            } catch (e) {
                console.log("getUserPkInfo出错：" + resp);
            } finally {
                resolve();
            }
        });
    });
}
async function getFriendPinList(pin) {
    console.log("开始获取所有好友可以使用Pk列表中……");
    let allFriends = [];
    for (let i = 0; i < 100; i++) {
        let friends = await getUserFriendsPage(pin, i + 1);
        if (friends.length === 0) {
            console.log("好友列表到底了，共获取" + i + "页好友！！")
            break;
        }
        //console.log(`第${i+1}页`);
        for (let j = 0; j < friends.length; j++) {
            let item = friends[j];

            if (item.pkStatus == 2) {
                if (item.leftAcceptPkNum > 0 && item.leftLunchPkNum > 0) {
                    allFriends.push(item.friendPin);
                }
            }
        }
    }
    return allFriends;
}

//获取好友PK列表
function getUserFriendsPage(pin, pageNo) {
    //?actId=9&pageNo=2&pageSize=10&appId=dafbe42d5bff9d82298e5230eb8c3f79&lkEPin=13f5ef448152243c1e8c7a33f3b76dd20f296a206a12473f57d63d95f3be0534
    const mquery = `actId=9&pageNo=${pageNo}&pageSize=10&appId=${APPID}&lkEPin=${pin}`
    const myRequest = getGetRequest('getUserFriendsPage', mquery);
    return new Promise((resolve) => {
        $.get(myRequest, (err, resp, res) => {
            let data;
            try {
                if (res) {
                    data = $.toObj(res);
                    data = data.datas;
                    if (data) {
                        resolve(data);
                        //console.log("获取好友PK列表第" + pageNo + "页");
                    }
                }
            } catch (e) {
                console.log(resp);
            } finally {

                resolve(data);
            }
        });
    });
}


//已改
function getBoxRewardInfo(mypin) {
    return new Promise((resolve) => {
        const mquery = `actId=9&appId=${APPID}&lkEPin=${mypin}`;
        const myRequest = getGetRequest('getBoxRewardInfo', mquery);
        $.get(myRequest, (err, resp, res) => {
            try {

                if (res) {
                    let data = $.toObj(res);
                    if (data.success) {
                        // $.awards = data.data.awards;
                        //console.log($.toStr($.awards));
                        // $.totalWins=data.data.totalWins;
                        console.log("总胜场:" + data.data.totalWins);
                        resolve(data.data);
                    }

                }
            } catch (e) {
                console.log(resp);
            } finally {
                resolve(res);
            }
        });
    });
}

//已修复
function sendBoxReward(rewardConfigId, mypin) {
    return new Promise((resolve) => {
        console.log("进行开宝箱")
        const mquery = `rewardConfigId=${rewardConfigId}&actId=9&appId=${APPID}&lkEPin=${mypin}`
        const myRequest = getGetRequest('sendBoxReward', mquery);
        $.get(myRequest, (err, resp, res) => {
            try {
                console.log(res);
                if (res) {
                    let data = $.toObj(res);
                    if (data.success) {
                        for (let j = 0; j < data.datas.length; j++) {
                            console.log('获得奖励类型:' + data.datas[j].type + "京豆数量：" + data.datas[j].beanNum);
                        }

                    }

                }
            } catch (e) {
                console.log(resp);
            } finally {
                resolve(res);
            }
        });
    });
}

async function getPin() {
    return new Promise((resolve) => {
        let options = {
            "url": `https://jdjoy.jd.com/saas/framework/encrypt/pin?appId=${APPID}`,
            "headers": {
                "Host": "jdjoy.jd.com",
                "Origin": "https://prodev.m.jd.com",
                "Cookie": cookie,
                "Connection": "keep-alive",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "jdapp;iPhone;9.5.4;13.6;db48e750b34fe9cd5254d970a409af316d8b5cf3;network/wifi;ADID/38EE562E-B8B2-7B58-DFF3-D5A3CED0683A;model/iPhone10,3;addressid/0;appBuild/167668;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
                "Accept-Language": "zh-cn",
                "Referer": "https://prodev.m.jd.com/"
            }
        };

        $.post(options, (err, resp, res) => {
            try {

                // console.log(res);
                if (res) {
                    let data = $.toObj(res);
                    if (data) {
                        let minfo = { Pin: data.data.lkEPin, lkToken: data.data.lkToken };
                        resolve(minfo);
                        // $.pin = data.data.lkEPin
                        // $.lkToken=data.data.lkToken
                    }
                }
            } catch (e) {
                console.log(e);
            } finally {
                resolve();
            }
        });
    });
};

function getToken() {
    return new Promise((resolve) => {
        let options = {
            "url": `https://jdjoy.jd.com/saas/framework/user/token?appId=${APPID}&client=m&url=pengyougou.m.jd.com`,
            "headers": {
                "Host": "jdjoy.jd.com",
                "Origin": "https://prodev.m.jd.com",
                "Cookie": cookie,
                "Connection": "keep-alive",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "jdapp;iPhone;9.5.4;13.6;db48e750b34fe9cd5254d970a409af316d8b5cf3;network/wifi;ADID/38EE562E-B8B2-7B58-DFF3-D5A3CED0683A;model/iPhone10,3;addressid/0;appBuild/167668;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
                "Accept-Language": "zh-cn",
                "Referer": "https://prodev.m.jd.com/"
            }
        };
        $.post(options, (err, resp, res) => {
            let token;
            //console.log(JSON.stringify(res))
            try {
                if (res) {
                    let data = $.toObj(res);
                    if (data) {
                        token = data.data;
                    }

                }
            } catch (e) {
                console.log(e);
            } finally {
                resolve(token);
            }
        });
    });
};
function getGetRequest(type, query, checktype = 1) {
    let url;
    if (checktype == 0) {
        url = `https://pengyougou.m.jd.com/open/api/like/jxz/${type}?${query}`;
    } else {
        url = `https://pengyougou.m.jd.com/like/jxz/${type}?${query}`;
    }

    const method = `GET`;
    const headers = {
        'Accept': `*/*`,
        "Origin": `https://game-cdn.moxigame.cn`,
        'Sec-Fetch-Site': `cross-site`,
        'Sec-Fetch-Mode': `cors`,
        'Sec-Fetch-Dest': `empty`,
        'Connection': `keep-alive`,
        'Content-Type': `application/x-www-form-urlencoded`,
        'Referer': `https://game-cdn.moxigame.cn/`,
        'Accept-Encoding': `gzip, deflate, br`,
        'Host': `pengyougou.m.jd.com`,
        "User-Agent": "jdapp;iPhone;9.5.4;13.6;db48e750b34fe9cd5254d970a409af316d8b5cf3;network/wifi;ADID/38EE562E-B8B2-7B58-DFF3-D5A3CED0683A;model/iPhone10,3;addressid/0;appBuild/167668;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
        'Accept-Language': `zh-cn`
    };
    //console.log(url)
    return { url: url, method: method, headers: headers };
};

function getPostRequest(type, query, body) {
    const url = `https://pengyougou.m.jd.com/open/api/like/jxz/${type}?${query}`;
    const method = `POST`;
    const headers = {
        'Accept': `*/*`,
        'Origin': `https://game-cdn.moxigame.cn`,
        'Sec-Fetch-Site': `cross-site`,
        'Sec-Fetch-Mode': `cors`,
        'Sec-Fetch-Dest': `empty`,
        'Accept-Encoding': `gzip, deflate, br`,
        'Content-Type': `application/json;charset=UTF-8`,
        'Host': `pengyougou.m.jd.com`,
        'Connection': `keep-alive`,
        "User-Agent": "jdapp;iPhone;9.5.4;13.6;db48e750b34fe9cd5254d970a409af316d8b5cf3;network/wifi;ADID/38EE562E-B8B2-7B58-DFF3-D5A3CED0683A;model/iPhone10,3;addressid/0;appBuild/167668;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
        'Referer': `https://game-cdn.moxigame.cn/`,
        'Accept-Language': `zh-cn`
    };
    //console.log(url)
    return myRequest = { url: url, method: method, headers: headers, body: body };
};


function jsonParse(str) {
    if (typeof str == "string") {
        try {
            return JSON.parse(str);
        } catch (e) {
            console.log(e);
            $.msg($.name, "", "不要在BoxJS手动复制粘贴修改cookie");
            return [];
        }
    }
};

function sleep(timeout) {
    return new Promise((resolve) => setTimeout(resolve, timeout));
};



// prettier-ignore
function Env(t, e) { "undefined" != typeof process && JSON.stringify(process.env).indexOf("GITHUB") > -1 && process.exit(0); class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return "POST" === e && (s = this.post), new Promise((e, i) => { s.call(this, t, (t, s, r) => { t ? i(t) : e(s) }) }) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new class { constructor(t, e) { this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `🔔${this.name}, 开始!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const i = this.getdata(t); if (i) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise(e => { this.get({ url: t }, (t, s, i) => e(i)) }) } runScript(t, e) { return new Promise(s => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r; const [o, h] = i.split("@"), n = { url: `http://${h}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": o, Accept: "*/*" } }; this.post(n, (t, e, i) => s(i)) }).catch(t => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e); if (!s && !i) return {}; { const i = s ? t : e; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const i = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of i) if (r = Object(r)[t], void 0 === r) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, i, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}"; try { const e = JSON.parse(h); this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i) } catch (e) { const o = {}; this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i) } } else s = this.setval(t, e); return s } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null } setval(t, e) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null } initGotEnv(t) { this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = (() => { })) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); s && this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar } } catch (t) { this.logErr(t) } }).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) })) } post(t, e = (() => { })) { if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.post(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: s, ...i } = t; this.got.post(s, i).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) }) } } time(t, e = null) { const s = e ? new Date(e) : new Date; let i = { "M+": s.getMonth() + 1, "d+": s.getDate(), "H+": s.getHours(), "m+": s.getMinutes(), "s+": s.getSeconds(), "q+": Math.floor((s.getMonth() + 3) / 3), S: s.getMilliseconds() }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in i) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : ("00" + i[e]).substr(("" + i[e]).length))); return t } msg(e = t, s = "", i = "", r) { const o = t => { if (!t) return t; if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : this.isSurge() ? { url: t } : void 0; if ("object" == typeof t) { if (this.isLoon()) { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } if (this.isQuanX()) { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl; return { "open-url": e, "media-url": s } } if (this.isSurge()) { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } } }; if (this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))), !this.isMuteLog) { let t = ["", "==============📣系统通知📣=============="]; t.push(e), s && t.push(s), i && t.push(i), console.log(t.join("\n")), this.logs = this.logs.concat(t) } } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { const s = !this.isSurge() && !this.isQuanX() && !this.isLoon(); s ? this.log("", `❗️${this.name}, 错误!`, t.stack) : this.log("", `❗️${this.name}, 错误!`, t) } wait(t) { return new Promise(e => setTimeout(e, t)) } done(t = {}) { const e = (new Date).getTime(), s = (e - this.startTime) / 1e3; this.log("", `🔔${this.name}, 结束! 🕛 ${s} 秒`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } }(t, e) }
