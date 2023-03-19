# sys.path.append("/Core.air")
import logging

from airtest.cli.parser import cli_setup
from airtest.core.api import *

import ProcessControl
import RoundTemplates
from entity.Apple import Apple
from entity.Friend import Friend

if not cli_setup():
    auto_setup(__file__,
               logdir=False,
               devices=[
                   "android://127.0.0.1:5037/127.0.0.1:64520?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
               ],
               project_root="F:/Airtest/FGO/src/Farm.air"
               )
# 最低输出 info 级别日志
logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)

def start_farm(max_apple_number):
    current_number = 0

    while True:
        RoundTemplates.大英雄狂娜()

        sleep(25)

        ProcessControl.close_result()

        current_number = ProcessControl.check_and_eat_apple(Apple.GOLDEN, current_number, max_apple_number)

        ProcessControl.select_friend(Friend.杀狐_最终_任意)


# 程序入口
max_number = 1

start_farm(max_number)
