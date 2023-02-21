# sys.path.append("/Core.air")
from airtest.cli.parser import cli_setup
from airtest.core.api import *

import ProcessControl
import RoundTemplates
from entity.Apple import Apple

if not cli_setup():
    auto_setup(__file__,
               logdir=False,
               devices=[
                   "android://127.0.0.1:5037/127.0.0.1:56419?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
               ],
               project_root="F:/Airtest/FGO/src/Core.air"
               )


def start_farm(max_apple_number):
    current_number = 0

    while True:
        RoundTemplates.达芬奇QP冲浪()

        sleep(25)

        ProcessControl.close_result()

        current_number = ProcessControl.check_and_eat_apple(Apple.SILVER, current_number, max_apple_number)

        ProcessControl.select_friend()


# 程序入口
max_number = 1

start_farm(max_number)
