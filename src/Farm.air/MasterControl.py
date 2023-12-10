# -*- encoding=utf8 -*-
__author__ = "Xavier"

from airtest.core.api import *

import ProcessControl


def change_enemy(index):
    sleep(0.5)

    if index == 1:
        touch((50, 50))
    if index == 2:
        touch((300, 50))
    if index == 3:
        touch((550, 50))

    sleep(0.5)


def master_skill(index, target):
    touch((1190, 310))
    sleep(0.5)

    if index == 1:
        touch((900, 310))
    if index == 2:
        touch((990, 310))
    if index == 3:
        touch((1080, 310))

    # 等待确认按钮
    conform_button = wait(
        Template(r"技能_决定.png", record_pos=(0.165, 0.049), resolution=(1280, 720))
    )
    touch(conform_button)

    if target is not None:
        sleep(0.5)
        if target == 1:
            touch((340, 450))
        if target == 2:
            touch((630, 450))
        if target == 3:
            touch((960, 450))

    ProcessControl.skip_animation()


def change_my_servant(skill_index, old_servant_index, new_servant_index):
    touch((1190, 310))
    sleep(0.5)

    if skill_index == 1:
        touch((900, 310))
    if skill_index == 2:
        touch((990, 310))
    if skill_index == 3:
        touch((1080, 310))

    # 等待确认按钮
    conform_button = wait(
        Template(r"技能_决定.png", record_pos=(0.165, 0.049), resolution=(1280, 720))
    )
    touch(conform_button)

    old_servant_point_x = 140 + (old_servant_index - 1) * 200
    new_servant_point_x = 140 + (new_servant_index - 1) * 200

    touch((old_servant_point_x, 340))

    sleep(0.5)

    touch((new_servant_point_x, 340))

    change_button = wait(
        Template(r"技能_进行更替.png", record_pos=(-0.001, 0.208), resolution=(1280, 720))
    )
    touch(change_button)
    # 等待换人动画
    sleep(8.5)
