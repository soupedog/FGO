# sys.path.append("/Core.air")
import logging

from airtest.cli.parser import cli_setup
from airtest.core.api import *

import ProcessControl
import RoundTemplates
import MasterControl
from entity.Apple import Apple
from entity.Friend import Friend

# 参考文档 https://airtest.readthedocs.io/zh_CN/latest/README_MORE.html
    
auto_setup(__file__,
           logdir=False,
           devices=[
               "android://127.0.0.1:5037/127.0.0.1:65513?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
           ],
           project_root="E:/Airtest/FGO/src/Farm.air"
           )
    
    
# 最低输出 info 级别日志
logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)
# 全局默认配置
# 图片匹配默认阈值
ST.THRESHOLD = 0.7
# 是否为报告保存图片
ST.SAVE_IMAGE = False
# 图片搜索算法列表
ST.CVSTRATEGY = ["tpl", "sift","brisk"]

# 替换默认的RESIZE_METHOD --- 自定义无缩放方法
def custom_resize_method(w, h, sch_resolution, src_resolution):
    return int(w), int(h)

ST.RESIZE_METHOD = custom_resize_method


def 活动点数报酬确认():
    next_button = wait(
        Template(r"结算_下一步.png")
    )
    sleep(1)
    touch(next_button)


def start_farm(max_apple_number):
    current_number = 0

    while True:
        RoundTemplates.狂娜双杀狐奥伯龙()

        # 取决于宝具动画速度，可以自行调整等待时长
        sleep(20)

        ProcessControl.close_result(None)
        # ProcessControl.close_result(活动点数报酬确认)

        current_number = ProcessControl.check_and_eat_apple(Apple.BLUE, current_number, max_apple_number)

        ProcessControl.select_friend(Friend.杀狐_最终_任意)


# 程序入口
max_number = 1

start_farm(max_number)
# MasterControl.change_my_servant(3, 2, 6)
# ProcessControl.check_and_eat_apple(Apple.BLUE, 0, 1)

# print("AAAAAAAA")
# pp = ProcessControl.select_friend(Friend.C呆_最终_任意)
# print(pp)
# touch(pp)




