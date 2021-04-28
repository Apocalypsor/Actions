import sys
import os
import requests


def notifyTG(tg_token: str, tg_chatID: str, service: str):
    msg = f"⚠️ *{service} 签到失败！*\n\n#提醒"
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


if __name__ == "__main__":
    tg_token = os.getenv("TG_TOKEN")
    tg_chatID = os.getenv("TG_CHATID")
    service = sys.argv[1]

    notifyTG(tg_token, tg_chatID, service)
