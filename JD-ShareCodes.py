import requests
import time
import os

# 东东农场
fruit_api = r"http://api.turinglabs.net/api/v1/jd/farm/create/"

# 东东萌宠
pet_api = r"http://api.turinglabs.net/api/v1/jd/pet/create/"

# 种豆得豆
plant_bean_api = r"http://api.turinglabs.net/api/v1/jd/bean/create/"

# 京喜工厂
dream_factory_api = r"http://api.turinglabs.net/api/v1/jd/jxfactory/create/"

# 京东赚赚
jdzz_api = r"https://code.chiang.fun/api/v1/jd/jdzz/create/"

# 疯狂的joy
jdjoy_api = r"https://code.chiang.fun/api/v1/jd/jdcrazyjoy/create/"

name = {
    fruit_api: "东东农场",
    pet_api: "东东萌宠",
    plant_bean_api: "种豆得豆",
    dream_factory_api: "京喜工厂",
    jdzz_api: "京东赚赚",
    jdjoy_api: "疯狂的joy",
}

sharecodes = {
    fruit_api: ["162e1936b67c44e489d5e9f2c19bf19e", "72d794ac40b5407b89b06dbf49b935b1"],
    pet_api: ["MTE1NDAxNzgwMDAwMDAwNDMwMzM5NjE=", "MTE1NDQ5MzYwMDAwMDAwNDMwMzM5Njk="],
    plant_bean_api: [
        "4npkonnsy7xi3dna3iw4in6t2ixkufx5rmoo5uq",
        "e7lhibzb3zek3gtlvnownonyawhg3fnp5txiq2a",
    ],
    dream_factory_api: ["Ll_BJZ0ycq8aIipapE1cUw==", "LfF5eSL8m4K8hD1b8MztSw=="],
    jdzz_api: ["S5KkcRxgY8QbQJxn3lv4Cdw", "S5KkcRBkao1zedRr2x_8Pdw"],
    jdjoy_api: ["AfTkMxFWZKDj6vs1Q8SPuqt9zd5YaBeE", "1ldyJmZ3vJwHoXm_caQTq6t9zd5YaBeE"],
}


def notifyTG(tg_token: str, tg_chatID: str, msg: str):
    tg_url = "https://api.telegram.org/bot" + tg_token + "/sendMessage"
    payload = {
        "chat_id": tg_chatID,
        "text": msg,
        "parse_mode": "markdown",
        "disable_web_page_preview": "true",
    }

    r = requests.post(tg_url, data=payload)
    if r.json()["ok"]:
        print("已成功发送到Telegram!")


def main():
    failed = ""
    for api, sharecode in sharecodes.items():
        for code in sharecode:
            i = 0
            while i < 3:
                try:
                    r = requests.get(
                        api + code,
                        timeout=10,
                    ).json()
                    if r["code"] == 200:
                        print("添加成功: " + api + code)
                        break
                    elif ("message" in r and "xist" in r["message"]) or (
                        "msg" in r and "xist" in r["msg"]
                    ):
                        print("互助码已存在: " + api + code)
                        break
                    else:
                        time.sleep(i * 30)
                        i += 1
                except Exception as e:
                    i += 1

            if i == 3:
                failed_msg = "添加错误: " + name[api] + " 互助码: " + code
                print(failed_msg)
                failed += failed_msg + "\n"

    return failed


if __name__ == "__main__":
    tg_token = os.getenv("TG_TOKEN")
    tg_chatID = os.getenv("TG_CHATID")

    msg = main()
    if msg:
        notifyTG(tg_token, tg_chatID, msg + "\n#京东互助码")
