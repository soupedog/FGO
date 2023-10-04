# sys.path.append("/Core.air")
import logging

from airtest.cli.parser import cli_setup
from airtest.core.api import *

import ProcessControl
import RoundTemplates
from entity.Apple import Apple
from entity.Friend import Friend

# 参考文档 https://airtest.readthedocs.io/zh_CN/latest/README_MORE.html

if not cli_setup():
    auto_setup(__file__,
               logdir=False,
               devices=[
                   "android://127.0.0.1:5037/127.0.0.1:51899?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
               ],
               project_root="F:/Airtest/FGO/src/Farm.air"
               )
# 最低输出 info 级别日志
logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)


def 活动点数报酬确认():
    next_button = wait(Template(r"结算_下一步.png", record_pos=(0.366, 0.217), resolution=(1280, 720)))
    sleep(1)
    touch(next_button)


def start_farm(max_apple_number):
    current_number = 0

    while True:
        RoundTemplates.一面自启动换人狂娜双杀狐()

        # 取决于宝具动画速度，可以自行调整等待时长
        sleep(20)

        ProcessControl.close_result(None)
        # ProcessControl.close_result(活动点数报酬确认)

        current_number = ProcessControl.check_and_eat_apple(Apple.GOLDEN, current_number, max_apple_number)

        ProcessControl.select_friend(Friend.杀狐_最终_任意)


# 程序入口
max_number = 0

start_farm(max_number)
