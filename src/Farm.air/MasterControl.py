# -*- encoding=utf8 -*-
__author__ = "Xavier"

from airtest.core.api import *


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
    conform_button = wait(Template(r"技能_决定.png", record_pos=(0.165, 0.049), resolution=(1280, 720)))
    touch(conform_button)

    if target is not None:
        sleep(0.5)
        if target == 1:
            touch((340, 450))
        if target == 2:
            touch((630, 450))
        if target == 3:
            touch((960, 450))

    # 等待技能动画
    sleep(3.5)


def change_my_servant(old_index, new_index):
    old_point_x = 140 + (old_index - 1) * 200
    new_point_x = 140 + (new_index - 1) * 200

    touch((old_point_x, 340))

    sleep(0.5)

    touch((new_point_x, 340))

    change_button = wait(Template(r"技能_进行更替.png", record_pos=(-0.001, 0.208), resolution=(1280, 720)))
    touch(change_button)
    # 等待换人动画
    sleep(3.5)
