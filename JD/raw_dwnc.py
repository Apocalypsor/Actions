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
    VERSION = os.getenv('DWNC_VERSION') if os.getenv('DWNC_VERSION') else '1.1.7'
    ENV = 'release'
    IGNORE_URLS = ['/login']

    def __init__(self, openid=None, sessid=None, account=None, ua=None):
        self.ua = ua if ua else 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.7(0x1800072d) NetType/WIFI Language/zh_CN'
        self.account = account if account else openid
        self.openid = openid
        self.sessid = sessid
        if not self.openid:
            raise Exception('请检查openid是否填写')
        if not self.sessid:
            raise Exception('请检查sessid是否填写')
        self.first = True
        self.is_help = False
        self._cache = {}
        self.level = 0
        self.gold = 0
        self.exp = 0
        self.coupon = 0
        self.redpack = 0
        self.diamond = 0
        self.cash = 0
        self.skip_info = {}
        self.building_info = {}
        self.skip_list = {}
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
        setting = {
            "shareInfo": {
                "default": {
                    "type": "default",
                    "title": "一起来种地，赚红包",
                    "imageUrl": "https://cos.ucpopo.com/dwnc/share/default.jpg",
                    "path": ""
                },
                "invite": {
                    "type": "invite",
                    "title": "新人奖5元我已经领到了，你快来领",
                    "imageUrl": "https://cos.ucpopo.com/dwnc/share/invite.jpg",
                    "path": ""
                },
                "water": {
                    "type": "water",
                    "title": "互助浇水，天天领红包",
                    "imageUrl": "https://cos.ucpopo.com/dwnc/share/water.jpg",
                    "path": ""
                },
                "get_award": {
                    "type": "get_award",
                    "title": "一起来种地，赚红包",
                    "imageUrl": "https://cos.ucpopo.com/dwnc/share/default.jpg",
                    "path": ""
                },
                "redpack": {
                    "type": "redpack",
                    "title": "有红包快来抢，手慢无！",
                    "imageUrl": "https://cos.ucpopo.com/dwnc/share/invite.jpg",
                    "path": ""
                }
            },
            "signInfo": {
                "1": {
                    "id": 1,
                    "name": "星期一",
                    "icon": "gold_1",
                    "gold": 3000,
                    "diamond": 0,
                    "redpack": 0
                },
                "2": {
                    "id": 2,
                    "name": "星期二",
                    "icon": "diamond_1",
                    "gold": 0,
                    "diamond": 15,
                    "redpack": 0
                },
                "3": {
                    "id": 3,
                    "name": "星期三",
                    "icon": "redpack_2",
                    "gold": 0,
                    "diamond": 0,
                    "redpack": 10
                },
                "4": {
                    "id": 4,
                    "name": "星期四",
                    "icon": "gold_2",
                    "gold": 5000,
                    "diamond": 0,
                    "redpack": 0
                },
                "5": {
                    "id": 5,
                    "name": "星期五",
                    "icon": "diamond_2",
                    "gold": 0,
                    "diamond": 20,
                    "redpack": 0
                },
                "6": {
                    "id": 6,
                    "name": "星期六",
                    "icon": "redpack_1",
                    "gold": 0,
                    "diamond": 0,
                    "redpack": 5
                },
                "7": {
                    "id": 7,
                    "name": "星期日",
                    "icon": "chest",
                    "gold": 9999,
                    "diamond": 30,
                    "redpack": 10
                }
            },
            "inviteInfo": {
                "1": {
                    "id": 1,
                    "name": "邀请1人，奖励",
                    "num": 1,
                    "sum": 1,
                    "award": 20
                },
                "2": {
                    "id": 2,
                    "name": "再邀请4人，奖励",
                    "num": 4,
                    "sum": 5,
                    "award": 100
                },
                "3": {
                    "id": 3,
                    "name": "再邀请10人，奖励",
                    "num": 10,
                    "sum": 15,
                    "award": 300
                }
            },
            "typeRedpack": {
                "1": {
                    "id": 1,
                    "name": "%s产出"
                },
                "2": {
                    "id": 2,
                    "name": "兑换红包"
                },
                "3": {
                    "id": 3,
                    "name": "兑换钻石"
                },
                "4": {
                    "id": 4,
                    "name": "从%s的农场偷取"
                },
                "5": {
                    "id": 5,
                    "name": "签到"
                },
                "6": {
                    "id": 6,
                    "name": "主线任务奖励"
                },
                "7": {
                    "id": 7,
                    "name": "聊天送出"
                },
                "8": {
                    "id": 8,
                    "name": "聊天送出"
                },
                "9": {
                    "id": 9,
                    "name": "聊天福利包"
                },
                "10": {
                    "id": 10,
                    "name": "聊天福利包"
                }
            },
            "typeMessage": {
                "1": {
                    "id": 1,
                    "name": "访问了你的农场",
                    "tip": ""
                },
                "2": {
                    "id": 2,
                    "name": "给%s",
                    "tip": "浇水"
                },
                "3": {
                    "id": 3,
                    "name": "偷了你的",
                    "tip": "x%s"
                },
                "4": {
                    "id": 4,
                    "name": "刚偷走了",
                    "tip": "x%s"
                },
                "5": {
                    "id": 5,
                    "name": "把你抓去打工了",
                    "tip": ""
                },
                "6": {
                    "id": 6,
                    "name": "把你放了",
                    "tip": ""
                },
                "7": {
                    "id": 7,
                    "name": "从你的农场逃跑了",
                    "tip": ""
                },
                "8": {
                    "id": 8,
                    "name": "抢走了你的短工",
                    "tip": ""
                },
                "9": {
                    "id": 9,
                    "name": "把你抢去打工了",
                    "tip": ""
                },
                "10": {
                    "id": 10,
                    "name": "买了你的",
                    "tip": "x%s"
                }
            },
            "taskDay": {
                "0": {
                    "id": 0,
                    "name": "完成所有任务",
                    "times": 0,
                    "sort": 0,
                    "award_gold": 12000,
                    "award_exp": 4500,
                    "award_diamond": 50
                },
                "1": {
                    "id": 1,
                    "name": "每日签到",
                    "times": 1,
                    "sort": 1,
                    "award_gold": 500,
                    "award_exp": 0,
                    "award_diamond": 0
                },
                "2": {
                    "id": 2,
                    "name": "种植(%s/%s)次",
                    "times": 3,
                    "sort": 2,
                    "award_gold": 1000,
                    "award_exp": 0,
                    "award_diamond": 0
                },
                "3": {
                    "id": 3,
                    "name": "给好友浇水(%s/%s)次",
                    "times": 3,
                    "sort": 5,
                    "award_gold": 2000,
                    "award_exp": 0,
                    "award_diamond": 0
                },
                "4": {
                    "id": 4,
                    "name": "到好友农场偷取(%s/%s)次",
                    "times": 3,
                    "sort": 6,
                    "award_gold": 3000,
                    "award_exp": 0,
                    "award_diamond": 0
                },
                "5": {
                    "id": 5,
                    "name": "收获农作物(%s/%s)次",
                    "times": 20,
                    "sort": 3,
                    "award_gold": 0,
                    "award_exp": 1500,
                    "award_diamond": 0
                },
                "6": {
                    "id": 6,
                    "name": "完成订单(%s/%s)次",
                    "times": 10,
                    "sort": 7,
                    "award_gold": 0,
                    "award_exp": 2000,
                    "award_diamond": 0
                },
                "7": {
                    "id": 7,
                    "name": "拍卖物品(%s/%s)次",
                    "times": 1,
                    "sort": 9,
                    "award_gold": 0,
                    "award_exp": 500,
                    "award_diamond": 0
                },
                "8": {
                    "id": 8,
                    "name": "市场购买(%s/%s)次",
                    "times": 5,
                    "sort": 10,
                    "award_gold": 0,
                    "award_exp": 1000,
                    "award_diamond": 0
                },
                "9": {
                    "id": 9,
                    "name": "抓或抢短工(%s/%s)次",
                    "times": 3,
                    "sort": 8,
                    "award_gold": 0,
                    "award_exp": 0,
                    "award_diamond": 10
                },
                "10": {
                    "id": 10,
                    "name": "邀请好友浇水(%s/%s)次",
                    "times": 3,
                    "sort": 4,
                    "award_gold": 0,
                    "award_exp": 0,
                    "award_diamond": 20
                }
            },
            "taskTitle": {
                "1": {
                    "id": 1,
                    "name": "邀请好友(%s/%s)人",
                    "title": "宣传员",
                    "times": 10,
                    "sort": 1
                },
                "2": {
                    "id": 2,
                    "name": "邀请好友(%s/%s)人",
                    "title": "代言人",
                    "times": 50,
                    "sort": 2
                },
                "3": {
                    "id": 3,
                    "name": "邀请好友(%s/%s)人",
                    "title": "形象大使",
                    "times": 200,
                    "sort": 3
                },
                "4": {
                    "id": 4,
                    "name": "种植作物(%s/%s)次",
                    "title": "垦荒达人",
                    "times": 10000,
                    "sort": 4
                },
                "5": {
                    "id": 5,
                    "name": "解锁(%s/%s)块黄土地",
                    "title": "小农场主",
                    "times": 9,
                    "sort": 5
                },
                "6": {
                    "id": 6,
                    "name": "解锁(%s/%s)块红土地",
                    "title": "大农场主",
                    "times": 9,
                    "sort": 6
                },
                "7": {
                    "id": 7,
                    "name": "解锁(%s/%s)块黑土地",
                    "title": "高级农场主",
                    "times": 9,
                    "sort": 7
                },
                "8": {
                    "id": 8,
                    "name": "解锁(%s/%s)块金土地",
                    "title": "农场大亨",
                    "times": 9,
                    "sort": 8
                },
                "9": {
                    "id": 9,
                    "name": "抓短工(%s/%s)次",
                    "title": "奴隶主",
                    "times": 5000,
                    "sort": 9
                },
                "10": {
                    "id": 10,
                    "name": "抢短工(%s/%s)次",
                    "title": "抢夺者",
                    "times": 1000,
                    "sort": 10
                },
                "11": {
                    "id": 11,
                    "name": "拍卖售出(%s/%s)件",
                    "title": "商业大亨",
                    "times": 10000,
                    "sort": 11
                },
                "12": {
                    "id": 12,
                    "name": "市场购买(%s/%s)次",
                    "title": "砍手党",
                    "times": 5000,
                    "sort": 12
                },
                "13": {
                    "id": 13,
                    "name": "完成订单(%s/%s)次",
                    "title": "订单王者",
                    "times": 10000,
                    "sort": 13
                },
                "14": {
                    "id": 14,
                    "name": "解锁所有动物(%s/%s)",
                    "title": "伪装大师",
                    "times": 50,
                    "sort": 14
                },
                "15": {
                    "id": 15,
                    "name": "浇水(%s/%s)次",
                    "title": "雨神",
                    "times": 10000,
                    "sort": 15
                },
                "16": {
                    "id": 16,
                    "name": "累计偷菜(%s/%s)kg",
                    "title": "金手指",
                    "times": 2000,
                    "sort": 16
                },
                "17": {
                    "id": 17,
                    "name": "累计偷菜(%s/%s)kg",
                    "title": "神偷",
                    "times": 50000,
                    "sort": 17
                },
                "18": {
                    "id": 18,
                    "name": "累计聊天(%s/%s)句",
                    "title": "话痨",
                    "times": 1000,
                    "sort": 18
                },
                "19": {
                    "id": 19,
                    "name": "累计聊天(%s/%s)句",
                    "title": "超级活跃",
                    "times": 5000,
                    "sort": 19
                },
                "20": {
                    "id": 20,
                    "name": "取得公会战第1名(%s/%s)次",
                    "title": "战神",
                    "times": 30,
                    "sort": 20
                }
            },
            "payInfo": {
                "1": {
                    "id": 1,
                    "name": "首充",
                    "type": 0,
                    "desc": "300钻+10天白银VIP",
                    "diamond": 300,
                    "vip_day": 10,
                    "price": 600
                },
                "2": {
                    "id": 2,
                    "name": "6元",
                    "type": 1,
                    "desc": "600钻",
                    "diamond": 600,
                    "vip_day": 0,
                    "price": 600
                },
                "3": {
                    "id": 3,
                    "name": "30元",
                    "type": 1,
                    "desc": "3000钻\n另赠150",
                    "diamond": 3150,
                    "vip_day": 0,
                    "price": 3000
                },
                "4": {
                    "id": 4,
                    "name": "128元",
                    "type": 1,
                    "desc": "12800钻\n另赠1280",
                    "diamond": 14080,
                    "vip_day": 0,
                    "price": 12800
                },
                "5": {
                    "id": 5,
                    "name": "30元",
                    "type": 2,
                    "desc": "白银VIP30天",
                    "diamond": 0,
                    "vip_day": 30,
                    "price": 3000
                },
                "6": {
                    "id": 6,
                    "name": "128元",
                    "type": 2,
                    "desc": "黄金VIP30天",
                    "diamond": 0,
                    "vip_day": 30,
                    "price": 12800
                },
                "7": {
                    "id": 7,
                    "name": "648元",
                    "type": 2,
                    "desc": "钻石VIP30天",
                    "diamond": 0,
                    "vip_day": 30,
                    "price": 64800
                }
            },
            "userLevel": {
                "1": {
                    "level": 1,
                    "exp": 10,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 1,
                    "order_refresh_min": 30,
                    "order_refresh_max": 30,
                    "worker_gold": 0.1,
                    "video_gold": 100
                },
                "2": {
                    "level": 2,
                    "exp": 50,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 2,
                    "order_refresh_min": 30,
                    "order_refresh_max": 30,
                    "worker_gold": 0.2,
                    "video_gold": 200
                },
                "3": {
                    "level": 3,
                    "exp": 100,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 2,
                    "order_refresh_min": 30,
                    "order_refresh_max": 30,
                    "worker_gold": 0.3,
                    "video_gold": 300
                },
                "4": {
                    "level": 4,
                    "exp": 200,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 2,
                    "order_refresh_min": 30,
                    "order_refresh_max": 30,
                    "worker_gold": 0.4,
                    "video_gold": 400
                },
                "5": {
                    "level": 5,
                    "exp": 300,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 2,
                    "order_refresh_min": 30,
                    "order_refresh_max": 30,
                    "worker_gold": 0.5,
                    "video_gold": 500
                },
                "6": {
                    "level": 6,
                    "exp": 400,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 3,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 0.6,
                    "video_gold": 550
                },
                "7": {
                    "level": 7,
                    "exp": 500,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 3,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 0.7,
                    "video_gold": 600
                },
                "8": {
                    "level": 8,
                    "exp": 600,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 3,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 0.8,
                    "video_gold": 650
                },
                "9": {
                    "level": 9,
                    "exp": 700,
                    "cost": 0,
                    "order_good_min": 1,
                    "order_good_max": 3,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 0.9,
                    "video_gold": 700
                },
                "10": {
                    "level": 10,
                    "exp": 800,
                    "cost": 500,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 1,
                    "video_gold": 750
                },
                "11": {
                    "level": 11,
                    "exp": 900,
                    "cost": 1000,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 1.1,
                    "video_gold": 800
                },
                "12": {
                    "level": 12,
                    "exp": 1000,
                    "cost": 1500,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 1.2,
                    "video_gold": 850
                },
                "13": {
                    "level": 13,
                    "exp": 1200,
                    "cost": 2000,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 1.3,
                    "video_gold": 900
                },
                "14": {
                    "level": 14,
                    "exp": 1400,
                    "cost": 2500,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 1.4,
                    "video_gold": 950
                },
                "15": {
                    "level": 15,
                    "exp": 1600,
                    "cost": 3000,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 120,
                    "worker_gold": 1.5,
                    "video_gold": 1000
                },
                "16": {
                    "level": 16,
                    "exp": 1800,
                    "cost": 3500,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 1.6,
                    "video_gold": 1050
                },
                "17": {
                    "level": 17,
                    "exp": 2000,
                    "cost": 4000,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 1.7,
                    "video_gold": 1100
                },
                "18": {
                    "level": 18,
                    "exp": 2200,
                    "cost": 4500,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 1.8,
                    "video_gold": 1150
                },
                "19": {
                    "level": 19,
                    "exp": 2400,
                    "cost": 5000,
                    "order_good_min": 1,
                    "order_good_max": 5,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 1.9,
                    "video_gold": 1200
                },
                "20": {
                    "level": 20,
                    "exp": 2600,
                    "cost": 5500,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2,
                    "video_gold": 1250
                },
                "21": {
                    "level": 21,
                    "exp": 2800,
                    "cost": 6000,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.1,
                    "video_gold": 1300
                },
                "22": {
                    "level": 22,
                    "exp": 3000,
                    "cost": 6500,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.2,
                    "video_gold": 1350
                },
                "23": {
                    "level": 23,
                    "exp": 3500,
                    "cost": 7000,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.3,
                    "video_gold": 1400
                },
                "24": {
                    "level": 24,
                    "exp": 4000,
                    "cost": 7500,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.4,
                    "video_gold": 1450
                },
                "25": {
                    "level": 25,
                    "exp": 4500,
                    "cost": 8000,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.5,
                    "video_gold": 1500
                },
                "26": {
                    "level": 26,
                    "exp": 5000,
                    "cost": 8500,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.6,
                    "video_gold": 1550
                },
                "27": {
                    "level": 27,
                    "exp": 5500,
                    "cost": 9000,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.7,
                    "video_gold": 1600
                },
                "28": {
                    "level": 28,
                    "exp": 6000,
                    "cost": 9500,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.8,
                    "video_gold": 1650
                },
                "29": {
                    "level": 29,
                    "exp": 6500,
                    "cost": 10000,
                    "order_good_min": 1,
                    "order_good_max": 10,
                    "order_refresh_min": 120,
                    "order_refresh_max": 300,
                    "worker_gold": 2.9,
                    "video_gold": 1700
                },
                "30": {
                    "level": 30,
                    "exp": 7000,
                    "cost": 11000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3,
                    "video_gold": 1750
                },
                "31": {
                    "level": 31,
                    "exp": 7500,
                    "cost": 12000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.1,
                    "video_gold": 1800
                },
                "32": {
                    "level": 32,
                    "exp": 8000,
                    "cost": 13000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.2,
                    "video_gold": 1850
                },
                "33": {
                    "level": 33,
                    "exp": 8500,
                    "cost": 14000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.3,
                    "video_gold": 1900
                },
                "34": {
                    "level": 34,
                    "exp": 9000,
                    "cost": 15000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.4,
                    "video_gold": 1950
                },
                "35": {
                    "level": 35,
                    "exp": 9500,
                    "cost": 16000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.5,
                    "video_gold": 2000
                },
                "36": {
                    "level": 36,
                    "exp": 10000,
                    "cost": 17000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.6,
                    "video_gold": 2050
                },
                "37": {
                    "level": 37,
                    "exp": 11000,
                    "cost": 18000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.7,
                    "video_gold": 2100
                },
                "38": {
                    "level": 38,
                    "exp": 12000,
                    "cost": 19000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.8,
                    "video_gold": 2150
                },
                "39": {
                    "level": 39,
                    "exp": 13000,
                    "cost": 20000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 3.9,
                    "video_gold": 2200
                },
                "40": {
                    "level": 40,
                    "exp": 14000,
                    "cost": 21000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4,
                    "video_gold": 2250
                },
                "41": {
                    "level": 41,
                    "exp": 15000,
                    "cost": 22000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.1,
                    "video_gold": 2300
                },
                "42": {
                    "level": 42,
                    "exp": 16000,
                    "cost": 23000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.2,
                    "video_gold": 2350
                },
                "43": {
                    "level": 43,
                    "exp": 17000,
                    "cost": 24000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.3,
                    "video_gold": 2400
                },
                "44": {
                    "level": 44,
                    "exp": 18000,
                    "cost": 25000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.4,
                    "video_gold": 2450
                },
                "45": {
                    "level": 45,
                    "exp": 19000,
                    "cost": 26000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.5,
                    "video_gold": 2500
                },
                "46": {
                    "level": 46,
                    "exp": 20000,
                    "cost": 27000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.6,
                    "video_gold": 2550
                },
                "47": {
                    "level": 47,
                    "exp": 21000,
                    "cost": 28000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.7,
                    "video_gold": 2600
                },
                "48": {
                    "level": 48,
                    "exp": 22000,
                    "cost": 29000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.8,
                    "video_gold": 2650
                },
                "49": {
                    "level": 49,
                    "exp": 23000,
                    "cost": 30000,
                    "order_good_min": 2,
                    "order_good_max": 15,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 4.9,
                    "video_gold": 2700
                },
                "50": {
                    "level": 50,
                    "exp": 24000,
                    "cost": 31000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5,
                    "video_gold": 2750
                },
                "51": {
                    "level": 51,
                    "exp": 25000,
                    "cost": 32000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.1,
                    "video_gold": 2800
                },
                "52": {
                    "level": 52,
                    "exp": 26000,
                    "cost": 33000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.2,
                    "video_gold": 2850
                },
                "53": {
                    "level": 53,
                    "exp": 27000,
                    "cost": 34000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.3,
                    "video_gold": 2900
                },
                "54": {
                    "level": 54,
                    "exp": 28000,
                    "cost": 35000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.4,
                    "video_gold": 2950
                },
                "55": {
                    "level": 55,
                    "exp": 29000,
                    "cost": 36000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.5,
                    "video_gold": 3000
                },
                "56": {
                    "level": 56,
                    "exp": 30000,
                    "cost": 37000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.6,
                    "video_gold": 3050
                },
                "57": {
                    "level": 57,
                    "exp": 31000,
                    "cost": 38000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.7,
                    "video_gold": 3100
                },
                "58": {
                    "level": 58,
                    "exp": 32000,
                    "cost": 39000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.8,
                    "video_gold": 3150
                },
                "59": {
                    "level": 59,
                    "exp": 33000,
                    "cost": 40000,
                    "order_good_min": 2,
                    "order_good_max": 20,
                    "order_refresh_min": 300,
                    "order_refresh_max": 600,
                    "worker_gold": 5.9,
                    "video_gold": 3200
                },
                "60": {
                    "level": 60,
                    "exp": 34000,
                    "cost": 41000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 5.99999999999999,
                    "video_gold": 3250
                },
                "61": {
                    "level": 61,
                    "exp": 35000,
                    "cost": 42000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.09999999999999,
                    "video_gold": 3300
                },
                "62": {
                    "level": 62,
                    "exp": 36000,
                    "cost": 43000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.19999999999999,
                    "video_gold": 3350
                },
                "63": {
                    "level": 63,
                    "exp": 37000,
                    "cost": 44000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.29999999999999,
                    "video_gold": 3400
                },
                "64": {
                    "level": 64,
                    "exp": 38000,
                    "cost": 45000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.39999999999999,
                    "video_gold": 3450
                },
                "65": {
                    "level": 65,
                    "exp": 39000,
                    "cost": 46000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.49999999999999,
                    "video_gold": 3500
                },
                "66": {
                    "level": 66,
                    "exp": 40000,
                    "cost": 47000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.59999999999999,
                    "video_gold": 3550
                },
                "67": {
                    "level": 67,
                    "exp": 41000,
                    "cost": 48000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.69999999999999,
                    "video_gold": 3600
                },
                "68": {
                    "level": 68,
                    "exp": 42000,
                    "cost": 49000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.79999999999999,
                    "video_gold": 3650
                },
                "69": {
                    "level": 69,
                    "exp": 43000,
                    "cost": 50000,
                    "order_good_min": 3,
                    "order_good_max": 20,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.89999999999999,
                    "video_gold": 3700
                },
                "70": {
                    "level": 70,
                    "exp": 44000,
                    "cost": 51000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 6.99999999999999,
                    "video_gold": 3750
                },
                "71": {
                    "level": 71,
                    "exp": 45000,
                    "cost": 52000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.09999999999999,
                    "video_gold": 3800
                },
                "72": {
                    "level": 72,
                    "exp": 46000,
                    "cost": 53000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.19999999999999,
                    "video_gold": 3850
                },
                "73": {
                    "level": 73,
                    "exp": 47000,
                    "cost": 54000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.29999999999999,
                    "video_gold": 3900
                },
                "74": {
                    "level": 74,
                    "exp": 48000,
                    "cost": 55000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.39999999999999,
                    "video_gold": 3950
                },
                "75": {
                    "level": 75,
                    "exp": 49000,
                    "cost": 56000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.49999999999999,
                    "video_gold": 4000
                },
                "76": {
                    "level": 76,
                    "exp": 50000,
                    "cost": 57000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.59999999999999,
                    "video_gold": 4050
                },
                "77": {
                    "level": 77,
                    "exp": 51000,
                    "cost": 58000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.69999999999999,
                    "video_gold": 4100
                },
                "78": {
                    "level": 78,
                    "exp": 52000,
                    "cost": 59000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.79999999999999,
                    "video_gold": 4150
                },
                "79": {
                    "level": 79,
                    "exp": 53000,
                    "cost": 60000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.89999999999999,
                    "video_gold": 4200
                },
                "80": {
                    "level": 80,
                    "exp": 54000,
                    "cost": 61000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 7.99999999999999,
                    "video_gold": 4250
                },
                "81": {
                    "level": 81,
                    "exp": 55000,
                    "cost": 62000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.09999999999999,
                    "video_gold": 4300
                },
                "82": {
                    "level": 82,
                    "exp": 56000,
                    "cost": 63000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.19999999999999,
                    "video_gold": 4350
                },
                "83": {
                    "level": 83,
                    "exp": 57000,
                    "cost": 64000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.29999999999999,
                    "video_gold": 4400
                },
                "84": {
                    "level": 84,
                    "exp": 58000,
                    "cost": 65000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.39999999999999,
                    "video_gold": 4450
                },
                "85": {
                    "level": 85,
                    "exp": 59000,
                    "cost": 66000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.49999999999999,
                    "video_gold": 4500
                },
                "86": {
                    "level": 86,
                    "exp": 60000,
                    "cost": 67000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.59999999999999,
                    "video_gold": 4550
                },
                "87": {
                    "level": 87,
                    "exp": 61000,
                    "cost": 68000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.69999999999999,
                    "video_gold": 4600
                },
                "88": {
                    "level": 88,
                    "exp": 62000,
                    "cost": 69000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.79999999999998,
                    "video_gold": 4650
                },
                "89": {
                    "level": 89,
                    "exp": 63000,
                    "cost": 70000,
                    "order_good_min": 3,
                    "order_good_max": 25,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.89999999999998,
                    "video_gold": 4700
                },
                "90": {
                    "level": 90,
                    "exp": 64000,
                    "cost": 71000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 8.99999999999998,
                    "video_gold": 4750
                },
                "91": {
                    "level": 91,
                    "exp": 65000,
                    "cost": 72000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.09999999999998,
                    "video_gold": 4800
                },
                "92": {
                    "level": 92,
                    "exp": 66000,
                    "cost": 73000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.19999999999998,
                    "video_gold": 4850
                },
                "93": {
                    "level": 93,
                    "exp": 67000,
                    "cost": 74000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.29999999999998,
                    "video_gold": 4900
                },
                "94": {
                    "level": 94,
                    "exp": 68000,
                    "cost": 75000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.39999999999998,
                    "video_gold": 4950
                },
                "95": {
                    "level": 95,
                    "exp": 69000,
                    "cost": 76000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.49999999999998,
                    "video_gold": 5000
                },
                "96": {
                    "level": 96,
                    "exp": 70000,
                    "cost": 77000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.59999999999998,
                    "video_gold": 5050
                },
                "97": {
                    "level": 97,
                    "exp": 71000,
                    "cost": 78000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.69999999999998,
                    "video_gold": 5100
                },
                "98": {
                    "level": 98,
                    "exp": 72000,
                    "cost": 79000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.79999999999998,
                    "video_gold": 5150
                },
                "99": {
                    "level": 99,
                    "exp": 73000,
                    "cost": 80000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.89999999999998,
                    "video_gold": 5200
                },
                "100": {
                    "level": 100,
                    "exp": 74000,
                    "cost": 81000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 9.99999999999998,
                    "video_gold": 5250
                },
                "101": {
                    "level": 101,
                    "exp": 75000,
                    "cost": 82000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.05,
                    "video_gold": 5300
                },
                "102": {
                    "level": 102,
                    "exp": 76000,
                    "cost": 83000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.1,
                    "video_gold": 5350
                },
                "103": {
                    "level": 103,
                    "exp": 77000,
                    "cost": 84000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.15,
                    "video_gold": 5400
                },
                "104": {
                    "level": 104,
                    "exp": 78000,
                    "cost": 85000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.2,
                    "video_gold": 5450
                },
                "105": {
                    "level": 105,
                    "exp": 79000,
                    "cost": 86000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.25,
                    "video_gold": 5500
                },
                "106": {
                    "level": 106,
                    "exp": 80000,
                    "cost": 87000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.3,
                    "video_gold": 5550
                },
                "107": {
                    "level": 107,
                    "exp": 81000,
                    "cost": 88000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.35,
                    "video_gold": 5600
                },
                "108": {
                    "level": 108,
                    "exp": 82000,
                    "cost": 89000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.4,
                    "video_gold": 5650
                },
                "109": {
                    "level": 109,
                    "exp": 83000,
                    "cost": 90000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.45,
                    "video_gold": 5700
                },
                "110": {
                    "level": 110,
                    "exp": 84000,
                    "cost": 91000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.5,
                    "video_gold": 5750
                },
                "111": {
                    "level": 111,
                    "exp": 85000,
                    "cost": 92000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.55,
                    "video_gold": 5800
                },
                "112": {
                    "level": 112,
                    "exp": 86000,
                    "cost": 93000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.6,
                    "video_gold": 5850
                },
                "113": {
                    "level": 113,
                    "exp": 87000,
                    "cost": 94000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.65,
                    "video_gold": 5900
                },
                "114": {
                    "level": 114,
                    "exp": 88000,
                    "cost": 95000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.7,
                    "video_gold": 5950
                },
                "115": {
                    "level": 115,
                    "exp": 89000,
                    "cost": 96000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.75,
                    "video_gold": 6000
                },
                "116": {
                    "level": 116,
                    "exp": 90000,
                    "cost": 97000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.8,
                    "video_gold": 6050
                },
                "117": {
                    "level": 117,
                    "exp": 91000,
                    "cost": 98000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.85,
                    "video_gold": 6100
                },
                "118": {
                    "level": 118,
                    "exp": 92000,
                    "cost": 99000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.9,
                    "video_gold": 6150
                },
                "119": {
                    "level": 119,
                    "exp": 93000,
                    "cost": 100000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 10.95,
                    "video_gold": 6200
                },
                "120": {
                    "level": 120,
                    "exp": 94000,
                    "cost": 102000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11,
                    "video_gold": 6250
                },
                "121": {
                    "level": 121,
                    "exp": 95000,
                    "cost": 104000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.05,
                    "video_gold": 6300
                },
                "122": {
                    "level": 122,
                    "exp": 96000,
                    "cost": 106000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.1,
                    "video_gold": 6350
                },
                "123": {
                    "level": 123,
                    "exp": 97000,
                    "cost": 108000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.15,
                    "video_gold": 6400
                },
                "124": {
                    "level": 124,
                    "exp": 98000,
                    "cost": 110000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.2,
                    "video_gold": 6450
                },
                "125": {
                    "level": 125,
                    "exp": 99000,
                    "cost": 112000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.25,
                    "video_gold": 6500
                },
                "126": {
                    "level": 126,
                    "exp": 100000,
                    "cost": 114000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.3,
                    "video_gold": 6550
                },
                "127": {
                    "level": 127,
                    "exp": 101000,
                    "cost": 116000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.35,
                    "video_gold": 6600
                },
                "128": {
                    "level": 128,
                    "exp": 102000,
                    "cost": 118000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.4,
                    "video_gold": 6650
                },
                "129": {
                    "level": 129,
                    "exp": 103000,
                    "cost": 120000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.45,
                    "video_gold": 6700
                },
                "130": {
                    "level": 130,
                    "exp": 104000,
                    "cost": 122000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.5,
                    "video_gold": 6750
                },
                "131": {
                    "level": 131,
                    "exp": 105000,
                    "cost": 124000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.55,
                    "video_gold": 6800
                },
                "132": {
                    "level": 132,
                    "exp": 106000,
                    "cost": 126000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.6,
                    "video_gold": 6850
                },
                "133": {
                    "level": 133,
                    "exp": 107000,
                    "cost": 128000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.65,
                    "video_gold": 6900
                },
                "134": {
                    "level": 134,
                    "exp": 108000,
                    "cost": 130000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.7,
                    "video_gold": 6950
                },
                "135": {
                    "level": 135,
                    "exp": 109000,
                    "cost": 132000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.75,
                    "video_gold": 7000
                },
                "136": {
                    "level": 136,
                    "exp": 110000,
                    "cost": 134000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.8,
                    "video_gold": 7050
                },
                "137": {
                    "level": 137,
                    "exp": 111000,
                    "cost": 136000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.85,
                    "video_gold": 7100
                },
                "138": {
                    "level": 138,
                    "exp": 112000,
                    "cost": 138000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.9,
                    "video_gold": 7150
                },
                "139": {
                    "level": 139,
                    "exp": 113000,
                    "cost": 140000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 11.95,
                    "video_gold": 7200
                },
                "140": {
                    "level": 140,
                    "exp": 114000,
                    "cost": 142000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12,
                    "video_gold": 7250
                },
                "141": {
                    "level": 141,
                    "exp": 115000,
                    "cost": 144000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.05,
                    "video_gold": 7300
                },
                "142": {
                    "level": 142,
                    "exp": 116000,
                    "cost": 146000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.1,
                    "video_gold": 7350
                },
                "143": {
                    "level": 143,
                    "exp": 117000,
                    "cost": 148000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.15,
                    "video_gold": 7400
                },
                "144": {
                    "level": 144,
                    "exp": 118000,
                    "cost": 150000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.2,
                    "video_gold": 7450
                },
                "145": {
                    "level": 145,
                    "exp": 119000,
                    "cost": 152000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.25,
                    "video_gold": 7500
                },
                "146": {
                    "level": 146,
                    "exp": 120000,
                    "cost": 154000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.3,
                    "video_gold": 7550
                },
                "147": {
                    "level": 147,
                    "exp": 121000,
                    "cost": 156000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.35,
                    "video_gold": 7600
                },
                "148": {
                    "level": 148,
                    "exp": 122000,
                    "cost": 158000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.4,
                    "video_gold": 7650
                },
                "149": {
                    "level": 149,
                    "exp": 123000,
                    "cost": 160000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.45,
                    "video_gold": 7700
                },
                "150": {
                    "level": 150,
                    "exp": 124000,
                    "cost": 162000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.5,
                    "video_gold": 7750
                },
                "151": {
                    "level": 151,
                    "exp": 125000,
                    "cost": 164000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.55,
                    "video_gold": 7800
                },
                "152": {
                    "level": 152,
                    "exp": 126000,
                    "cost": 166000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.6,
                    "video_gold": 7850
                },
                "153": {
                    "level": 153,
                    "exp": 127000,
                    "cost": 168000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.65,
                    "video_gold": 7900
                },
                "154": {
                    "level": 154,
                    "exp": 128000,
                    "cost": 170000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.7,
                    "video_gold": 7950
                },
                "155": {
                    "level": 155,
                    "exp": 129000,
                    "cost": 172000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.75,
                    "video_gold": 8000
                },
                "156": {
                    "level": 156,
                    "exp": 130000,
                    "cost": 174000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.8,
                    "video_gold": 8050
                },
                "157": {
                    "level": 157,
                    "exp": 131000,
                    "cost": 176000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.85,
                    "video_gold": 8100
                },
                "158": {
                    "level": 158,
                    "exp": 132000,
                    "cost": 178000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.9,
                    "video_gold": 8150
                },
                "159": {
                    "level": 159,
                    "exp": 133000,
                    "cost": 180000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 12.95,
                    "video_gold": 8200
                },
                "160": {
                    "level": 160,
                    "exp": 134000,
                    "cost": 182000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13,
                    "video_gold": 8250
                },
                "161": {
                    "level": 161,
                    "exp": 135000,
                    "cost": 184000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.05,
                    "video_gold": 8300
                },
                "162": {
                    "level": 162,
                    "exp": 136000,
                    "cost": 186000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.1,
                    "video_gold": 8350
                },
                "163": {
                    "level": 163,
                    "exp": 137000,
                    "cost": 188000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.15,
                    "video_gold": 8400
                },
                "164": {
                    "level": 164,
                    "exp": 138000,
                    "cost": 190000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.2,
                    "video_gold": 8450
                },
                "165": {
                    "level": 165,
                    "exp": 139000,
                    "cost": 192000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.25,
                    "video_gold": 8500
                },
                "166": {
                    "level": 166,
                    "exp": 140000,
                    "cost": 194000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.3,
                    "video_gold": 8550
                },
                "167": {
                    "level": 167,
                    "exp": 141000,
                    "cost": 196000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.35,
                    "video_gold": 8600
                },
                "168": {
                    "level": 168,
                    "exp": 142000,
                    "cost": 198000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.4,
                    "video_gold": 8650
                },
                "169": {
                    "level": 169,
                    "exp": 143000,
                    "cost": 200000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.45,
                    "video_gold": 8700
                },
                "170": {
                    "level": 170,
                    "exp": 144000,
                    "cost": 202000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.5,
                    "video_gold": 8750
                },
                "171": {
                    "level": 171,
                    "exp": 145000,
                    "cost": 204000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.55,
                    "video_gold": 8800
                },
                "172": {
                    "level": 172,
                    "exp": 146000,
                    "cost": 206000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.6,
                    "video_gold": 8850
                },
                "173": {
                    "level": 173,
                    "exp": 147000,
                    "cost": 208000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.65,
                    "video_gold": 8900
                },
                "174": {
                    "level": 174,
                    "exp": 148000,
                    "cost": 210000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.7,
                    "video_gold": 8950
                },
                "175": {
                    "level": 175,
                    "exp": 149000,
                    "cost": 212000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.75,
                    "video_gold": 9000
                },
                "176": {
                    "level": 176,
                    "exp": 150000,
                    "cost": 214000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.8,
                    "video_gold": 9050
                },
                "177": {
                    "level": 177,
                    "exp": 151000,
                    "cost": 216000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.85,
                    "video_gold": 9100
                },
                "178": {
                    "level": 178,
                    "exp": 152000,
                    "cost": 218000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.9,
                    "video_gold": 9150
                },
                "179": {
                    "level": 179,
                    "exp": 153000,
                    "cost": 220000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 13.95,
                    "video_gold": 9200
                },
                "180": {
                    "level": 180,
                    "exp": 154000,
                    "cost": 222000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14,
                    "video_gold": 9250
                },
                "181": {
                    "level": 181,
                    "exp": 155000,
                    "cost": 224000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.05,
                    "video_gold": 9300
                },
                "182": {
                    "level": 182,
                    "exp": 156000,
                    "cost": 226000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.1,
                    "video_gold": 9350
                },
                "183": {
                    "level": 183,
                    "exp": 157000,
                    "cost": 228000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.15,
                    "video_gold": 9400
                },
                "184": {
                    "level": 184,
                    "exp": 158000,
                    "cost": 230000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.2,
                    "video_gold": 9450
                },
                "185": {
                    "level": 185,
                    "exp": 159000,
                    "cost": 232000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.25,
                    "video_gold": 9500
                },
                "186": {
                    "level": 186,
                    "exp": 160000,
                    "cost": 234000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.3,
                    "video_gold": 9550
                },
                "187": {
                    "level": 187,
                    "exp": 161000,
                    "cost": 236000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.35,
                    "video_gold": 9600
                },
                "188": {
                    "level": 188,
                    "exp": 162000,
                    "cost": 238000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.4,
                    "video_gold": 9650
                },
                "189": {
                    "level": 189,
                    "exp": 163000,
                    "cost": 240000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.45,
                    "video_gold": 9700
                },
                "190": {
                    "level": 190,
                    "exp": 164000,
                    "cost": 242000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.5,
                    "video_gold": 9750
                },
                "191": {
                    "level": 191,
                    "exp": 165000,
                    "cost": 244000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.55,
                    "video_gold": 9800
                },
                "192": {
                    "level": 192,
                    "exp": 166000,
                    "cost": 246000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.6,
                    "video_gold": 9850
                },
                "193": {
                    "level": 193,
                    "exp": 167000,
                    "cost": 248000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.65,
                    "video_gold": 9900
                },
                "194": {
                    "level": 194,
                    "exp": 168000,
                    "cost": 250000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.7,
                    "video_gold": 9950
                },
                "195": {
                    "level": 195,
                    "exp": 169000,
                    "cost": 252000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.75,
                    "video_gold": 10000
                },
                "196": {
                    "level": 196,
                    "exp": 170000,
                    "cost": 254000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.8,
                    "video_gold": 10050
                },
                "197": {
                    "level": 197,
                    "exp": 171000,
                    "cost": 256000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.85,
                    "video_gold": 10100
                },
                "198": {
                    "level": 198,
                    "exp": 172000,
                    "cost": 258000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.9000000000001,
                    "video_gold": 10150
                },
                "199": {
                    "level": 199,
                    "exp": 173000,
                    "cost": 260000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 14.9500000000001,
                    "video_gold": 10200
                },
                "200": {
                    "level": 200,
                    "exp": 174000,
                    "cost": 262000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.0000000000001,
                    "video_gold": 10250
                },
                "201": {
                    "level": 201,
                    "exp": 175000,
                    "cost": 264000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.0500000000001,
                    "video_gold": 10300
                },
                "202": {
                    "level": 202,
                    "exp": 176000,
                    "cost": 266000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.1000000000001,
                    "video_gold": 10350
                },
                "203": {
                    "level": 203,
                    "exp": 177000,
                    "cost": 268000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.1500000000001,
                    "video_gold": 10400
                },
                "204": {
                    "level": 204,
                    "exp": 178000,
                    "cost": 270000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.2000000000001,
                    "video_gold": 10450
                },
                "205": {
                    "level": 205,
                    "exp": 179000,
                    "cost": 272000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.2500000000001,
                    "video_gold": 10500
                },
                "206": {
                    "level": 206,
                    "exp": 180000,
                    "cost": 274000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.3000000000001,
                    "video_gold": 10550
                },
                "207": {
                    "level": 207,
                    "exp": 181000,
                    "cost": 276000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.3500000000001,
                    "video_gold": 10600
                },
                "208": {
                    "level": 208,
                    "exp": 182000,
                    "cost": 278000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.4000000000001,
                    "video_gold": 10650
                },
                "209": {
                    "level": 209,
                    "exp": 183000,
                    "cost": 280000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.4500000000001,
                    "video_gold": 10700
                },
                "210": {
                    "level": 210,
                    "exp": 184000,
                    "cost": 282000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.5000000000001,
                    "video_gold": 10750
                },
                "211": {
                    "level": 211,
                    "exp": 185000,
                    "cost": 284000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.5500000000001,
                    "video_gold": 10800
                },
                "212": {
                    "level": 212,
                    "exp": 186000,
                    "cost": 286000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.6000000000001,
                    "video_gold": 10850
                },
                "213": {
                    "level": 213,
                    "exp": 187000,
                    "cost": 288000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.6500000000001,
                    "video_gold": 10900
                },
                "214": {
                    "level": 214,
                    "exp": 188000,
                    "cost": 290000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.7000000000001,
                    "video_gold": 10950
                },
                "215": {
                    "level": 215,
                    "exp": 189000,
                    "cost": 292000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.7500000000001,
                    "video_gold": 11000
                },
                "216": {
                    "level": 216,
                    "exp": 190000,
                    "cost": 294000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.8000000000001,
                    "video_gold": 11050
                },
                "217": {
                    "level": 217,
                    "exp": 191000,
                    "cost": 296000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.8500000000001,
                    "video_gold": 11100
                },
                "218": {
                    "level": 218,
                    "exp": 192000,
                    "cost": 298000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.9000000000001,
                    "video_gold": 11150
                },
                "219": {
                    "level": 219,
                    "exp": 193000,
                    "cost": 300000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 15.9500000000001,
                    "video_gold": 11200
                },
                "220": {
                    "level": 220,
                    "exp": 194000,
                    "cost": 305000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.0000000000001,
                    "video_gold": 11250
                },
                "221": {
                    "level": 221,
                    "exp": 195000,
                    "cost": 310000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.0500000000001,
                    "video_gold": 11300
                },
                "222": {
                    "level": 222,
                    "exp": 196000,
                    "cost": 315000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.1000000000001,
                    "video_gold": 11350
                },
                "223": {
                    "level": 223,
                    "exp": 197000,
                    "cost": 320000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.1500000000001,
                    "video_gold": 11400
                },
                "224": {
                    "level": 224,
                    "exp": 198000,
                    "cost": 325000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.2000000000001,
                    "video_gold": 11450
                },
                "225": {
                    "level": 225,
                    "exp": 199000,
                    "cost": 330000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.2500000000001,
                    "video_gold": 11500
                },
                "226": {
                    "level": 226,
                    "exp": 200000,
                    "cost": 335000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.3000000000001,
                    "video_gold": 11550
                },
                "227": {
                    "level": 227,
                    "exp": 201000,
                    "cost": 340000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.3500000000001,
                    "video_gold": 11600
                },
                "228": {
                    "level": 228,
                    "exp": 202000,
                    "cost": 345000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.4000000000001,
                    "video_gold": 11650
                },
                "229": {
                    "level": 229,
                    "exp": 203000,
                    "cost": 350000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.4500000000001,
                    "video_gold": 11700
                },
                "230": {
                    "level": 230,
                    "exp": 204000,
                    "cost": 355000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.5000000000001,
                    "video_gold": 11750
                },
                "231": {
                    "level": 231,
                    "exp": 205000,
                    "cost": 360000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.5500000000001,
                    "video_gold": 11800
                },
                "232": {
                    "level": 232,
                    "exp": 206000,
                    "cost": 365000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.6000000000001,
                    "video_gold": 11850
                },
                "233": {
                    "level": 233,
                    "exp": 207000,
                    "cost": 370000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.6500000000001,
                    "video_gold": 11900
                },
                "234": {
                    "level": 234,
                    "exp": 208000,
                    "cost": 375000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.7000000000001,
                    "video_gold": 11950
                },
                "235": {
                    "level": 235,
                    "exp": 209000,
                    "cost": 380000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.7500000000001,
                    "video_gold": 12000
                },
                "236": {
                    "level": 236,
                    "exp": 210000,
                    "cost": 385000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.8000000000001,
                    "video_gold": 12050
                },
                "237": {
                    "level": 237,
                    "exp": 211000,
                    "cost": 390000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.8500000000001,
                    "video_gold": 12100
                },
                "238": {
                    "level": 238,
                    "exp": 212000,
                    "cost": 395000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.9000000000001,
                    "video_gold": 12150
                },
                "239": {
                    "level": 239,
                    "exp": 213000,
                    "cost": 400000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 16.9500000000001,
                    "video_gold": 12200
                },
                "240": {
                    "level": 240,
                    "exp": 214000,
                    "cost": 405000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.0000000000001,
                    "video_gold": 12250
                },
                "241": {
                    "level": 241,
                    "exp": 215000,
                    "cost": 410000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.0500000000001,
                    "video_gold": 12300
                },
                "242": {
                    "level": 242,
                    "exp": 216000,
                    "cost": 415000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.1000000000001,
                    "video_gold": 12350
                },
                "243": {
                    "level": 243,
                    "exp": 217000,
                    "cost": 420000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.1500000000001,
                    "video_gold": 12400
                },
                "244": {
                    "level": 244,
                    "exp": 218000,
                    "cost": 425000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.2000000000001,
                    "video_gold": 12450
                },
                "245": {
                    "level": 245,
                    "exp": 219000,
                    "cost": 430000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.2500000000001,
                    "video_gold": 12500
                },
                "246": {
                    "level": 246,
                    "exp": 220000,
                    "cost": 435000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.3000000000001,
                    "video_gold": 12550
                },
                "247": {
                    "level": 247,
                    "exp": 221000,
                    "cost": 440000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.3500000000001,
                    "video_gold": 12600
                },
                "248": {
                    "level": 248,
                    "exp": 222000,
                    "cost": 445000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.4000000000001,
                    "video_gold": 12650
                },
                "249": {
                    "level": 249,
                    "exp": 223000,
                    "cost": 450000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.4500000000001,
                    "video_gold": 12700
                },
                "250": {
                    "level": 250,
                    "exp": 224000,
                    "cost": 455000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.5000000000001,
                    "video_gold": 12750
                },
                "251": {
                    "level": 251,
                    "exp": 225000,
                    "cost": 460000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.5500000000001,
                    "video_gold": 12800
                },
                "252": {
                    "level": 252,
                    "exp": 226000,
                    "cost": 465000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.6000000000001,
                    "video_gold": 12850
                },
                "253": {
                    "level": 253,
                    "exp": 227000,
                    "cost": 470000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.6500000000001,
                    "video_gold": 12900
                },
                "254": {
                    "level": 254,
                    "exp": 228000,
                    "cost": 475000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.7000000000001,
                    "video_gold": 12950
                },
                "255": {
                    "level": 255,
                    "exp": 229000,
                    "cost": 480000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.7500000000001,
                    "video_gold": 13000
                },
                "256": {
                    "level": 256,
                    "exp": 230000,
                    "cost": 485000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.8000000000001,
                    "video_gold": 13050
                },
                "257": {
                    "level": 257,
                    "exp": 231000,
                    "cost": 490000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.8500000000001,
                    "video_gold": 13100
                },
                "258": {
                    "level": 258,
                    "exp": 232000,
                    "cost": 495000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.9000000000001,
                    "video_gold": 13150
                },
                "259": {
                    "level": 259,
                    "exp": 233000,
                    "cost": 500000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 17.9500000000001,
                    "video_gold": 13200
                },
                "260": {
                    "level": 260,
                    "exp": 234000,
                    "cost": 505000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.0000000000001,
                    "video_gold": 13250
                },
                "261": {
                    "level": 261,
                    "exp": 235000,
                    "cost": 510000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.0500000000001,
                    "video_gold": 13300
                },
                "262": {
                    "level": 262,
                    "exp": 236000,
                    "cost": 515000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.1000000000001,
                    "video_gold": 13350
                },
                "263": {
                    "level": 263,
                    "exp": 237000,
                    "cost": 520000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.1500000000001,
                    "video_gold": 13400
                },
                "264": {
                    "level": 264,
                    "exp": 238000,
                    "cost": 525000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.2000000000001,
                    "video_gold": 13450
                },
                "265": {
                    "level": 265,
                    "exp": 239000,
                    "cost": 530000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.2500000000001,
                    "video_gold": 13500
                },
                "266": {
                    "level": 266,
                    "exp": 240000,
                    "cost": 535000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.3000000000001,
                    "video_gold": 13550
                },
                "267": {
                    "level": 267,
                    "exp": 241000,
                    "cost": 540000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.3500000000001,
                    "video_gold": 13600
                },
                "268": {
                    "level": 268,
                    "exp": 242000,
                    "cost": 545000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.4000000000001,
                    "video_gold": 13650
                },
                "269": {
                    "level": 269,
                    "exp": 243000,
                    "cost": 550000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.4500000000001,
                    "video_gold": 13700
                },
                "270": {
                    "level": 270,
                    "exp": 244000,
                    "cost": 555000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.5000000000001,
                    "video_gold": 13750
                },
                "271": {
                    "level": 271,
                    "exp": 245000,
                    "cost": 560000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.5500000000001,
                    "video_gold": 13800
                },
                "272": {
                    "level": 272,
                    "exp": 246000,
                    "cost": 565000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.6000000000001,
                    "video_gold": 13850
                },
                "273": {
                    "level": 273,
                    "exp": 247000,
                    "cost": 570000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.6500000000001,
                    "video_gold": 13900
                },
                "274": {
                    "level": 274,
                    "exp": 248000,
                    "cost": 575000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.7000000000001,
                    "video_gold": 13950
                },
                "275": {
                    "level": 275,
                    "exp": 249000,
                    "cost": 580000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.7500000000001,
                    "video_gold": 14000
                },
                "276": {
                    "level": 276,
                    "exp": 250000,
                    "cost": 585000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.8000000000001,
                    "video_gold": 14050
                },
                "277": {
                    "level": 277,
                    "exp": 251000,
                    "cost": 590000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.8500000000001,
                    "video_gold": 14100
                },
                "278": {
                    "level": 278,
                    "exp": 252000,
                    "cost": 595000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.9000000000001,
                    "video_gold": 14150
                },
                "279": {
                    "level": 279,
                    "exp": 253000,
                    "cost": 600000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 18.9500000000001,
                    "video_gold": 14200
                },
                "280": {
                    "level": 280,
                    "exp": 254000,
                    "cost": 605000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.0000000000001,
                    "video_gold": 14250
                },
                "281": {
                    "level": 281,
                    "exp": 255000,
                    "cost": 610000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.0500000000001,
                    "video_gold": 14300
                },
                "282": {
                    "level": 282,
                    "exp": 256000,
                    "cost": 615000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.1000000000001,
                    "video_gold": 14350
                },
                "283": {
                    "level": 283,
                    "exp": 257000,
                    "cost": 620000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.1500000000001,
                    "video_gold": 14400
                },
                "284": {
                    "level": 284,
                    "exp": 258000,
                    "cost": 625000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.2000000000001,
                    "video_gold": 14450
                },
                "285": {
                    "level": 285,
                    "exp": 259000,
                    "cost": 630000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.2500000000001,
                    "video_gold": 14500
                },
                "286": {
                    "level": 286,
                    "exp": 260000,
                    "cost": 635000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.3000000000001,
                    "video_gold": 14550
                },
                "287": {
                    "level": 287,
                    "exp": 261000,
                    "cost": 640000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.3500000000001,
                    "video_gold": 14600
                },
                "288": {
                    "level": 288,
                    "exp": 262000,
                    "cost": 645000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.4000000000001,
                    "video_gold": 14650
                },
                "289": {
                    "level": 289,
                    "exp": 263000,
                    "cost": 650000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.4500000000001,
                    "video_gold": 14700
                },
                "290": {
                    "level": 290,
                    "exp": 264000,
                    "cost": 655000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.5000000000001,
                    "video_gold": 14750
                },
                "291": {
                    "level": 291,
                    "exp": 265000,
                    "cost": 660000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.5500000000001,
                    "video_gold": 14800
                },
                "292": {
                    "level": 292,
                    "exp": 266000,
                    "cost": 665000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.6000000000001,
                    "video_gold": 14850
                },
                "293": {
                    "level": 293,
                    "exp": 267000,
                    "cost": 670000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.6500000000001,
                    "video_gold": 14900
                },
                "294": {
                    "level": 294,
                    "exp": 268000,
                    "cost": 675000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.7000000000001,
                    "video_gold": 14950
                },
                "295": {
                    "level": 295,
                    "exp": 269000,
                    "cost": 680000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.7500000000001,
                    "video_gold": 15000
                },
                "296": {
                    "level": 296,
                    "exp": 270000,
                    "cost": 685000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.8000000000001,
                    "video_gold": 15050
                },
                "297": {
                    "level": 297,
                    "exp": 271000,
                    "cost": 690000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.8500000000001,
                    "video_gold": 15100
                },
                "298": {
                    "level": 298,
                    "exp": 272000,
                    "cost": 695000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.9000000000001,
                    "video_gold": 15150
                },
                "299": {
                    "level": 299,
                    "exp": 273000,
                    "cost": 700000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 19.9500000000001,
                    "video_gold": 15200
                },
                "300": {
                    "level": 300,
                    "exp": 274000,
                    "cost": 705000,
                    "order_good_min": 3,
                    "order_good_max": 30,
                    "order_refresh_min": 600,
                    "order_refresh_max": 900,
                    "worker_gold": 20.0000000000001,
                    "video_gold": 15250
                }
            },
            "guildLevel": {
                "1": {
                    "level": 1,
                    "exp": 20,
                    "member_max": 10,
                    "admin_max": 3,
                    "sign_gold": 100
                },
                "2": {
                    "level": 2,
                    "exp": 24,
                    "member_max": 12,
                    "admin_max": 3,
                    "sign_gold": 200
                },
                "3": {
                    "level": 3,
                    "exp": 28,
                    "member_max": 14,
                    "admin_max": 3,
                    "sign_gold": 300
                },
                "4": {
                    "level": 4,
                    "exp": 32,
                    "member_max": 16,
                    "admin_max": 3,
                    "sign_gold": 400
                },
                "5": {
                    "level": 5,
                    "exp": 36,
                    "member_max": 18,
                    "admin_max": 3,
                    "sign_gold": 500
                },
                "6": {
                    "level": 6,
                    "exp": 40,
                    "member_max": 20,
                    "admin_max": 4,
                    "sign_gold": 600
                },
                "7": {
                    "level": 7,
                    "exp": 110,
                    "member_max": 22,
                    "admin_max": 4,
                    "sign_gold": 700
                },
                "8": {
                    "level": 8,
                    "exp": 120,
                    "member_max": 24,
                    "admin_max": 4,
                    "sign_gold": 800
                },
                "9": {
                    "level": 9,
                    "exp": 130,
                    "member_max": 26,
                    "admin_max": 4,
                    "sign_gold": 900
                },
                "10": {
                    "level": 10,
                    "exp": 140,
                    "member_max": 28,
                    "admin_max": 4,
                    "sign_gold": 1000
                },
                "11": {
                    "level": 11,
                    "exp": 150,
                    "member_max": 30,
                    "admin_max": 5,
                    "sign_gold": 1100
                },
                "12": {
                    "level": 12,
                    "exp": 160,
                    "member_max": 32,
                    "admin_max": 5,
                    "sign_gold": 1200
                },
                "13": {
                    "level": 13,
                    "exp": 170,
                    "member_max": 34,
                    "admin_max": 5,
                    "sign_gold": 1300
                },
                "14": {
                    "level": 14,
                    "exp": 180,
                    "member_max": 36,
                    "admin_max": 5,
                    "sign_gold": 1400
                },
                "15": {
                    "level": 15,
                    "exp": 190,
                    "member_max": 38,
                    "admin_max": 5,
                    "sign_gold": 1500
                },
                "16": {
                    "level": 16,
                    "exp": 200,
                    "member_max": 40,
                    "admin_max": 6,
                    "sign_gold": 1600
                },
                "17": {
                    "level": 17,
                    "exp": 210,
                    "member_max": 42,
                    "admin_max": 6,
                    "sign_gold": 1700
                },
                "18": {
                    "level": 18,
                    "exp": 220,
                    "member_max": 44,
                    "admin_max": 6,
                    "sign_gold": 1800
                },
                "19": {
                    "level": 19,
                    "exp": 230,
                    "member_max": 46,
                    "admin_max": 6,
                    "sign_gold": 1900
                },
                "20": {
                    "level": 20,
                    "exp": 240,
                    "member_max": 48,
                    "admin_max": 6,
                    "sign_gold": 2000
                },
                "21": {
                    "level": 21,
                    "exp": 250,
                    "member_max": 50,
                    "admin_max": 7,
                    "sign_gold": 2100
                },
                "22": {
                    "level": 22,
                    "exp": 260,
                    "member_max": 52,
                    "admin_max": 7,
                    "sign_gold": 2200
                },
                "23": {
                    "level": 23,
                    "exp": 270,
                    "member_max": 54,
                    "admin_max": 7,
                    "sign_gold": 2300
                },
                "24": {
                    "level": 24,
                    "exp": 280,
                    "member_max": 56,
                    "admin_max": 7,
                    "sign_gold": 2400
                },
                "25": {
                    "level": 25,
                    "exp": 290,
                    "member_max": 58,
                    "admin_max": 7,
                    "sign_gold": 2500
                },
                "26": {
                    "level": 26,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 2600
                },
                "27": {
                    "level": 27,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 2700
                },
                "28": {
                    "level": 28,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 2800
                },
                "29": {
                    "level": 29,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 2900
                },
                "30": {
                    "level": 30,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3000
                },
                "31": {
                    "level": 31,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3100
                },
                "32": {
                    "level": 32,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3200
                },
                "33": {
                    "level": 33,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3300
                },
                "34": {
                    "level": 34,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3400
                },
                "35": {
                    "level": 35,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3500
                },
                "36": {
                    "level": 36,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3600
                },
                "37": {
                    "level": 37,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3700
                },
                "38": {
                    "level": 38,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3800
                },
                "39": {
                    "level": 39,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 3900
                },
                "40": {
                    "level": 40,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4000
                },
                "41": {
                    "level": 41,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4100
                },
                "42": {
                    "level": 42,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4200
                },
                "43": {
                    "level": 43,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4300
                },
                "44": {
                    "level": 44,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4400
                },
                "45": {
                    "level": 45,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4500
                },
                "46": {
                    "level": 46,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4600
                },
                "47": {
                    "level": 47,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4700
                },
                "48": {
                    "level": 48,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4800
                },
                "49": {
                    "level": 49,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 4900
                },
                "50": {
                    "level": 50,
                    "exp": 300,
                    "member_max": 60,
                    "admin_max": 8,
                    "sign_gold": 5000
                }
            },
            "helperLevel": {
                "1": {
                    "level": 1,
                    "video": 1,
                    "offline_gold": 1
                },
                "2": {
                    "level": 2,
                    "video": 2,
                    "offline_gold": 2
                },
                "3": {
                    "level": 3,
                    "video": 3,
                    "offline_gold": 3
                },
                "4": {
                    "level": 4,
                    "video": 4,
                    "offline_gold": 4
                },
                "5": {
                    "level": 5,
                    "video": 5,
                    "offline_gold": 5
                },
                "6": {
                    "level": 6,
                    "video": 6,
                    "offline_gold": 6
                },
                "7": {
                    "level": 7,
                    "video": 7,
                    "offline_gold": 7
                },
                "8": {
                    "level": 8,
                    "video": 8,
                    "offline_gold": 8
                },
                "9": {
                    "level": 9,
                    "video": 9,
                    "offline_gold": 9
                },
                "10": {
                    "level": 10,
                    "video": 10,
                    "offline_gold": 10
                },
                "11": {
                    "level": 11,
                    "video": 10,
                    "offline_gold": 10.5
                },
                "12": {
                    "level": 12,
                    "video": 10,
                    "offline_gold": 11
                },
                "13": {
                    "level": 13,
                    "video": 10,
                    "offline_gold": 11.5
                },
                "14": {
                    "level": 14,
                    "video": 10,
                    "offline_gold": 12
                },
                "15": {
                    "level": 15,
                    "video": 10,
                    "offline_gold": 12.5
                },
                "16": {
                    "level": 16,
                    "video": 10,
                    "offline_gold": 13
                },
                "17": {
                    "level": 17,
                    "video": 10,
                    "offline_gold": 13.5
                },
                "18": {
                    "level": 18,
                    "video": 10,
                    "offline_gold": 14
                },
                "19": {
                    "level": 19,
                    "video": 10,
                    "offline_gold": 14.5
                },
                "20": {
                    "level": 20,
                    "video": 10,
                    "offline_gold": 15
                },
                "21": {
                    "level": 21,
                    "video": 10,
                    "offline_gold": 15.5
                },
                "22": {
                    "level": 22,
                    "video": 10,
                    "offline_gold": 16
                },
                "23": {
                    "level": 23,
                    "video": 10,
                    "offline_gold": 16.5
                },
                "24": {
                    "level": 24,
                    "video": 10,
                    "offline_gold": 17
                },
                "25": {
                    "level": 25,
                    "video": 10,
                    "offline_gold": 17.5
                },
                "26": {
                    "level": 26,
                    "video": 10,
                    "offline_gold": 18
                },
                "27": {
                    "level": 27,
                    "video": 10,
                    "offline_gold": 18.5
                },
                "28": {
                    "level": 28,
                    "video": 10,
                    "offline_gold": 19
                },
                "29": {
                    "level": 29,
                    "video": 10,
                    "offline_gold": 19.5
                },
                "30": {
                    "level": 30,
                    "video": 10,
                    "offline_gold": 20
                },
                "31": {
                    "level": 31,
                    "video": 10,
                    "offline_gold": 20.5
                },
                "32": {
                    "level": 32,
                    "video": 10,
                    "offline_gold": 21
                },
                "33": {
                    "level": 33,
                    "video": 10,
                    "offline_gold": 21.5
                },
                "34": {
                    "level": 34,
                    "video": 10,
                    "offline_gold": 22
                },
                "35": {
                    "level": 35,
                    "video": 10,
                    "offline_gold": 22.5
                },
                "36": {
                    "level": 36,
                    "video": 10,
                    "offline_gold": 23
                },
                "37": {
                    "level": 37,
                    "video": 10,
                    "offline_gold": 23.5
                },
                "38": {
                    "level": 38,
                    "video": 10,
                    "offline_gold": 24
                },
                "39": {
                    "level": 39,
                    "video": 10,
                    "offline_gold": 24.5
                },
                "40": {
                    "level": 40,
                    "video": 10,
                    "offline_gold": 25
                },
                "41": {
                    "level": 41,
                    "video": 10,
                    "offline_gold": 25.5
                },
                "42": {
                    "level": 42,
                    "video": 10,
                    "offline_gold": 26
                },
                "43": {
                    "level": 43,
                    "video": 10,
                    "offline_gold": 26.5
                },
                "44": {
                    "level": 44,
                    "video": 10,
                    "offline_gold": 27
                },
                "45": {
                    "level": 45,
                    "video": 10,
                    "offline_gold": 27.5
                },
                "46": {
                    "level": 46,
                    "video": 10,
                    "offline_gold": 28
                },
                "47": {
                    "level": 47,
                    "video": 10,
                    "offline_gold": 28.5
                },
                "48": {
                    "level": 48,
                    "video": 10,
                    "offline_gold": 29
                },
                "49": {
                    "level": 49,
                    "video": 10,
                    "offline_gold": 29.5
                },
                "50": {
                    "level": 50,
                    "video": 10,
                    "offline_gold": 30
                },
                "51": {
                    "level": 51,
                    "video": 10,
                    "offline_gold": 30.5
                },
                "52": {
                    "level": 52,
                    "video": 10,
                    "offline_gold": 31
                },
                "53": {
                    "level": 53,
                    "video": 10,
                    "offline_gold": 31.5
                },
                "54": {
                    "level": 54,
                    "video": 10,
                    "offline_gold": 32
                },
                "55": {
                    "level": 55,
                    "video": 10,
                    "offline_gold": 32.5
                },
                "56": {
                    "level": 56,
                    "video": 10,
                    "offline_gold": 33
                },
                "57": {
                    "level": 57,
                    "video": 10,
                    "offline_gold": 33.5
                },
                "58": {
                    "level": 58,
                    "video": 10,
                    "offline_gold": 34
                },
                "59": {
                    "level": 59,
                    "video": 10,
                    "offline_gold": 34.5
                },
                "60": {
                    "level": 60,
                    "video": 10,
                    "offline_gold": 35
                },
                "61": {
                    "level": 61,
                    "video": 10,
                    "offline_gold": 35.5
                },
                "62": {
                    "level": 62,
                    "video": 10,
                    "offline_gold": 36
                },
                "63": {
                    "level": 63,
                    "video": 10,
                    "offline_gold": 36.5
                },
                "64": {
                    "level": 64,
                    "video": 10,
                    "offline_gold": 37
                },
                "65": {
                    "level": 65,
                    "video": 10,
                    "offline_gold": 37.5
                },
                "66": {
                    "level": 66,
                    "video": 10,
                    "offline_gold": 38
                },
                "67": {
                    "level": 67,
                    "video": 10,
                    "offline_gold": 38.5
                },
                "68": {
                    "level": 68,
                    "video": 10,
                    "offline_gold": 39
                },
                "69": {
                    "level": 69,
                    "video": 10,
                    "offline_gold": 39.5
                },
                "70": {
                    "level": 70,
                    "video": 10,
                    "offline_gold": 40
                },
                "71": {
                    "level": 71,
                    "video": 10,
                    "offline_gold": 40.5
                },
                "72": {
                    "level": 72,
                    "video": 10,
                    "offline_gold": 41
                },
                "73": {
                    "level": 73,
                    "video": 10,
                    "offline_gold": 41.5
                },
                "74": {
                    "level": 74,
                    "video": 10,
                    "offline_gold": 42
                },
                "75": {
                    "level": 75,
                    "video": 10,
                    "offline_gold": 42.5
                },
                "76": {
                    "level": 76,
                    "video": 10,
                    "offline_gold": 43
                },
                "77": {
                    "level": 77,
                    "video": 10,
                    "offline_gold": 43.5
                },
                "78": {
                    "level": 78,
                    "video": 10,
                    "offline_gold": 44
                },
                "79": {
                    "level": 79,
                    "video": 10,
                    "offline_gold": 44.5
                },
                "80": {
                    "level": 80,
                    "video": 10,
                    "offline_gold": 45
                },
                "81": {
                    "level": 81,
                    "video": 10,
                    "offline_gold": 45.5
                },
                "82": {
                    "level": 82,
                    "video": 10,
                    "offline_gold": 46
                },
                "83": {
                    "level": 83,
                    "video": 10,
                    "offline_gold": 46.5
                },
                "84": {
                    "level": 84,
                    "video": 10,
                    "offline_gold": 47
                },
                "85": {
                    "level": 85,
                    "video": 10,
                    "offline_gold": 47.5
                },
                "86": {
                    "level": 86,
                    "video": 10,
                    "offline_gold": 48
                },
                "87": {
                    "level": 87,
                    "video": 10,
                    "offline_gold": 48.5
                },
                "88": {
                    "level": 88,
                    "video": 10,
                    "offline_gold": 49
                },
                "89": {
                    "level": 89,
                    "video": 10,
                    "offline_gold": 49.5
                },
                "90": {
                    "level": 90,
                    "video": 10,
                    "offline_gold": 50
                },
                "91": {
                    "level": 91,
                    "video": 10,
                    "offline_gold": 50.5
                },
                "92": {
                    "level": 92,
                    "video": 10,
                    "offline_gold": 51
                },
                "93": {
                    "level": 93,
                    "video": 10,
                    "offline_gold": 51.5
                },
                "94": {
                    "level": 94,
                    "video": 10,
                    "offline_gold": 52
                },
                "95": {
                    "level": 95,
                    "video": 10,
                    "offline_gold": 52.5
                },
                "96": {
                    "level": 96,
                    "video": 10,
                    "offline_gold": 53
                },
                "97": {
                    "level": 97,
                    "video": 10,
                    "offline_gold": 53.5
                },
                "98": {
                    "level": 98,
                    "video": 10,
                    "offline_gold": 54
                },
                "99": {
                    "level": 99,
                    "video": 10,
                    "offline_gold": 54.5
                },
                "100": {
                    "level": 100,
                    "video": 10,
                    "offline_gold": 55
                }
            },
            "landInfo": {
                "1": {
                    "id": 1,
                    "skinType": 5,
                    "skinId": 17,
                    "workerId": 1
                },
                "2": {
                    "id": 2,
                    "skinType": 6,
                    "skinId": 21,
                    "workerId": 2
                },
                "3": {
                    "id": 3,
                    "skinType": 7,
                    "skinId": 25,
                    "workerId": 3
                },
                "4": {
                    "id": 4,
                    "skinType": 8,
                    "skinId": 29,
                    "workerId": 4
                },
                "5": {
                    "id": 5,
                    "skinType": 9,
                    "skinId": 33,
                    "workerId": 5
                },
                "6": {
                    "id": 6,
                    "skinType": 10,
                    "skinId": 37,
                    "workerId": 6
                },
                "7": {
                    "id": 7,
                    "skinType": 11,
                    "skinId": 41,
                    "workerId": 7
                },
                "8": {
                    "id": 8,
                    "skinType": 12,
                    "skinId": 45,
                    "workerId": 8
                },
                "9": {
                    "id": 9,
                    "skinType": 13,
                    "skinId": 49,
                    "workerId": 9
                }
            },
            "skinType": {
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
            },
            "skinInfo": {
                "1": {
                    "id": 1,
                    "name": "小草棚",
                    "icon": "house_1",
                    "type": 1,
                    "buff": 0,
                    "cost": 100,
                    "level": 1,
                    "desc": "解锁每日任务与成就系统."
                },
                "2": {
                    "id": 2,
                    "name": "木屋",
                    "icon": "house_2",
                    "type": 1,
                    "buff": 0,
                    "cost": 500,
                    "level": 5,
                    "desc": "开启市场可购买或出售商品 ."
                },
                "3": {
                    "id": 3,
                    "name": "砖房",
                    "icon": "house_3",
                    "type": 1,
                    "buff": 0,
                    "cost": 10000,
                    "level": 10,
                    "desc": "获得聊天权限."
                },
                "4": {
                    "id": 4,
                    "name": "别墅",
                    "icon": "house_4",
                    "type": 1,
                    "buff": 0,
                    "cost": 15000,
                    "level": 20,
                    "desc": "可加入或创建公会."
                },
                "5": {
                    "id": 5,
                    "name": "迷你仓库",
                    "icon": "store_1",
                    "type": 2,
                    "buff": 100,
                    "cost": 0,
                    "level": 0,
                    "desc": "获得100kg仓库容量."
                },
                "6": {
                    "id": 6,
                    "name": "小仓库",
                    "icon": "store_2",
                    "type": 2,
                    "buff": 300,
                    "cost": 20000,
                    "level": 25,
                    "desc": "仓库容量增加至300kg."
                },
                "7": {
                    "id": 7,
                    "name": "大仓库",
                    "icon": "store_3",
                    "type": 2,
                    "buff": 500,
                    "cost": 100000,
                    "level": 50,
                    "desc": "仓库容量增加至500kg."
                },
                "8": {
                    "id": 8,
                    "name": "超大仓库",
                    "icon": "store_4",
                    "type": 2,
                    "buff": 1000,
                    "cost": 320000,
                    "level": 100,
                    "desc": "仓库容量增加至1000kg."
                },
                "9": {
                    "id": 9,
                    "name": "简易渠",
                    "icon": "tap_1",
                    "type": 3,
                    "buff": 0.1,
                    "cost": 900,
                    "level": 9,
                    "desc": "减少作物成熟时间10%."
                },
                "10": {
                    "id": 10,
                    "name": "铁水管",
                    "icon": "tap_2",
                    "type": 3,
                    "buff": 0.15,
                    "cost": 50000,
                    "level": 30,
                    "desc": "减少作物成熟时间15%."
                },
                "11": {
                    "id": 11,
                    "name": "铜制水管",
                    "icon": "tap_3",
                    "type": 3,
                    "buff": 0.2,
                    "cost": 150000,
                    "level": 60,
                    "desc": "减少作物成熟时间20%."
                },
                "12": {
                    "id": 12,
                    "name": "花式渠",
                    "icon": "tap_4",
                    "type": 3,
                    "buff": 0.3,
                    "cost": 550000,
                    "level": 120,
                    "desc": "减少作物成熟时间30%."
                },
                "13": {
                    "id": 13,
                    "name": "木栅栏",
                    "icon": "fence_1",
                    "type": 4,
                    "buff": 0.05,
                    "cost": 1200,
                    "level": 12,
                    "desc": "防盗几率增加至5%."
                },
                "14": {
                    "id": 14,
                    "name": "红栅栏",
                    "icon": "fence_2",
                    "type": 4,
                    "buff": 0.1,
                    "cost": 80000,
                    "level": 35,
                    "desc": "防盗几率增加至10%."
                },
                "15": {
                    "id": 15,
                    "name": "双板栅栏",
                    "icon": "fence_3",
                    "type": 4,
                    "buff": 0.15,
                    "cost": 200000,
                    "level": 75,
                    "desc": "防盗几率增加至15%."
                },
                "16": {
                    "id": 16,
                    "name": "铁艺栅栏",
                    "icon": "fence_4",
                    "type": 4,
                    "buff": 0.2,
                    "cost": 880000,
                    "level": 150,
                    "desc": "防盗几率增加至20%."
                },
                "17": {
                    "id": 17,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 5,
                    "buff": 2,
                    "cost": 0,
                    "level": 0,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "18": {
                    "id": 18,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 5,
                    "buff": 4,
                    "cost": 20000,
                    "level": 30,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "19": {
                    "id": 19,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 5,
                    "buff": 6,
                    "cost": 150000,
                    "level": 80,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "20": {
                    "id": 20,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 5,
                    "buff": 8,
                    "cost": 600000,
                    "level": 200,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "21": {
                    "id": 21,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 6,
                    "buff": 2,
                    "cost": 10,
                    "level": 2,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "22": {
                    "id": 22,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 6,
                    "buff": 4,
                    "cost": 30000,
                    "level": 32,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "23": {
                    "id": 23,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 6,
                    "buff": 6,
                    "cost": 200000,
                    "level": 85,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "24": {
                    "id": 24,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 6,
                    "buff": 8,
                    "cost": 650000,
                    "level": 210,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "25": {
                    "id": 25,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 7,
                    "buff": 2,
                    "cost": 100,
                    "level": 4,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "26": {
                    "id": 26,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 7,
                    "buff": 4,
                    "cost": 40000,
                    "level": 34,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "27": {
                    "id": 27,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 7,
                    "buff": 6,
                    "cost": 250000,
                    "level": 90,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "28": {
                    "id": 28,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 7,
                    "buff": 8,
                    "cost": 700000,
                    "level": 220,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "29": {
                    "id": 29,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 8,
                    "buff": 2,
                    "cost": 200,
                    "level": 6,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "30": {
                    "id": 30,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 8,
                    "buff": 4,
                    "cost": 50000,
                    "level": 36,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "31": {
                    "id": 31,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 8,
                    "buff": 6,
                    "cost": 300000,
                    "level": 95,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "32": {
                    "id": 32,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 8,
                    "buff": 8,
                    "cost": 750000,
                    "level": 230,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "33": {
                    "id": 33,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 9,
                    "buff": 2,
                    "cost": 500,
                    "level": 8,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "34": {
                    "id": 34,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 9,
                    "buff": 4,
                    "cost": 60000,
                    "level": 38,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "35": {
                    "id": 35,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 9,
                    "buff": 6,
                    "cost": 350000,
                    "level": 100,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "36": {
                    "id": 36,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 9,
                    "buff": 8,
                    "cost": 800000,
                    "level": 240,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "37": {
                    "id": 37,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 10,
                    "buff": 2,
                    "cost": 1000,
                    "level": 10,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "38": {
                    "id": 38,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 10,
                    "buff": 4,
                    "cost": 70000,
                    "level": 40,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "39": {
                    "id": 39,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 10,
                    "buff": 6,
                    "cost": 400000,
                    "level": 105,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "40": {
                    "id": 40,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 10,
                    "buff": 8,
                    "cost": 850000,
                    "level": 250,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "41": {
                    "id": 41,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 11,
                    "buff": 2,
                    "cost": 2000,
                    "level": 12,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "42": {
                    "id": 42,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 11,
                    "buff": 4,
                    "cost": 80000,
                    "level": 45,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "43": {
                    "id": 43,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 11,
                    "buff": 6,
                    "cost": 450000,
                    "level": 110,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "44": {
                    "id": 44,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 11,
                    "buff": 8,
                    "cost": 900000,
                    "level": 260,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "45": {
                    "id": 45,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 12,
                    "buff": 2,
                    "cost": 5000,
                    "level": 15,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "46": {
                    "id": 46,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 12,
                    "buff": 4,
                    "cost": 90000,
                    "level": 50,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "47": {
                    "id": 47,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 12,
                    "buff": 6,
                    "cost": 500000,
                    "level": 115,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "48": {
                    "id": 48,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 12,
                    "buff": 8,
                    "cost": 950000,
                    "level": 270,
                    "desc": "农作物产量x4倍，产出8kg."
                },
                "49": {
                    "id": 49,
                    "name": "黄土地",
                    "icon": "land_1",
                    "type": 13,
                    "buff": 2,
                    "cost": 10000,
                    "level": 20,
                    "desc": "可种植各种农作物，产量2kg."
                },
                "50": {
                    "id": 50,
                    "name": "红土地",
                    "icon": "land_2",
                    "type": 13,
                    "buff": 4,
                    "cost": 100000,
                    "level": 55,
                    "desc": "农作物产量x2倍，产出4kg."
                },
                "51": {
                    "id": 51,
                    "name": "黑土地",
                    "icon": "land_3",
                    "type": 13,
                    "buff": 6,
                    "cost": 550000,
                    "level": 120,
                    "desc": "农作物产量x3倍，产出6kg."
                },
                "52": {
                    "id": 52,
                    "name": "金土地",
                    "icon": "land_4",
                    "type": 13,
                    "buff": 8,
                    "cost": 1000000,
                    "level": 280,
                    "desc": "农作物产量x4倍，产出8kg."
                }
            },
            "seedInfo": {
                "1": {
                    "id": 1,
                    "name": "西红柿",
                    "cost": 5,
                    "time": 300,
                    "order_gold": 15,
                    "order_exp": 10,
                    "price_diamond": 1,
                    "redpack_num": 5,
                    "redpack_rate": 0.2,
                    "unlock": 1,
                    "desc": "西红柿原产南美洲，中国南北方广泛栽培。果实营养丰富，具特殊风味。可以生食、煮食、加工番茄酱、汁或整果罐藏。"
                },
                "2": {
                    "id": 2,
                    "name": "大白菜",
                    "cost": 15,
                    "time": 600,
                    "order_gold": 45,
                    "order_exp": 15,
                    "price_diamond": 2,
                    "redpack_num": 10,
                    "redpack_rate": 0.1,
                    "unlock": 2,
                    "desc": "大白菜原分布于中国华北，中国各地广泛栽培。菜叶可供炒食、生食、盐腌、酱渍，外层脱落的菜叶尚可作饲料，具有一定的药用价值。"
                },
                "3": {
                    "id": 3,
                    "name": "胡萝卜",
                    "cost": 30,
                    "time": 900,
                    "order_gold": 90,
                    "order_exp": 30,
                    "price_diamond": 3,
                    "redpack_num": 15,
                    "redpack_rate": 0.0666666666666667,
                    "unlock": 5,
                    "desc": "胡萝卜原产亚洲西部，12世纪经伊朗传入中国。富含胡萝卜素可以促进生长，防止细菌感染，以及保护表皮组织的功能与作用。"
                },
                "4": {
                    "id": 4,
                    "name": "苹果",
                    "cost": 45,
                    "time": 1800,
                    "order_gold": 135,
                    "order_exp": 45,
                    "price_diamond": 5,
                    "redpack_num": 20,
                    "redpack_rate": 0.05,
                    "unlock": 10,
                    "desc": "苹果是一种低热量的食物，每100克产生大约60千卡左右的热量。营养成分可溶性大，容易被人体吸收，使皮肤润滑柔嫩。"
                },
                "5": {
                    "id": 5,
                    "name": "葡萄",
                    "cost": 60,
                    "time": 3600,
                    "order_gold": 180,
                    "order_exp": 60,
                    "price_diamond": 6,
                    "redpack_num": 25,
                    "redpack_rate": 0.04,
                    "unlock": 15,
                    "desc": "葡萄是世界最古老的果树树种之一，原产亚洲西部，世界各地均有栽培。可生食、制葡萄干或酿酒，根和藤药用能止呕、安胎。"
                },
                "6": {
                    "id": 6,
                    "name": "橙子",
                    "cost": 75,
                    "time": 5400,
                    "order_gold": 225,
                    "order_exp": 75,
                    "price_diamond": 8,
                    "redpack_num": 30,
                    "redpack_rate": 0.0333333333333333,
                    "unlock": 20,
                    "desc": "橙子为橙树的果实，亦称黄果、柑子、金环、柳丁。果肉味美多汁，也可以用作其他食物的调料，幼果、落果可干制作药用。"
                },
                "7": {
                    "id": 7,
                    "name": "南瓜",
                    "cost": 90,
                    "time": 7200,
                    "order_gold": 270,
                    "order_exp": 90,
                    "price_diamond": 9,
                    "redpack_num": 35,
                    "redpack_rate": 0.0285714285714286,
                    "unlock": 25,
                    "desc": "南瓜原产墨西哥到中美洲一带，明代传入中国。果实可蒸煮，味甜，亦可作为主食。全株各部具有一定的药用价值。"
                },
                "8": {
                    "id": 8,
                    "name": "茄子",
                    "cost": 105,
                    "time": 10800,
                    "order_gold": 315,
                    "order_exp": 105,
                    "price_diamond": 11,
                    "redpack_num": 40,
                    "redpack_rate": 0.025,
                    "unlock": 30,
                    "desc": "茄子原产亚洲热带，中国各省均有栽培。果可供蔬食。根、茎、叶入药，为收敛剂，有利尿之效，叶也可以作麻醉剂。"
                },
                "9": {
                    "id": 9,
                    "name": "黄瓜",
                    "cost": 120,
                    "time": 14400,
                    "order_gold": 360,
                    "order_exp": 120,
                    "price_diamond": 12,
                    "redpack_num": 45,
                    "redpack_rate": 0.0222222222222222,
                    "unlock": 35,
                    "desc": "黄瓜为中国各地夏季主要菜蔬之一，中国各地普遍栽培。茎藤药用，能消炎、祛痰、镇痉。"
                },
                "10": {
                    "id": 10,
                    "name": "鸭梨",
                    "cost": 135,
                    "time": 18000,
                    "order_gold": 405,
                    "order_exp": 135,
                    "price_diamond": 14,
                    "redpack_num": 50,
                    "redpack_rate": 0.02,
                    "unlock": 40,
                    "desc": "鸭梨果皮薄，果肉厚，肉质细腻，酥脆多汁，甘甜爽口，含多种营养成分，具有生津、止渴、润肺、宽肠、强心、利尿等作用。"
                },
                "11": {
                    "id": 11,
                    "name": "香蕉",
                    "cost": 150,
                    "time": 21600,
                    "order_gold": 450,
                    "order_exp": 150,
                    "price_diamond": 15,
                    "redpack_num": 55,
                    "redpack_rate": 0.0181818181818182,
                    "unlock": 45,
                    "desc": "香蕉原产亚洲东南部，热带地区广泛种植。果实味香、富含营养。植株为大型草本，每一根株可活多年。"
                },
                "12": {
                    "id": 12,
                    "name": "芒果",
                    "cost": 165,
                    "time": 25200,
                    "order_gold": 495,
                    "order_exp": 165,
                    "price_diamond": 17,
                    "redpack_num": 60,
                    "redpack_rate": 0.0166666666666667,
                    "unlock": 50,
                    "desc": "芒果为著名热带水果之一，原产印度。果实含有糖、蛋白质、粗纤维，可制果汁、果酱、罐头、腌渍、酸辣泡菜及芒果奶粉、蜜饯等。"
                },
                "13": {
                    "id": 13,
                    "name": "玉米",
                    "cost": 180,
                    "time": 28800,
                    "order_gold": 540,
                    "order_exp": 180,
                    "price_diamond": 18,
                    "redpack_num": 65,
                    "redpack_rate": 0.0153846153846154,
                    "unlock": 55,
                    "desc": "玉米原产于中、南美洲，为世界重要的粮食作物，具有很强环境适应性。营养价值较高，煮熟即可食用，味微甜。"
                },
                "14": {
                    "id": 14,
                    "name": "豌豆",
                    "cost": 195,
                    "time": 32400,
                    "order_gold": 585,
                    "order_exp": 195,
                    "price_diamond": 20,
                    "redpack_num": 70,
                    "redpack_rate": 0.0142857142857143,
                    "unlock": 60,
                    "desc": "豌豆原产地中海和中亚细亚地区。种子及嫩荚、嫩苗均可食用，茎叶能清凉解暑，并作绿肥、饲料或燃料。"
                },
                "15": {
                    "id": 15,
                    "name": "土豆",
                    "cost": 210,
                    "time": 36000,
                    "order_gold": 630,
                    "order_exp": 210,
                    "price_diamond": 21,
                    "redpack_num": 75,
                    "redpack_rate": 0.0133333333333333,
                    "unlock": 65,
                    "desc": "土豆原产于南美洲安第斯山区。含有大量的淀粉，能为人体提供丰富的热量，且富含蛋白质、氨基酸及多种维生素、矿物质。"
                },
                "16": {
                    "id": 16,
                    "name": "菠萝",
                    "cost": 225,
                    "time": 43200,
                    "order_gold": 675,
                    "order_exp": 225,
                    "price_diamond": 23,
                    "redpack_num": 80,
                    "redpack_rate": 0.0125,
                    "unlock": 70,
                    "desc": "菠萝原产于南美洲，16世纪从巴西传入中国，岭南四大名果之一。肉色金黄，香味浓郁，甜酸适口，清脆多汁。"
                },
                "17": {
                    "id": 17,
                    "name": "柠檬",
                    "cost": 240,
                    "time": 50400,
                    "order_gold": 720,
                    "order_exp": 240,
                    "price_diamond": 24,
                    "redpack_num": 85,
                    "redpack_rate": 0.0117647058823529,
                    "unlock": 75,
                    "desc": "柠檬原产东南亚，中国长江以南地区。果实汁多肉脆，有浓郁的芳香气，为上等调味料，用来调制饮料菜肴、化妆品等。"
                },
                "18": {
                    "id": 18,
                    "name": "甘蔗",
                    "cost": 255,
                    "time": 57600,
                    "order_gold": 765,
                    "order_exp": 255,
                    "price_diamond": 26,
                    "redpack_num": 90,
                    "redpack_rate": 0.0111111111111111,
                    "unlock": 80,
                    "desc": "甘蔗是温带和热带农作物，制造蔗糖的原料。含有丰富的糖分、水分，对人体有益的各种维生素、有机酸、钙、铁等物质。"
                },
                "19": {
                    "id": 19,
                    "name": "洋葱",
                    "cost": 270,
                    "time": 64800,
                    "order_gold": 810,
                    "order_exp": 270,
                    "price_diamond": 27,
                    "redpack_num": 95,
                    "redpack_rate": 0.0105263157894737,
                    "unlock": 85,
                    "desc": "洋葱原产亚洲西部，是中国主栽蔬菜之一。肉质柔嫩，汁多辣味淡，品质佳，适于生食。被誉为“菜中皇后”，营养价值较高。"
                },
                "20": {
                    "id": 20,
                    "name": "秋葵",
                    "cost": 285,
                    "time": 72000,
                    "order_gold": 855,
                    "order_exp": 285,
                    "price_diamond": 29,
                    "redpack_num": 100,
                    "redpack_rate": 0.01,
                    "unlock": 90,
                    "desc": "秋葵原产地印度，广泛栽培于热带和亚热带地区。有蔬菜王之称，其嫩荚肉质柔嫩，口感爽滑，除嫩果可食外，其叶片、芽、花也可食用。"
                },
                "21": {
                    "id": 21,
                    "name": "蓝莓",
                    "cost": 300,
                    "time": 79200,
                    "order_gold": 900,
                    "order_exp": 300,
                    "price_diamond": 30,
                    "redpack_num": 105,
                    "redpack_rate": 0.00952380952380952,
                    "unlock": 95,
                    "desc": "蓝莓原生于北美洲与东亚，生长于海拔900 ~ 2300 m的地区。果实中含有丰富的营养成分，尤其富含花青素，具有良好的营养保健作用。"
                },
                "22": {
                    "id": 22,
                    "name": "猕猴桃",
                    "cost": 315,
                    "time": 86400,
                    "order_gold": 945,
                    "order_exp": 315,
                    "price_diamond": 32,
                    "redpack_num": 110,
                    "redpack_rate": 0.00909090909090909,
                    "unlock": 100,
                    "desc": "中国是猕猴桃的原产地。因为果皮覆毛，貌似猕猴而得名，是一种品质鲜嫩，营养丰富，风味鲜美的水果。"
                }
            },
            "orderInfo": {
                "1": {
                    "id": 1,
                    "unlock_video": 0
                },
                "2": {
                    "id": 2,
                    "unlock_video": 0
                },
                "3": {
                    "id": 3,
                    "unlock_video": 1
                },
                "4": {
                    "id": 4,
                    "unlock_video": 3
                },
                "5": {
                    "id": 5,
                    "unlock_video": 5
                },
                "6": {
                    "id": 6,
                    "unlock_video": 10
                },
                "7": {
                    "id": 7,
                    "unlock_video": 20
                },
                "8": {
                    "id": 8,
                    "unlock_video": 30
                },
                "9": {
                    "id": 9,
                    "unlock_video": 30
                },
                "10": {
                    "id": 10,
                    "unlock_video": 30
                },
                "11": {
                    "id": 11,
                    "unlock_video": 30
                },
                "12": {
                    "id": 12,
                    "unlock_video": 30
                },
                "13": {
                    "id": 13,
                    "unlock_video": 30
                },
                "14": {
                    "id": 14,
                    "unlock_video": 30
                },
                "15": {
                    "id": 15,
                    "unlock_video": 30
                },
                "16": {
                    "id": 16,
                    "unlock_video": 30
                },
                "17": {
                    "id": 17,
                    "unlock_video": 30
                },
                "18": {
                    "id": 18,
                    "unlock_video": 30
                },
                "19": {
                    "id": 19,
                    "unlock_video": 30
                },
                "20": {
                    "id": 20,
                    "unlock_video": 30
                }
            },
            "animalInfo": {
                "1": {
                    "id": 1,
                    "name": "蛋壳",
                    "unlock_level": 1,
                    "order_gold": 0,
                    "order_exp": 0,
                    "pretend_order": 1
                },
                "2": {
                    "id": 2,
                    "name": "大耳朵",
                    "unlock_level": 1,
                    "order_gold": 0.02,
                    "order_exp": 0,
                    "pretend_order": 2
                },
                "3": {
                    "id": 3,
                    "name": "猪小粉",
                    "unlock_level": 2,
                    "order_gold": 0.04,
                    "order_exp": 0,
                    "pretend_order": 3
                },
                "4": {
                    "id": 4,
                    "name": "二妹儿",
                    "unlock_level": 5,
                    "order_gold": 0.06,
                    "order_exp": 0,
                    "pretend_order": 4
                },
                "5": {
                    "id": 5,
                    "name": "福克斯",
                    "unlock_level": 10,
                    "order_gold": 0.08,
                    "order_exp": 0,
                    "pretend_order": 5
                },
                "6": {
                    "id": 6,
                    "name": "斑点狗",
                    "unlock_level": 15,
                    "order_gold": 0.1,
                    "order_exp": 0.02,
                    "pretend_order": 6
                },
                "7": {
                    "id": 7,
                    "name": "角角",
                    "unlock_level": 20,
                    "order_gold": 0.1,
                    "order_exp": 0.04,
                    "pretend_order": 7
                },
                "8": {
                    "id": 8,
                    "name": "潘大先生",
                    "unlock_level": 25,
                    "order_gold": 0.1,
                    "order_exp": 0.06,
                    "pretend_order": 8
                },
                "9": {
                    "id": 9,
                    "name": "小黄",
                    "unlock_level": 30,
                    "order_gold": 0.1,
                    "order_exp": 0.08,
                    "pretend_order": 9
                },
                "10": {
                    "id": 10,
                    "name": "卷毛",
                    "unlock_level": 35,
                    "order_gold": 0.1,
                    "order_exp": 0.1,
                    "pretend_order": 10
                },
                "11": {
                    "id": 11,
                    "name": "豚豚",
                    "unlock_level": 40,
                    "order_gold": 0.12,
                    "order_exp": 0.2,
                    "pretend_order": 11
                },
                "12": {
                    "id": 12,
                    "name": "王子",
                    "unlock_level": 45,
                    "order_gold": 0.14,
                    "order_exp": 0.2,
                    "pretend_order": 12
                },
                "13": {
                    "id": 13,
                    "name": "小胸许",
                    "unlock_level": 50,
                    "order_gold": 0.16,
                    "order_exp": 0.2,
                    "pretend_order": 13
                },
                "14": {
                    "id": 14,
                    "name": "大眼儿",
                    "unlock_level": 55,
                    "order_gold": 0.18,
                    "order_exp": 0.2,
                    "pretend_order": 14
                },
                "15": {
                    "id": 15,
                    "name": "长鼻象",
                    "unlock_level": 60,
                    "order_gold": 0.2,
                    "order_exp": 0.2,
                    "pretend_order": 15
                },
                "16": {
                    "id": 16,
                    "name": "小西装",
                    "unlock_level": 65,
                    "order_gold": 0.3,
                    "order_exp": 0.22,
                    "pretend_order": 16
                },
                "17": {
                    "id": 17,
                    "name": "大壮",
                    "unlock_level": 70,
                    "order_gold": 0.3,
                    "order_exp": 0.24,
                    "pretend_order": 17
                },
                "18": {
                    "id": 18,
                    "name": "悟空",
                    "unlock_level": 75,
                    "order_gold": 0.3,
                    "order_exp": 0.26,
                    "pretend_order": 18
                },
                "19": {
                    "id": 19,
                    "name": "牛魔王",
                    "unlock_level": 80,
                    "order_gold": 0.3,
                    "order_exp": 0.28,
                    "pretend_order": 19
                },
                "20": {
                    "id": 20,
                    "name": "点点",
                    "unlock_level": 85,
                    "order_gold": 0.3,
                    "order_exp": 0.3,
                    "pretend_order": 20
                },
                "21": {
                    "id": 21,
                    "name": "大灰",
                    "unlock_level": 90,
                    "order_gold": 0.32,
                    "order_exp": 0.4,
                    "pretend_order": 21
                },
                "22": {
                    "id": 22,
                    "name": "树袋熊",
                    "unlock_level": 95,
                    "order_gold": 0.34,
                    "order_exp": 0.4,
                    "pretend_order": 22
                },
                "23": {
                    "id": 23,
                    "name": "小西几",
                    "unlock_level": 100,
                    "order_gold": 0.36,
                    "order_exp": 0.4,
                    "pretend_order": 23
                },
                "24": {
                    "id": 24,
                    "name": "比尔",
                    "unlock_level": 105,
                    "order_gold": 0.38,
                    "order_exp": 0.4,
                    "pretend_order": 24
                },
                "25": {
                    "id": 25,
                    "name": "小草",
                    "unlock_level": 110,
                    "order_gold": 0.4,
                    "order_exp": 0.4,
                    "pretend_order": 25
                },
                "26": {
                    "id": 26,
                    "name": "带带",
                    "unlock_level": 115,
                    "order_gold": 0.5,
                    "order_exp": 0.42,
                    "pretend_order": 26
                },
                "27": {
                    "id": 27,
                    "name": "猪小野",
                    "unlock_level": 120,
                    "order_gold": 0.5,
                    "order_exp": 0.44,
                    "pretend_order": 27
                },
                "28": {
                    "id": 28,
                    "name": "闪电",
                    "unlock_level": 125,
                    "order_gold": 0.5,
                    "order_exp": 0.46,
                    "pretend_order": 28
                },
                "29": {
                    "id": 29,
                    "name": "双峰驼",
                    "unlock_level": 130,
                    "order_gold": 0.5,
                    "order_exp": 0.48,
                    "pretend_order": 29
                },
                "30": {
                    "id": 30,
                    "name": "小灰",
                    "unlock_level": 135,
                    "order_gold": 0.5,
                    "order_exp": 0.5,
                    "pretend_order": 30
                },
                "31": {
                    "id": 31,
                    "name": "三金",
                    "unlock_level": 140,
                    "order_gold": 0.52,
                    "order_exp": 0.6,
                    "pretend_order": 31
                },
                "32": {
                    "id": 32,
                    "name": "穿山甲",
                    "unlock_level": 145,
                    "order_gold": 0.54,
                    "order_exp": 0.6,
                    "pretend_order": 32
                },
                "33": {
                    "id": 33,
                    "name": "大白",
                    "unlock_level": 150,
                    "order_gold": 0.56,
                    "order_exp": 0.6,
                    "pretend_order": 33
                },
                "34": {
                    "id": 34,
                    "name": "墨镜",
                    "unlock_level": 155,
                    "order_gold": 0.58,
                    "order_exp": 0.6,
                    "pretend_order": 34
                },
                "35": {
                    "id": 35,
                    "name": "大脑腐",
                    "unlock_level": 160,
                    "order_gold": 0.6,
                    "order_exp": 0.6,
                    "pretend_order": 35
                },
                "36": {
                    "id": 36,
                    "name": "鸭嘴兽",
                    "unlock_level": 165,
                    "order_gold": 0.7,
                    "order_exp": 0.62,
                    "pretend_order": 36
                },
                "37": {
                    "id": 37,
                    "name": "大仙",
                    "unlock_level": 170,
                    "order_gold": 0.7,
                    "order_exp": 0.64,
                    "pretend_order": 37
                },
                "38": {
                    "id": 38,
                    "name": "牛头梗",
                    "unlock_level": 175,
                    "order_gold": 0.7,
                    "order_exp": 0.66,
                    "pretend_order": 38
                },
                "39": {
                    "id": 39,
                    "name": "杰克",
                    "unlock_level": 180,
                    "order_gold": 0.7,
                    "order_exp": 0.68,
                    "pretend_order": 39
                },
                "40": {
                    "id": 40,
                    "name": "水獭",
                    "unlock_level": 185,
                    "order_gold": 0.7,
                    "order_exp": 0.7,
                    "pretend_order": 40
                },
                "41": {
                    "id": 41,
                    "name": "平头哥",
                    "unlock_level": 190,
                    "order_gold": 0.72,
                    "order_exp": 0.8,
                    "pretend_order": 41
                },
                "42": {
                    "id": 42,
                    "name": "老白",
                    "unlock_level": 195,
                    "order_gold": 0.74,
                    "order_exp": 0.8,
                    "pretend_order": 42
                },
                "43": {
                    "id": 43,
                    "name": "火烧",
                    "unlock_level": 200,
                    "order_gold": 0.76,
                    "order_exp": 0.8,
                    "pretend_order": 43
                },
                "44": {
                    "id": 44,
                    "name": "小黄",
                    "unlock_level": 205,
                    "order_gold": 0.78,
                    "order_exp": 0.8,
                    "pretend_order": 44
                },
                "45": {
                    "id": 45,
                    "name": "鹿迪尔",
                    "unlock_level": 210,
                    "order_gold": 0.8,
                    "order_exp": 0.8,
                    "pretend_order": 45
                },
                "46": {
                    "id": 46,
                    "name": "河马先生",
                    "unlock_level": 215,
                    "order_gold": 0.9,
                    "order_exp": 0.82,
                    "pretend_order": 46
                },
                "47": {
                    "id": 47,
                    "name": "小熊猫",
                    "unlock_level": 220,
                    "order_gold": 0.9,
                    "order_exp": 0.84,
                    "pretend_order": 47
                },
                "48": {
                    "id": 48,
                    "name": "道格",
                    "unlock_level": 225,
                    "order_gold": 0.9,
                    "order_exp": 0.86,
                    "pretend_order": 48
                },
                "49": {
                    "id": 49,
                    "name": "干脆面君",
                    "unlock_level": 230,
                    "order_gold": 0.9,
                    "order_exp": 0.88,
                    "pretend_order": 49
                },
                "50": {
                    "id": 50,
                    "name": "六号",
                    "unlock_level": 235,
                    "order_gold": 0.9,
                    "order_exp": 0.9,
                    "pretend_order": 50
                }
            },
            "workerInfo": {
                "1": {
                    "id": 1,
                    "unlock_video": 1
                },
                "2": {
                    "id": 2,
                    "unlock_video": 3
                },
                "3": {
                    "id": 3,
                    "unlock_video": 5
                },
                "4": {
                    "id": 4,
                    "unlock_video": 10
                },
                "5": {
                    "id": 5,
                    "unlock_video": 20
                },
                "6": {
                    "id": 6,
                    "unlock_video": 30
                },
                "7": {
                    "id": 7,
                    "unlock_video": 30
                },
                "8": {
                    "id": 8,
                    "unlock_video": 30
                },
                "9": {
                    "id": 9,
                    "unlock_video": 30
                }
            },
            "auctionInfo": {
                "1": {
                    "id": 1,
                    "unlock_video": 0
                },
                "2": {
                    "id": 2,
                    "unlock_video": 1
                },
                "3": {
                    "id": 3,
                    "unlock_video": 3
                },
                "4": {
                    "id": 4,
                    "unlock_video": 5
                },
                "5": {
                    "id": 5,
                    "unlock_video": 10
                },
                "6": {
                    "id": 6,
                    "unlock_video": 20
                },
                "7": {
                    "id": 7,
                    "unlock_video": 30
                },
                "8": {
                    "id": 8,
                    "unlock_video": 30
                },
                "9": {
                    "id": 9,
                    "unlock_video": 30
                }
            },
            "rankAward": {
                "1": {
                    "id": 1,
                    "name": "第1名",
                    "rank_min": 1,
                    "rank_max": 1,
                    "gold": 8800,
                    "diamond": 100
                },
                "2": {
                    "id": 2,
                    "name": "第2名",
                    "rank_min": 2,
                    "rank_max": 2,
                    "gold": 6000,
                    "diamond": 80
                },
                "3": {
                    "id": 3,
                    "name": "第3名",
                    "rank_min": 3,
                    "rank_max": 3,
                    "gold": 5000,
                    "diamond": 60
                },
                "4": {
                    "id": 4,
                    "name": "第4~10名",
                    "rank_min": 4,
                    "rank_max": 10,
                    "gold": 3000,
                    "diamond": 50
                },
                "5": {
                    "id": 5,
                    "name": "第11~20名",
                    "rank_min": 11,
                    "rank_max": 20,
                    "gold": 2000,
                    "diamond": 30
                },
                "6": {
                    "id": 6,
                    "name": "第21~50名",
                    "rank_min": 21,
                    "rank_max": 50,
                    "gold": 1500,
                    "diamond": 20
                },
                "7": {
                    "id": 7,
                    "name": "第51~100名",
                    "rank_min": 51,
                    "rank_max": 100,
                    "gold": 1000,
                    "diamond": 10
                },
                "8": {
                    "id": 8,
                    "name": "第101~500名",
                    "rank_min": 101,
                    "rank_max": 500,
                    "gold": 500,
                    "diamond": 5
                }
            },
            "guildAward": {
                "1": {
                    "id": 1,
                    "name": "第1名",
                    "rank_min": 1,
                    "rank_max": 1,
                    "gold": 6000,
                    "diamond": 30
                },
                "2": {
                    "id": 2,
                    "name": "第2名",
                    "rank_min": 2,
                    "rank_max": 2,
                    "gold": 4500,
                    "diamond": 25
                },
                "3": {
                    "id": 3,
                    "name": "第3名",
                    "rank_min": 3,
                    "rank_max": 3,
                    "gold": 3000,
                    "diamond": 20
                },
                "4": {
                    "id": 4,
                    "name": "第4~10名",
                    "rank_min": 4,
                    "rank_max": 10,
                    "gold": 2000,
                    "diamond": 15
                },
                "5": {
                    "id": 5,
                    "name": "第11~30名",
                    "rank_min": 11,
                    "rank_max": 30,
                    "gold": 1000,
                    "diamond": 10
                },
                "6": {
                    "id": 6,
                    "name": "第31~100名",
                    "rank_min": 31,
                    "rank_max": 100,
                    "gold": 500,
                    "diamond": 5
                }
            },
            "textRedpack": {
                "cash": "　1. 可兑换金额以显示档位为准，每天兑换不限次数；\n　2. 兑换比例：100福袋=1.00元；\n　3. 每兑换1元红包，还需消耗1张兑换券。",
                "diamond": "　1. 福袋达到10点以上可兑换，兑换钻石的数量以显示为准；\n　2. 兑换比例：10福袋=10钻石。",
                "withdraw": "　1. 每天可申请提现1次；\n　2. 申请后，红包金额将全部提现至微信的零钱帐户中；\n　3. 手续费20%，新用户免手续费。",
                "coupon": "每次看视频后有8%的几率获得兑换券\n点击广告可提高几率至12%"
            }
        }
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
        t = time.time() * 1000
        data = data if data else {}
        data['openid'] = self.openid
        data['sessid'] = self.sessid

        if url in self.IGNORE_URLS:
            data['gameid'] = self.GAME_ID
            data['ver'] = self.VERSION
            data['t'] = t
        else:
            c = self.encode(data, t)
            data = {
                'c': c,
                'gameid': self.GAME_ID,
                'ver': self.VERSION,
                't': t
            }
        if not url.startswith('http'):
            url = 'https://minigame.ucpopo.com/dwnc' + url

        headers = {
            'Host': 'minigame.ucpopo.com',
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': self.ua,
            'Referer': 'https://servicewechat.com/wxdbbf991feed9e2ba/14/page-frame.html',
        }

        return requests.get(url, params=data, headers=headers)

    def sign(self):
        self.look_video('other', message='签到看广告')
        res = self.get('/sign/continuousSign', {'isVideo': 2})
        data = res.json()
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

    def login(self):
        res = self.get('/login')
        data = res.json()
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
        res = self.get('/land/reap', {'landid': id, 'isVideo': self.get_is_video(can_zero=False) if red else 0})
        data = res.json()
        # print(res.json())
        if data.get('crop'):
            self.update_warehouse(data['crop'], crop_id)
        else:
            print(res.json(), flush=True)

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
        res = self.get('/land/videoSpeed', {'landid': id, 'isVideo': self.get_is_video(can_zero=False)})
        data = res.json()
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
        seed = self.get_seed_id()
        seed_id = seed['id']
        self.random_wait(1, 2, message=f'种植第{landid}块地')
        res = self.get('/land/plant', {'seedid': seed_id, 'landid': landid})
        # pprint(res.json())

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
                    res = self.get('/order/done', {'orderid': order_id})
                    pprint(res.json())
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
            res = self.get('/order/videoUnlock', {'orderid': order_id})
            print(res.json())

    def check_unlock_land(self):
        self.get('/land/unlock', {'landid': '1'})

    def check_daily(self):
        res = self.get('/task/getDayList')
        data = res.json()
        tasks = data['taskDay']
        is_take = False
        for task_id, task in tasks.items():
            if task_id != '0':
                need_done = self.task_daily.get(task_id)['times']
                done_num = task['done']
                if need_done == done_num and not task['isTake']:
                    # todo task done
                    self.random_wait(1, 2, message=f'完成任务{self.task_daily.get(task_id)["name"]}')
                    self.get('/task/takeDayAward', {'taskid': task_id})
                else:
                    is_take = task['isTake']

        total = data['total']
        done = data['done']

        if total == done and not is_take:
            res = self.get('/task/takeChest')
            pprint(res.json())

    def check_worker(self):
        for i in range(len(self.land_list)):
            if (i + 1 > len(self.worker_list) or not self.worker_list.get(str(i + 1)).get('unlock')) and self.can_video:
                self.look_video('video_advert', message=f'看视频解锁工人{i + 1}')
                res = self.get('/worker/videoUnlock', {'workerid': str(i + 1)})
                pprint(res.json())
                num = res.json()['worker']['video']
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
            res = self.get('/worker/getCatchList')
            data = res.json()
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
                    res = self.get('/worker/catch', {'workerid': k, 'otherid': worker[1]})
                    self.day_times['worker_catch'] += 1
                    pprint(res.json())
            elif info.get('status') == 0:
                # todo 放
                if info.get('createtime'):
                    work_time = (time.time() - info['createtime'] // 1000) // 3600
                    if work_time >= 12:
                        self.random_wait(0.5, 1)
                        res = self.get('/worker/free', {'workerid': k})
                        pprint(res.json())

            if info.get('gold', 0) > 1000:
                self.random_wait(0.5, 1)
                res = self.get('/worker/takeGold', {'workerid': k})
                data = res.json()
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
                        res = self.get('/land/unlock', {'landid': str(skip_type - 4)})
                        pprint(res.json())
                        self.random_wait(1, 2, message=f'解锁{info["name"]}')
                    else:
                        res = self.get('/skin/unlock', {'skinid': skin_id})
                        pprint(res.json())
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
                    res = self.get('/land/unlock', {'landid': str(landid)})
                    self.print(f'解锁地块{landid}')
                    pprint(res.json())
                break

    def get_offline_award(self):
        try:
            duration = time.time() - self.helper_info['takeAwardTime'] / 1000
            if duration > 10000:
                res = self.get('/helper/takeOfflineAward',
                               {'isVideo': self.look_video('offline', message='看广告拿金币') if self.can_gold else 0})
                data = res.json()
                self.random_wait(1, 2, message=f'获取离线金币成功，当前金币{data["gold"]}')
                self.gold = data['gold']
        except Exception as e:
            self.print('没有离线收入')

    def check_helper_level(self):
        if self.helper_info['level'] < self.level and self.can_video:
            self.look_video('video_advert', message='看广告升级管家中……')
            res = self.get('/helper/levelup', {})
            self.helper_info = res.json()['helper']
            print(res.json())

    def check_cash(self):
        self.print(f'当前资产：{self.redpack}🧧，兑换券{self.coupon}张, 💰{self.cash / 100}元')
        if self.redpack >= 500 and self.coupon >= 5:
            self.random_wait(1, 2, message='兑换5元红包')
            res = self.get('/user/redpack2cash', {'num': '500'})
            data = res.json()
            self.cash = data['cash']
            self.coupon = data['coupon']
            self.redpack = data['redpack']

        if self.cash > 30 and self.first:
            self.random_wait(1, 2, message=f'提现红包{self.cash / 100}元')
            res = self.get('/user/withdraw', {})
            pprint(res.json())
            if CAN_NOTIFY:
                send('动物农场', content=f'{self.account}\t提现红包{self.cash / 100}元')
            self.first = False

    def check_auction(self):
        if '2' in self.skip_list.keys() and self.can_video:
            for i in range(9):
                if not self.auction_list.get(str(i + 1), {}).get('unlock'):
                    self.look_video('video_advert', message='解锁拍卖位')
                    res = self.get('/auction/videoUnlock', {'auctionid': str(i + 1)})
                    pprint(res.json())
                    return

    def check_unlock_skin(self):
        for k, v in self.skip_info.items():
            if k not in self.skip_list.keys() and self.level >= v['level'] and self.gold >= v['cost']:
                self.random_wait(1, 2, message=f'解锁{v["name"]}')
                res = self.get('/skin/unloc', {'skinid': k})
                pprint(res.json())

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

    def buy_page_cache(self, page):
        rs = self._cache.get(page)
        if rs:
            # self.print(f'查找低价拍卖,第{page}页, 从缓存')
            return rs
        self.random_wait(1, 2, message=f'查找低价拍卖,第{page}页')
        res = self.get('/auction/getList', {'page': page})
        data = res.json()
        self._cache[page] = data
        return data

    def buy(self, target=None, target_num=None, k=1.5, full=0.6):
        max_page = 0
        page = 1
        if self.is_full(full) or self.gold < self.level * 1500:
            return 0
        have_buy_num = 0
        while page <= max_page or page == 1:
            data = self.buy_page_cache(page)
            max_page = data['pageMax']
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
                    res = self.get('/auction/buy', {'sellerid': open_id, 'auctionid': auctionid})
                    data = res.json()
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

    def help(self, openid):
        self.get('/visit/lookUser', {'lookid': openid})
        self.random_wait(1, 2)
        res = self.get('/visit/lookFarm', {'lookid': openid})
        data = res.json()
        water_land_ids = []
        land_list = data['landList']
        self.random_wait(1, 2)
        for landid, info in land_list.items():
            if not info.get('water', 1):
                water_land_ids.append(landid)

        random.shuffle(water_land_ids)

        for land in water_land_ids:
            if self.day_times.get('land_water', 0) < self.config.get('DAY_WATER_MAX', 20):
                self.random_wait(0.1, 1, '浇水一次')
                res = self.get('/visit/water', {'lookid': openid, 'landid': land})
                try:
                    land_list[land] = res.json()['land']
                except Exception as e:
                    pprint(res.json())
                self.day_times['land_water'] = self.day_times['land_water'] + 1

        random.shuffle(water_land_ids)

        for land in water_land_ids:
            info = land_list.get(land)
            if info['steal'] == 1 or info['expireTime'] > time.time() * 1000:
                continue
            if self.is_full():
                break
            self.random_wait(0.1, 1, '偷一次')
            res = self.get('/visit/steal', {'lookid': openid, 'landid': land})
            data = res.json()
            self.update_warehouse(data['crop'], crop=info['cropid'])
            pprint(res.json())

    def get_unlack_good(self):
        needs = defaultdict(int)
        sells = []
        for value in self.orders.values():
            goods = value.get('goods', [])
            for good in goods:
                needs[good['id']] += good['num']

        for k, info in self.warehouse.items():
            d = info['num'] - needs.get(k, 0)
            if d > 0:
                sells += [k] * d

        random.shuffle(sells)
        return sells

    def on_buy(self):
        res = self.get('/auction/getMy')
        data = res.json()
        pprint(data)
        unlack_goods = self.get_unlack_good()
        for k, info in data.items():
            expire_time = info.get('expireTime')
            unlock = info.get('unlock')
            buyer_id = info.get('buyerid')
            if expire_time:
                now = time.time() * 1000
                if now >= expire_time:
                    pass

            if buyer_id:
                self.random_wait(1, 2, message=f'收取一个拍卖')
                res = self.get('/auction/takeGold', {'auctionid': k})
                data = res.json()
                pprint(data)

                if unlack_goods:
                    sell_good_id = unlack_goods.pop()
                    self.random_wait(1,2, message=f'拍卖上架一个{self.seeds_info[sell_good_id]["name"]}')
                    self.get('/auction/on', {'auctionid': k, 'goodid': sell_good_id, 'num': 1, 'price': self.seeds_info[sell_good_id]['order_gold'] * 3, 'time': 2})
                    data = res.json()
                    pprint(data)

            if not buyer_id and not expire_time and unlock:
                if unlack_goods:
                    sell_good_id = unlack_goods.pop()
                    self.random_wait(1,2, message=f'拍卖上架一个{self.seeds_info[sell_good_id]["name"]}')
                    self.get('/auction/on', {'auctionid': k, 'goodid': sell_good_id, 'num': 1, 'price': self.seeds_info[sell_good_id]['order_gold'] * 3, 'time': 2})
                    data = res.json()
                    pprint(data)

    def get_gold(self):
        if self.can_gold:
            res = self.get('/user/getGold', {'isVideo': self.look_video('get_gold', message='看广告获取金币')})
            data = res.json()
            self.gold = data['gold']
            pprint(data)

    def check_task_main(self):
        if self.task_main.get('done'):
            task_id = self.task_main.get('id')
            if task_id:
                self.random_wait(1, 2, message=f"完成任务{self.task_main.get('name')}")
                res = self.get("/task/takeMainAward", {'taskid': task_id})
                data = res.json()
                self.update(data)

if __name__ == '__main__':
    last = None

    def parse(account):
        params = account.split(';')
        data = {}
        for param in params:
            if '=' in param:
                k, v = param.split('=')
                data[k] = v
        return data

    # accounts = "openid=xxx;sessid=xxx;&openid=xxx;&sessid=xxx;"
    accounts = os.getenv('DWNC_AUTH')
    if not accounts:
        print('请设置环境变量DWNC_AUTH', flush=True)
    
    # ua 【非必填】    
    # ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.7(0x1800072d) NetType/WIFI Language/zh_CN"
    ua = os.getenv('DWNC_UA')

    # version = "1.1.9"
    version = os.getenv('DWNC_VERSION')
    if ua:
        print(f'DWNC_UA:{ua}', flush=True)
    if version:
        Dwnc.VERSION = version
        print(f'DWNC_VERSION:{version}', flush=True)
    accounts = [parse(account) for account in accounts.split('&') if account]
    accounts = [Dwnc(**account, ua=ua) for account in accounts]

    print(f'总计{len(accounts)}个账号', flush=True)
    while True:
        try:
            for dwnc in accounts:
                print(f'---------------当前账号: {dwnc.account}------------------')
                dwnc.login()
                if last and not dwnc.is_help:
                    if last.openid != dwnc.openid:
                        dwnc.help(last.openid)
                        dwnc.is_help = True
                dwnc.get_gold()
                # dwnc.buy()
                dwnc.on_buy()
                dwnc.get_offline_award()
                dwnc.check_catch_worker()
                dwnc.check_cash()
                dwnc.check_sign()
                dwnc.check_open()
                # dwnc.check_open_land()
                dwnc.check_level()
                dwnc.check_order()
                dwnc.check_daily()
                dwnc.check_task_main()
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

            if datetime.datetime.now().hour >= 22:
                break
        except Exception as e:
            print(e, flush=True)

        Dwnc.random_wait(200, 900, message='休息一会儿～～～～')
