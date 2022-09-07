# sys.path.append("/Core.air")
from airtest.cli.parser import cli_setup
from airtest.core.api import *

import Core
from entity.Apple import Apple

if not cli_setup():
    auto_setup(__file__,
               logdir=False,
               devices=[
                   "android://127.0.0.1:5037/127.0.0.1:55883?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
               ],
               project_root="F:/Airtest/FGO/src/Core.air"
               )


def C呆充三号宇宙凛加攻UB():
    Core.block_to_area_ready()

    Core.skill(1, 1, None)

    Core.skill(2, 2, 3)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)


def C呆加攻宇宙凛自充UB():
    Core.block_to_area_ready()

    Core.skill(2, 1, None)
    Core.skill(1, 3, None)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)


def C呆蓝魔放大公UB():
    Core.block_to_area_ready()

    Core.skill(2, 3, 3)

    Core.skill(3, 2, None)

    Core.start_attack()
    Core.attack_single_ultimate_combo(3)


def 大英雄一面():
    Core.block_to_area_ready()

    # Core.skill(1, 3, None)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)

def 芭娜娜杀狐二面():
    Core.block_to_area_ready()

    Core.skill(1, 1, None)
    Core.skill(1, 2, None)

    Core.skill(2, 3, 1)
    Core.skill(3, 3, 1)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)

def 芭娜娜杀狐三面():
    Core.block_to_area_ready()

    Core.skill(2, 1, 1)
    Core.skill(3, 1, 1)
    # Core.skill(2, 2, 1)
    # Core.skill(3, 2, 1)

    Core.skill(1, 1, None)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)


def 三三一宇宙凛大公(max_number):
    current_number = 0

    while True:
        C呆充三号宇宙凛加攻UB()

        C呆加攻宇宙凛自充UB()

        C呆蓝魔放大公UB()

        sleep(25)

        Core.close_result()

        current_number = Core.check_and_eat_apple(Apple.GOLDEN, current_number, max_number)

        Core.select_friend()

def 芭娜娜双杀狐通用(max_number):
    current_number = 0

    while True:
        大英雄一面()

        芭娜娜杀狐二面()

        芭娜娜杀狐三面()

        sleep(25)

        Core.close_result()

        current_number = Core.check_and_eat_apple(Apple.GOLDEN, current_number, max_number)

        Core.select_friend()



# 程序入口
max_number = 0

芭娜娜双杀狐通用(max_number)
