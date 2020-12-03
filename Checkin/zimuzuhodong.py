import requests
import json
import time
import os

def qiandao(cookies):
    headers["Cookie"] = 'PHPSESSID={}'.format(cookies)
    qiandao_login_url = "http://h5.rrhuodong.com/index.php?g=api/mission&m=clock&a=store&id=2"
    get(qiandao_login_url)
    info_url = "http://h5.rrhuodong.com/index.php?g=api/mission&m=index&a=user_info"
    info = json.loads(get(info_url).text)['data']
    print("{} 签到成功： 称昵：{} 等级：{} 人人钻：{} ".format(time.strftime("%Y-%m-%d %H:%M", time.localtime()),info['nickname'],info['main_group_name'],info['point']))
    headers.pop("Cookie")

def get_huodong(uid,token):
    huodong_login_url = "http://h5.rrhuodong.com/index.php?g=api/mission&m=index&a=login&uid={}&token={}".format(uid,token)
    return requests.utils.dict_from_cookiejar(get(huodong_login_url).cookies)['PHPSESSID']

def get_token():
    token_login_url = "http://a.zmzapi.com/index.php?g=api/public&m=v2&accesskey=519f9cab85c8059d17544947k361a827&client=2&a=login&account={}&password={}".format(username,passwd)
    return get(token_login_url).text

def get(url):
    content = requests.get(url.format(username,passwd), headers=headers, verify=False, allow_redirects=False)
    return content

if __name__ == '__main__':
    headers = {
    "User-Agent":"Mozilla/5.0 (Linux; U; Android 9; zh-cn; MI 6 Build/9.0) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1"
    }
    username = os.getenv('USERNAME')
    passwd = os.getenv('PASSWD')
    
    info = json.loads(get_token())
    uid,token = info['data']['uid'],info['data']['token']
    cookies = get_huodong(uid,token)
    qiandao(cookies)
