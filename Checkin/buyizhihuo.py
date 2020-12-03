# -*- coding: UTF-8 -*-

import requests
import re
import os
import sys

def getFormHash(base_url: str, headers: dict):
    r = requests.get(base_url + '/plugin.php', headers=headers)
    matchObj = re.search(r"name=\"formhash\" value=\"(\w{8})\"", r.text, re.M|re.U)
    if matchObj:
        form_hash = matchObj.group(1)
        return(form_hash)
    else:
        print('未找到Form Hash')

def checkin(base_url: str, headers: dict):
    form_hash = getFormHash(base_url, headers)

    checkin_url = base_url + r'/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
    data = 'formhash=' + form_hash + '&qdxq=kx&qdmode=3&fastreply=0'
    r = requests.post(checkin_url, headers=headers, data=data)

    if re.search('恭喜你签到成功|您今日已经签到', r.text):
        return True
    else:
        return False

if __name__ == '__main__':
    cookie = os.getenv('COOKIE')

    base_url = r'https://www.byzhihuo.com'
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Referer': 'https://www.byzhihuo.com/plugin.php?id=dsu_paulsign:sign',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    result = checkin(base_url, headers)
    if result:
        print('不移之火签到成功！')
    else:
        sys.exit('不移之火签到失败！')
        
