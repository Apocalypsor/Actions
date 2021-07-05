CAN_NOTIFY = True
import datetime
import json
import os
import random
import time
from collections import defaultdict
from pprint import pprint
try:
    from notify import send
except Exception as e:
    CAN_NOTIFY = False
import requests

if CAN_NOTIFY:
    print('启用通知成功', flush=True)
else:
    print('启用通知失败，缺少notify.py', flush=True)

class Dwnc:
    GAME_ID = 'dwnc'
    VERSION = '1.2.2'
    ENV = 'release'
    IGNORE_URLS = ['/login']

    def __init__(self, openid=None, sessid=None, account=None, ua=None, character=None):
        self.ua = ua if ua else 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X)' \
                                ' AppleWebKit/605.1.15 (KHTML, like Gecko)' \
                                ' Mobile/15E148 MicroMessenger/8.0.7(0x1800072d) NetType/WIFI Language/zh_CN'
        self.character = 'Tomato Tycoon' if character in ['Tomato Tycoon', '番茄大亨', 'TomatoTycoon'] else '普通人'
        self.account = account if account else openid
        self.openid = openid
        self.sessid = sessid
        if not self.openid:
            raise Exception('请检查openid是否填写')
        if not self.sessid:
            raise Exception('请检查sessid是否填写')
        self.first = True
        # self.is_help = False
        self.order_task_finished = False
        self.invite_water_finished = False
        self._cache = {}
        self.level = 0
        self.gold = 0
        self.exp = 0
        self.coupon = 0
        self.redpack = 0
        self.diamond = 0
        self.cash = 0
        self.skip_info = {}
        self.sign_week_info = {}
        self.building_info = {}
        self.skip_list = {}
        self.thief_info = {}
        self.seeds_info = {}
        self.level_info = {}
        self.task_daily = {}
        self.helper_info = {}
        self.task_main = {}
        self.config = {}
        self.day_times = defaultdict(int)
        self.land_info = {}
        self.land_list = {}
        self.worker_list = {}
        self.worker_list2 = {}
        self.worker_info = {}
        self.sign_info = {}
        self.auction_list = {}
        self.load_setting()
        self.orders = {}
        self.warehouse = {}
        self.can_speed = True
        self.can_video = True
        self.can_gold = True

    def load_setting(self):
        headers = {
            'Host': 'cos.ucpopo.com',
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': self.ua,
            'Referer': 'https://servicewechat.com/wxdbbf991feed9e2ba/24/page-frame.html',
        }
        url = f'https://cos.ucpopo.com/dwnc/settings/v{self.VERSION}.json?ts={int(time.time())}'
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            raise Exception("配置文件获取失败，请检查版本号DWNC_VERSION是否正确")
        setting = res.json()
        self.thief_info = setting['thiefInfo']
        self.seeds_info = setting['seedInfo']
        self.level_info = setting['userLevel']
        self.task_daily = setting['taskDay']
        self.worker_info = setting['workerInfo']
        self.skip_info = setting['skinInfo']
        land_info = setting['landInfo']

        for landid, info in land_info.items():
            info['skip_info'] = self.skip_info.get(str(info['skinId']), {})
            land_info[landid] = info
        self.land_info = land_info

    @classmethod
    def random_wait(cls, a, b, message=None):
        r = a + random.random() * (b - a)
        if message:
            print(message + f',等待{r}s', flush=True)
        time.sleep(r)
        return r

    def look_video(self, t, zero=False, message=None):
        self.random_wait(35, 50, message)
        self.day_times[t] = self.day_times[t] + 1 if self.day_times.get(t, 0) else 1
        if self.day_times['video_advert'] >= self.config.get('DAY_VIDEO_MAX'):
            self.can_video = False
        if t == 'video_advert':
            self.print(f'剩余广告次数({t}): {self.day_times["video_advert"]}/{self.config.get("DAY_VIDEO_MAX")}')
        if self.day_times['land_speed'] >= self.config.get('DAY_SPEED_MAX'):
            self.can_speed = False
        if t == 'land_speed':
            self.print(f'剩余广告次数({t}): {self.day_times["land_speed"]}/{self.config.get("DAY_SPEED_MAX")}')
        if self.day_times['get_gold'] >= self.config.get('GET_GOLD_MAX'):
            self.can_gold = False
        if t == 'get_gold':
            self.print(f'剩余广告次数({t}): {self.day_times["get_gold"]}/{self.config.get("GET_GOLD_MAX")}')
        return self.get_is_video(zero)

    @staticmethod
    def print(*args):
        print(*args, flush=True)

    @classmethod
    def encode(cls, data, t):
        t = str(t) + cls.VERSION
        i = ""
        a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_+"
        data = json.dumps(data).replace(" ", "")
        for c in data:
            s = str(bin(ord(c)))[2:]
            o = 16 - len(s)
            for c in range(o):
                s = "0" + s
            i += s

        r = len(i) % 6

        if r:
            for n in range(6 - r):
                i += "0"
        l = ""
        while i:
            temp = i[0:6]
            i = i[6:]
            l += a[int(temp, 2)]

        d = ""

        for n in range(len(l)):
            p = a.index(l[n])
            h = ord(str(t)[n % len(t)])
            d += a[(p + h) % len(a): (p + h) % len(a) + 1]
        return d

    def get(self, url, data=None):
        # 1625505649919
        # 1625505910984
        t = int(time.time() * 1000)
        data = data if data else {}
        raw_data = data
        data['openid'] = self.openid
        data['sessid'] = self.sessid

        if url in self.IGNORE_URLS:
            data['gameid'] = self.GAME_ID
            data['ver'] = self.VERSION
            data['t'] = t
            data['env'] = self.ENV
        else:
            c = self.encode(data, t)
            data = {
                'c': c,
                'gameid': self.GAME_ID,
                'ver': self.VERSION,
                'env': self.ENV,
                't': t
            }
        if not url.startswith('http'):
            url = 'https://minigame.ucpopo.com/dwnc' + url

        headers = {
            'Host': 'minigame.ucpopo.com',
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': self.ua,
            'Referer': 'https://servicewechat.com/wxdbbf991feed9e2ba/24/page-frame.html',
        }

        res = requests.get(url, params=data, headers=headers)
        data = res.json()
        err = data.get('errMsg')
        if err:
            self.print(f'{url}\t{json.dumps(raw_data)}')
            self.print(err)
        return data

    def sign(self):
        self.look_video('other', message='签到看广告')
        data = self.get('/sign/continuousSign', {'isVideo': 2})
        times = data['signContinuous']['times']
        self.exp = data['exp']
        self.gold = data['gold']
        self.diamond = data['diamond']
        self.redpack = data['redpack']
        self.coupon = data['coupon']
        self.print(f'连续签到{times}天')

    def check_sign(self):
        if not self.sign_info.get('isTaked', 0):
            self.sign()
        else:
            self.print('已签到')

        w = datetime.datetime.now().weekday()
        week_sign = self.sign_week_info.get(str(w + 1))
        if not week_sign:
            self.get('/sign/weekSign', {'isVideo': 2})
        else:
            self.print('已打卡')

    def login(self):
        data = self.get('/login')
        if 'user' not in data.keys():
            if CAN_NOTIFY:
                send('动物农场', content=f'{self.account}\t登录失效, 换设备打开小程序，原有登录信息会过期，请重新获取')
            raise Exception('登录失效, 换设备打开小程序，原有登录信息会过期，请重新获取')
        self.random_wait(5, 10, message='没啥用的等待～假装在加载界面😂')
        land_list = data['user']['landList']
        self.land_list = land_list
        self.worker_list = data['user']['workerList']
        self.level = data['user']['level']
        self.exp = data['user']['exp']
        self.gold = data['user']['gold']
        self.cash = data['user']['cash']
        self.diamond = data['user']['diamond']
        self.config = data['ccon']
        self.day_times = data['user']['dayTimes']
        if self.day_times['video_advert'] >= self.config.get('DAY_VIDEO_MAX'):
            self.can_video = False
        if self.day_times['land_speed'] >= self.config.get('DAY_SPEED_MAX'):
            self.can_speed = False
        if self.day_times['get_gold'] >= self.config.get('GET_GOLD_MAX'):
            self.can_gold = False
        self.coupon = data['user']['coupon']
        self.account = data['user'].get('name', self.account)
        self.redpack = data['user']['redpack']
        self.orders = data['user']['orderList']
        self.warehouse = data['user']['cropList']
        self.sign_info = data['user']['signContinuous']
        self.sign_week_info = data['user']['signList']
        self.helper_info = data['user']['helper']
        self.skip_list = data['user']['skinList']
        self.building_info = data['user']['skinType']
        self.task_main = data['user']['taskMain']
        self.auction_list = data['user'].get('auctionList', [])
        now = time.time() * 1000
        for index, info in land_list.items():
            expire_time = info.get('expireTime')
            if expire_time:
                is_finish = now > info['expireTime']
                if is_finish:
                    self.reap(str(index), info['cropid'], red=info['redpack'])
                    self.plant(str(index))
                else:
                    if self.can_speed:
                        finish = self.speed(index)
                        if finish:
                            print(f"种植{index}号田")
                            self.plant(str(index))
            else:
                self.print(f"种植{index}号田")
                self.plant(str(index))

    def reap(self, id, crop_id, red=False):
        if self.is_full():
            return
        data = self.get('/land/reap', {'landid': id, 'isVideo': self.get_is_video(can_zero=False) if red else 0})
        if data.get('crop'):
            self.update_warehouse(data['crop'], crop_id)
        else:
            print(data, flush=True)

        self.random_wait(1, 3, message=f'收取{id}号田')

    def get_is_video(self, can_zero=True):
        a = random.random()
        if a > 0.1:
            return 2
        elif a > 0.9:
            return 1
        else:
            return 0 if can_zero else 1

    def speed(self, id):
        if not self.can_speed:
            return self.print('今日视频加速次数已达到上限')
        self.look_video('land_speed', message=f'加速{id}号田看广告')
        data = self.get('/land/videoSpeed', {'landid': id, 'isVideo': self.get_is_video(can_zero=False)})
        now = time.time() * 1000
        if data.get('errMsg'):
            print('已达到上限')
            self.can_speed = False
            return False
        self.print(f'加速{id}号田, 成功')
        if now > data['land']['expireTime']:
            return True
        else:
            return False
        # pprint(res.json())

    def get_seed_id(self):
        if self.level < 5:
            return self.seeds_info['1']
        seeds = self.which_lack()
        if not seeds:
            total = 0

            for k, v in self.warehouse.items():
                total += v['num']

            for sid, seed in self.seeds_info.items():
                if seed['unlock'] <= self.level:
                    if total:
                        seeds += [str(seed['id'])] * (total - self.warehouse.get(str(seed['id']), {}).get('num', 0)) * (
                                    total - self.warehouse.get(str(seed['id']), {}).get('num', 0))
                    else:
                        seeds.append(str(seed['id']))

        i = int(random.random() * len(seeds))
        if not len(seeds):
            return self.seeds_info['1']
        random.shuffle(seeds)
        self.print(f'选择种子:{self.seeds_info[str(seeds[i])]["name"]}')
        return self.seeds_info[str(seeds[i])]

    def which_lack(self):
        seeds = []
        for k, info in self.orders.items():
            goods = info.get('goods', [])
            for good in goods:
                num = good['num']
                good_id = good['id']
                if self.warehouse.get(good_id, {}).get('num', 0) < num:
                    seeds += [good_id] * (num - self.warehouse.get(good_id, {}).get('num', 0))
        random.shuffle(seeds)
        return seeds

    def plant(self, landid):
        if self.character == 'Tomato Tycoon':
            seed_id = '1'
        else:
            seed = self.get_seed_id()
            seed_id = seed['id']
        self.random_wait(1, 2, message=f'种植第{landid}块地')
        self.get('/land/plant', {'seedid': seed_id, 'landid': landid})

    def check_level(self):
        level_info = self.level_info.get(str(self.level))
        if self.exp >= level_info['exp'] and self.gold >= level_info['cost']:
            self.random_wait(1, 2, message=f'升级到{self.level + 1}级')
            self.get('/user/levelup')
        else:
            self.print(
                '升级所需:' + f'\t金币:{self.gold}/{level_info["cost"]}({round(self.gold / level_info["cost"] * 100, 2) if level_info["cost"] else 100}%)' + f'\t经验值:{self.exp}/{level_info["exp"]}({round(self.exp / level_info["exp"] * 100, 2) if level_info["exp"] else 100}%)')

    def check_order(self):
        unlock = False
        for order_id, order_info in self.orders.items():
            goods = order_info.get('goods')
            if goods:
                if self.order_task_finished and self.character == 'Tomato Tycoon':
                    continue
                finish = True
                for good in goods:
                    good_id = good['id']
                    need = int(good['num']) - int(self.warehouse.get(good_id, {}).get('num', 0))
                    if need > 0:
                        # buy_num = 0
                        for k in [2, 3]:
                            if need <= 0:
                                break
                            buy_num = self.buy(target=good_id, target_num=need - self.warehouse.get(good_id, {}).get('num', 0), k=k, full=1)
                            need -= buy_num

                        if need > 0:
                            finish = False

                if finish:
                    self.get('/order/done', {'orderid': order_id})
                    self.random_wait(1, 2, message=f'完成订单{order_id}')
                    for good in goods:
                        good_id = good['id']
                        need = good['num']
                        self.warehouse[good_id]['num'] = self.warehouse[good_id]['num'] - need
            elif not order_info.get('refreshTime') and self.can_video:
                self.look_video('video_advert', message=f'解锁第{order_id}个订单')
                self.get('/order/videoUnlock', {'orderid': order_id})
                unlock = True
            else:
                self.print('订单未刷新')

        if (len(self.orders.items()) < self.level_info.get(str(self.level))['order_good_max']) and (
        not unlock) and self.can_video:
            order_id = len(self.orders.items()) + 1
            self.look_video('video_advert', message=f'解锁第{order_id}个订单')
            self.get('/order/videoUnlock', {'orderid': order_id})

    def check_unlock_land(self):
        self.get('/land/unlock', {'landid': '1'})

    def check_daily(self):
        data = self.get('/task/getDayList')
        tasks = data['taskDay']
        is_take = False
        for task_id, task in tasks.items():
            task_name = self.task_daily.get(task_id)["name"]
            if task_id != '0':
                if self.task_daily.get(task_id):
                    need_done = self.task_daily.get(task_id)['times']
                    done_num = task['done']
                    if need_done == done_num and not task['isTake']:
                        # todo task done
                        self.random_wait(1, 2, message=f'完成任务{self.task_daily.get(task_id)["name"]}')
                        self.get('/task/takeDayAward', {'taskid': task_id})
                    else:
                        is_take = task['isTake']
                        if is_take:
                            if '完成订单' in task_name:
                                self.order_task_finished = True
                            if '邀请好友浇水' in task_name:
                                self.print('已完成邀请好友浇水')
                                self.invite_water_finished = True

        total = data['total']
        done = data['done']

        if total == done and not is_take:
            self.get('/task/takeChest')

    def check_worker(self):
        for i in range(len(self.land_list)):
            if (i + 1 > len(self.worker_list) or not self.worker_list.get(str(i + 1)).get('unlock')) and self.can_video:
                self.look_video('video_advert', message=f'看视频解锁工人{i + 1}')
                data = self.get('/worker/videoUnlock', {'workerid': str(i + 1)})
                num = data['worker']['video']
                self.print(f'解锁进度：{num} / {self.worker_info.get(str(i + 1))["unlock_video"]}')
                if int(num) == int(self.worker_info.get(str(i + 1))["unlock_video"]):
                    return True
                break
        return False

    def get_work(self):
        workers = []
        has_ten = False
        for _ in range(3):
            self.random_wait(1,3)
            data = self.get('/worker/getCatchList')
            for work in data.get('catchList', []):
                if not work.get('master', {}).get('id'):
                    level = work['level']
                    if level < self.level:
                        workers.append((level, work['openid']))
                        if level >= 10:
                            has_ten = True

            if has_ten:
                break
        return sorted(workers, key=lambda x:x[0], reverse=True)

    def check_catch_worker(self):
        for k, info in self.worker_list.items():
            if info.get('status') in [1, 2] and self.day_times.get('worker_catch', 0) < self.config.get('WORKER_CATCH_MAX', 10):
                # todo 抓
                self.random_wait(0.5, 1)
                worker = self.get_work()
                if worker:
                    worker = worker[0]
                    self.get('/worker/catch', {'workerid': k, 'otherid': worker[1]})
                    self.day_times['worker_catch'] += 1
            elif info.get('status') == 0:
                # todo 放
                if info.get('createtime'):
                    work_time = (time.time() - info['createtime'] // 1000) // 3600
                    if work_time >= 12:
                        self.random_wait(0.5, 1)
                        self.get('/worker/free', {'workerid': k})

            if info.get('gold', 0) > 1000:
                self.random_wait(0.5, 1)
                data = self.get('/worker/takeGold', {'workerid': k})
                self.update_gold(data)

    def check_open(self):
        types = {
            "1": {
                "id": 1,
                "name": "房子"
            },
            "2": {
                "id": 2,
                "name": "仓库"
            },
            "3": {
                "id": 3,
                "name": "水渠"
            },
            "4": {
                "id": 4,
                "name": "栅栏"
            },
            "5": {
                "id": 5,
                "name": "1号农田"
            },
            "6": {
                "id": 6,
                "name": "2号农田"
            },
            "7": {
                "id": 7,
                "name": "3号农田"
            },
            "8": {
                "id": 8,
                "name": "4号农田"
            },
            "9": {
                "id": 9,
                "name": "5号农田"
            },
            "10": {
                "id": 10,
                "name": "6号农田"
            },
            "11": {
                "id": 11,
                "name": "7号农田"
            },
            "12": {
                "id": 12,
                "name": "8号农田"
            },
            "13": {
                "id": 13,
                "name": "9号农田"
            }
        }
        continue_type = []
        for skin_id, info in self.skip_info.items():
            skip_type = info['type']
            if skip_type in continue_type:
                continue
            cur_id = self.building_info.get(str(skip_type), 0)
            if int(skin_id) > cur_id:
                need_level = info['level']
                cost = info['cost']
                self.print(f'解锁{types[str(skip_type)]["name"]}({info["name"]})所需: \t等级{self.level}/{need_level}\t金币:{self.gold}/{cost}({round(self.gold / cost * 100, 2) if cost else 100}%)')
                if self.gold >= cost and self.level >= need_level:
                    if skip_type >= 5 and self.level < 30:
                        self.get('/land/unlock', {'landid': str(skip_type - 4)})
                        self.random_wait(1, 2, message=f'解锁{info["name"]}')
                    else:
                        self.get('/skin/unlock', {'skinid': skin_id})
                        self.random_wait(1, 2, message=f'解锁{info["name"]}')
                continue_type.append(skip_type)



    def check_open_land(self):
        # for skipid, info in self.skip_info.items():
        #     need_level = info['level']
        #     cost = info['cost']



        land_info_sorted = sorted(self.land_info.items(), key=lambda x: x[0])
        for landid, info in land_info_sorted:
            if landid not in self.land_list.keys():
                need_level = info['skip_info']['level']
                cost = info['skip_info']['cost']
                self.print(f'解锁地块{landid}所需: \t等级{self.level}/{need_level}\t金币:{self.gold}/{cost}({round(self.gold / cost * 100, 2) if cost else 100}%)')
                if self.gold >= cost and self.level >= need_level:
                    self.get('/land/unlock', {'landid': str(landid)})
                    self.print(f'解锁地块{landid}')
                break

    def get_offline_award(self):
        try:
            duration = time.time() - self.helper_info['takeAwardTime'] / 1000
            if duration > 10000:
                data = self.get('/helper/takeOfflineAward',
                               {'isVideo': self.look_video('offline', message='看广告拿金币') if self.can_gold else 0})
                self.random_wait(1, 2, message=f'获取离线金币成功，当前金币{data["gold"]}')
                self.gold = data['gold']
        except Exception as e:
            self.print('没有离线收入')

    def check_helper_level(self):
        if self.helper_info['level'] < self.level and self.can_video:
            self.look_video('video_advert', message='看广告升级管家中……')
            data = self.get('/helper/levelup', {})
            self.helper_info = data['helper']

    def check_cash(self):
        self.print(f'当前资产：{self.redpack}🧧，兑换券{self.coupon}张, 💰{self.cash / 100}元')
        if self.redpack >= 500 and self.coupon >= 5:
            self.random_wait(1, 2, message='兑换5元红包')
            data = self.get('/user/redpack2cash', {'num': '500'})
            self.cash = data['cash']
            self.coupon = data['coupon']
            self.redpack = data['redpack']

        if self.cash > 30 and self.first:
            self.random_wait(1, 2, message=f'提现红包{self.cash / 100}元')
            self.get('/user/withdraw', {})
            if CAN_NOTIFY:
                send('动物农场', content=f'{self.account}\t提现红包{self.cash / 100}元')
            self.first = False

    def check_auction(self):
        if '2' in self.skip_list.keys() and self.can_video:
            for i in range(9):
                if not self.auction_list.get(str(i + 1), {}).get('unlock'):
                    self.look_video('video_advert', message='解锁拍卖位')
                    self.get('/auction/videoUnlock', {'auctionid': str(i + 1)})
                    return

    def check_unlock_skin(self):
        for k, v in self.skip_info.items():
            if k not in self.skip_list.keys() and self.level >= v['level'] and self.gold >= v['cost']:
                self.random_wait(1, 2, message=f'解锁{v["name"]}')
                self.get('/skin/unloc', {'skinid': k})

    def is_full(self, rate=1.0):
        skin_id = self.building_info.get('2')
        info = self.skip_info.get(str(skin_id))
        buff = info['buff']
        total = sum([v['num'] for v in self.warehouse.values()])
        return total >= (buff * rate)

    def update_warehouse(self, value, crop=None):
        if crop:
            value = value if isinstance(value, dict) else {'num': value}
            self.warehouse[str(crop)] = value
        else:
            value = value['cropList']
            self.warehouse.update(value)

    def update_gold(self, value):
        value = value['gold']
        self.gold = value

    def update(self, data):
        diamond = data.get('diamond')
        if diamond:
            self.diamond = diamond

        gold = data.get('gold')
        if gold:
            self.gold = gold

        redpack = data.get('redpack')
        if redpack:
            self.redpack = redpack

        coupon = data.get('coupon')
        if coupon:
            self.coupon = coupon

    def buy_page_cache(self, page):
        rs = self._cache.get(page)
        if rs:
            # self.print(f'查找低价拍卖,第{page}页, 从缓存')
            return rs
        self.random_wait(1, 2, message=f'查找低价拍卖,第{page}页')
        data = self.get('/auction/getList', {'page': page})
        if data.get('pageMax'):
            self._cache[page] = data
        return data

    def buy(self, target=None, target_num=None, k=1.5, full=0.6, gold=None):
        max_page = 0
        page = 1
        if self.is_full(full) or self.gold < (gold if gold else self.level * 2000):
            return 0
        have_buy_num = 0
        while page <= max_page or page == 1:
            data = self.buy_page_cache(page)
            max_page = data.get('pageMax', 1)
            max_page = max_page if max_page < 40 else 40
            goods = data['list']
            for good in goods:
                total_price = good['auction']['price']
                price = good['auction']['price'] / good['auction']['num']
                good_id = good['auction']['goodid']
                num = good["auction"]["num"]
                is_target = str(target) == str(good_id) if target else good_id
                open_id = good['openid']
                auctionid = good['auctionid']
                if is_target and self.seeds_info.get(str(good_id), {}).get('order_gold',
                                                             15) * k >= price and self.gold >= total_price and not self.is_full(full):
                    self.random_wait(1, 2, message=f'购买 {self.seeds_info.get(str(good_id))["name"]}*{good["auction"]["num"]}, 单价:{price}, 花费:{total_price}')
                    data = self.get('/auction/buy', {'sellerid': open_id, 'auctionid': auctionid})
                    if data.get('errMsg'):
                        self.print(data.get('errMsg'))
                    else:
                        self.update_gold(data)
                        self.update_warehouse(data)
                        have_buy_num += num
                    self._cache.pop(page, None)

                if target_num:
                    if target_num <= have_buy_num:
                        break

            if self.is_full():
                break

            page += 1
            if page > max_page:
                break

        return have_buy_num

    def help(self):
        def get_help_id():
            try:
                with open('.dwnc.help', 'r') as f:
                    return f.read()

            except Exception as e:
                return None

        def export_help_id(i):
            with open('.dwnc.help', 'w') as f:
                f.write(i)

        if self.day_times.get('land_water', 0) + 3 > self.config.get('DAY_WATER_MAX', 0):
            return

        openid = get_help_id()
        if not self.invite_water_finished:
            export_help_id(self.openid)

        if not openid or openid == self.openid:
            return

        self.get('/visit/lookUser', {'lookid': openid})
        self.random_wait(1, 2)
        data = self.get('/visit/lookFarm', {'lookid': openid})
        water_land_ids = []
        land_list = data['landList']
        self.random_wait(1, 2)
        for landid, info in land_list.items():
            if not info.get('water', 1):
                water_land_ids.append(landid)

        random.shuffle(water_land_ids)

        water_times = 0
        for land in water_land_ids:
            if self.day_times.get('land_water', 0) < self.config.get('DAY_WATER_MAX', 20):
                self.random_wait(0.1, 1, '浇水一次')
                data = self.get('/visit/water', {'lookid': openid, 'landid': land})
                try:
                    land_list[land] = data['land']
                except Exception as e:
                    pprint(data)
                self.day_times['land_water'] = self.day_times['land_water'] + 1
                water_times += 1
                if water_times >= 3:
                    break

        random.shuffle(water_land_ids)

        for land in water_land_ids:
            info = land_list.get(land)
            if info['steal'] == 1 or info['expireTime'] > time.time() * 1000:
                continue
            if self.is_full():
                break
            self.random_wait(0.1, 1, '偷一次')
            data = self.get('/visit/steal', {'lookid': openid, 'landid': land})
            self.update_warehouse(data['crop'], crop=info['cropid'])

    def get_unlack_good(self):
        needs = defaultdict(int)
        # sells = []
        unlack = {}
        for value in self.orders.values():
            goods = value.get('goods', [])
            for good in goods:
                needs[good['id']] += good['num']

        for k, info in self.warehouse.items():
            if str(k) == '1':
                if self.day_times.get('thief_times', 0) < self.config.get('DAY_THIEF_MAX'):
                    continue
            d = info['num'] - needs.get(k, 0)
            if d > 0:
                unlack[k] = d

        # random.shuffle(sells)
        return unlack

    def on_buy(self):
        data = self.get('/auction/getMy')
        unlack_goods = self.get_unlack_good()
        unlack_good_ids = list(unlack_goods.keys())
        random.shuffle(unlack_good_ids)
        for k, info in data.items():
            expire_time = info.get('expireTime')
            unlock = info.get('unlock')
            buyer_id = info.get('buyerid')
            if expire_time:
                now = time.time() * 1000
                if now >= expire_time:
                    pass

            if buyer_id:
                self.random_wait(1, 2, message=f'收取拍卖')
                self.get('/auction/takeGold', {'auctionid': k})

                if unlack_good_ids:
                    sell_good_id = unlack_good_ids.pop()
                    num = unlack_goods[sell_good_id]
                    num = num if num <= 20 else 20
                    self.random_wait(1,2, message=f'拍卖上架{num}个{self.seeds_info[sell_good_id]["name"]}')
                    self.get('/auction/on', {'auctionid': k, 'goodid': sell_good_id, 'num': num, 'price': self.seeds_info[sell_good_id]['order_gold'] * 3, 'time': 2})

            if not buyer_id and not expire_time and unlock:
                if unlack_good_ids:
                    sell_good_id = unlack_good_ids.pop()
                    num = unlack_goods[sell_good_id]
                    num = num if num <= 20 else 20
                    self.random_wait(1,2, message=f'拍卖上架{num}个{self.seeds_info[sell_good_id]["name"]}')
                    self.get('/auction/on', {'auctionid': k, 'goodid': sell_good_id, 'num': num, 'price': self.seeds_info[sell_good_id]['order_gold'] * 3, 'time': 2})

    def get_gold(self):
        if self.can_gold:
            data = self.get('/user/getGold', {'isVideo': self.look_video('get_gold', message='看广告获取金币')})
            self.gold = data.get('gold') if data.get('gold') else self.gold

    def check_task_main(self):
        if self.task_main.get('done'):
            task_id = self.task_main.get('id')
            if task_id:
                self.random_wait(1, 2, message=f"完成任务{self.task_main.get('name')}")
                data = self.get("/task/takeMainAward", {'taskid': task_id})
                self.update(data)

    def thief_win(self):
        if self.day_times.get('thief_times', 0) >= self.config.get('DAY_THIEF_MAX'):
            return

        thiefs = []
        for thief_id, info in self.thief_info.items():
            if self.level > info.get('unlock', 80):
                thiefs.append(info['id'])

        if not thiefs:
            return

        win_rate = os.getenv('DWNC_WIN_THIEF_RATE')
        win_rate = float(win_rate) if win_rate else 0.8
        r = random.random()
        thief_id = str(thiefs.pop())
        need_num = self.thief_info[thief_id]["hp_max"] * 3 - self.warehouse.get('1', {}).get("num", 0)

        for k in [3]:
            if need_num > 0:
                need_num -= self.buy('1', need_num, k=k, full=1, gold=2000)

        if need_num <= 0:
            self.random_wait(50, 70, message='正在挑战盗贼')
            if r < win_rate:
                data = self.get('/activity/thief/win', {'thiefid': thief_id, 'bullet': random.randint(self.thief_info[thief_id]["hp_max"] * 2, self.thief_info[thief_id]["hp_max"] * 3)})
                self.random_wait(1, 2, message=f'挑战盗贼:{self.thief_info[thief_id]["name"]}成功')
            else:
                data = self.get('/activity/thief/lose', {'thiefid': thief_id, 'bullet': random.randint(self.thief_info[thief_id]["hp_max"] * 2, self.thief_info[thief_id]["hp_max"] * 3)})
                self.random_wait(1, 2, message=f'挑战盗贼:{self.thief_info[thief_id]["name"]}失败')

            self.update(data)


if __name__ == '__main__':
    last = None
    print('本脚本仅用于学习', flush=True)

    def parse(account):
        params = account.split(';')
        data = {}
        for param in params:
            if '=' in param:
                k, v = param.split('=')
                data[k] = v
        return data

    # accounts = "openid=xxx;sessid=xxx;&openid=xxx;&sessid=xxx;"
    accounts = os.getenv('DWNC_AUTH', '')
    if not accounts:
        print('请设置环境变量DWNC_AUTH', flush=True)
    print(accounts, flush=True)

    # ua 【非必填】
    # ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.7(0x1800072d) NetType/WIFI Language/zh_CN"
    ua = os.getenv('DWNC_UA')

    # version = "1.1.9"
    version = os.getenv('DWNC_VERSION', '1.2.2')
    if ua:
        print(f'DWNC_UA:{ua}', flush=True)
    if version:
        Dwnc.VERSION = version
        print(f'DWNC_VERSION:{version}', flush=True)

    end_time_hour = int(os.getenv('DWNC_ENDTIME_HOUR', 22))

    accounts = [parse(account) for account in accounts.split('&') if account]
    accounts = [Dwnc(**account, ua=ua) for account in accounts]

    print(f'总计{len(accounts)}个账号', flush=True)
    while True:
        for dwnc in accounts:
            try:
                print(f'-------当前账号: {dwnc.account}({dwnc.character})-------')
                dwnc.login()
                dwnc.get_gold()
                dwnc.thief_win()
                dwnc.buy()
                dwnc.on_buy()
                dwnc.get_offline_award()
                dwnc.check_catch_worker()
                dwnc.check_sign()
                dwnc.check_cash()
                dwnc.check_open()
                dwnc.check_level()
                dwnc.check_daily()
                dwnc.check_order()
                dwnc.check_task_main()
                dwnc.help()
                for _ in range(random.randint(1, 3)):
                    status = dwnc.check_worker()
                    if status:
                        break
                for _ in range(random.randint(2, 6)):
                    dwnc.check_helper_level()
                for _ in range(random.randint(1, 3)):
                    dwnc.check_auction()

                # dwnc.first = False
                last = dwnc
                dwnc._cache = {}
                print('-------------------------------------------------\n\n\n\n')
            except Exception as e:
                print(e, flush=True)
            if datetime.datetime.now().hour >= end_time_hour:
                break

        end_time_hour = int(os.getenv('DWNC_ENDTIME_HOUR', 22))
        Dwnc.VERSION = os.getenv('DWNC_VERSION', '1.2.1')
        if last:
            if last.character == 'Tomato Tycoon':
                Dwnc.random_wait(100, 300, message='休息一会儿～～～～')
        else:
            Dwnc.random_wait(200, 600, message='休息一会儿～～～～')