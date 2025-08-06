# -*- encoding=utf8 -*-
__author__ = "Xavier"

from airtest.core.api import *

import ProcessControl


def start_attack():
    touch(
        Template(r"指令卡_开始攻击.png")
    )
    # 等待攻击取消按钮
    sleep(0.5)


def attack_ultimate(servant):
    if servant == 1:
        touch((400, 200))
    if servant == 2:
        touch((640, 200))
    if servant == 3:
        touch((850, 200))

    sleep(0.25)


def attack_card(target):
    if target == 1:
        touch((120, 500))
    if target == 2:
        touch((400, 500))
    if target == 3:
        touch((650, 500))
    if target == 4:
        touch((900, 500))
    if target == 5:
        touch((1150, 500))

    sleep(0.25)


def attack_single_ultimate_combo(target):
    attack_ultimate(target)
    attack_card(1)
    attack_card(2)
    # 默认宝具动画至少有 5 秒
    sleep(5)


def skill(servant, index, target):
    point_x = 480
    if servant == 1:
        point_x = point_x - 320
    if servant == 3:
        point_x = point_x + 320

    if index == 1:
        point_x = point_x - 90
    if index == 3:
        point_x = point_x + 90

    touch((point_x, 580))

    sleep(0.25)

    if target is not None:
        sleep(0.25)
        if target == 1:
            touch((340, 450))
        if target == 2:
            touch((630, 450))
        if target == 3:
            touch((960, 450))
    # 等待技能动画
    ProcessControl.skip_animation()
