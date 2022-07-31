# sys.path.append("/Core.air")
from airtest.cli.parser import cli_setup
from airtest.core.api import *

import Core
from entity.Apple import Apple

if not cli_setup():
    auto_setup(__file__,
               logdir=True,
               devices=[
                   "android://127.0.0.1:5037/127.0.0.1:55179?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
               ],
               project_root="F:/Airtest/FGO/src/Core.air"
               )


def tu1():
    Core.block_to_area_ready()

    Core.skill(1, 3, None)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)


def tu2():
    Core.block_to_area_ready()

    Core.skill(1, 1, None)
    Core.skill(1, 2, None)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)


def tu3():
    Core.block_to_area_ready()

    Core.skill(2, 1, 1)
    Core.skill(2, 2, 1)
    Core.skill(2, 3, 1)

    Core.skill(3, 1, 1)
    Core.skill(3, 2, 1)
    Core.skill(3, 3, 1)

    Core.start_attack()
    Core.attack_single_ultimate_combo(1)


current_number = 0
max_number = 4
while True:
    tu1()

    tu2()

    tu3()

    sleep(30)

    Core.close_result()

    current_number = Core.check_and_eat_apple(Apple.SILVER, current_number, max_number)

    Core.select_friend()
