# -*- encoding=utf8 -*-
__author__ = "Xavier"

from airtest.core.api import *

from entity.Apple import Apple


def check_and_eat_apple(apple: Apple, previous_number, max_number) -> int:
    if apple == Apple.GOLDEN:
        target = exists(Template(r"tpl1657429122818.png", threshold=0.8, rgb=True, record_pos=(-0.209, -0.032),
                                 resolution=(1280, 720)))
    elif apple == Apple.SILVER:
        target = exists(Template(r"tpl1657429219391.png", threshold=0.8, rgb=True, record_pos=(-0.209, 0.084),
                                 resolution=(1280, 720)))
    else:
        raise Exception("苹果请使用 Apple 枚举，并且目前不支持铜苹果")

    result = previous_number
    if target:
        if previous_number >= max_number:
            raise Exception("已到达最大苹果限制 %s" % previous_number)
        sleep(1)
        touch(target)
        conform_button = wait(Template(r"tpl1657430567355.png", record_pos=(0.155, 0.159), resolution=(1280, 720)))
        sleep(1)
        touch(conform_button)

        result = previous_number + 1
        print("吃掉了一个 %s,共计已吃 %d 个苹果" % (apple.value, result))
    return result


def select_friend():
    while True:
        friend = exists(Template(r"I_杀狐_羁绊.png", record_pos=(-0.379, -0.057), resolution=(1280, 720)))

        if friend:
            touch(friend)
            break
        else:
            refresh_button = exists(Template(r"I_好友列表更新.png", record_pos=(0.227, -0.18), resolution=(1280, 720)))

            if refresh_button:
                touch(refresh_button)
                conform_button = wait(
                    Template(r"tpl1657431120364.png", record_pos=(0.154, 0.159), resolution=(1280, 720)))
                touch(conform_button)
            else:
                sleep(10)


def block_to_area_ready():
    wait(Template(r"tpl1657024928260.png", record_pos=(0.384, 0.15), resolution=(1280, 720)), timeout=60, interval=5)
    sleep(5)
    print("关卡就绪", flush=True)


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

    # 等待确认按钮
    conform_button = wait(Template(r"tpl1657431874530.png", record_pos=(0.166, 0.05), resolution=(1280, 720)))
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
    conform_button = wait(Template(r"tpl1657432488231.png", record_pos=(0.165, 0.049), resolution=(1280, 720)))
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

    change_button = wait(Template(r"tpl1657029847683.png", record_pos=(-0.001, 0.208), resolution=(1280, 720)))
    touch(change_button)
    # 等待换人动画
    sleep(3.5)


def start_attack():
    touch(Template(r"tpl1657024928260.png", record_pos=(0.384, 0.15), resolution=(1280, 720)))
    # 等待攻击取消按钮
    wait(Template(r"tpl1657027469724.png", record_pos=(0.436, 0.25), resolution=(1280, 720)))


def attack_ultimate(servant):
    if servant == 1:
        touch((400, 200))
    if servant == 2:
        touch((640, 200))
    if servant == 3:
        touch((850, 200))

    sleep(0.5)


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

    sleep(0.5)


def attack_single_ultimate_combo(target):
    attack_ultimate(target)
    attack_card(1)
    attack_card(2)


def close_result():
    qian_ban = wait(Template(r"tpl1657444470564.png", record_pos=(-0.351, -0.134), resolution=(1280, 720)), timeout=60,
                    interval=5)
    sleep(1)
    touch(qian_ban)
    exp = wait(Template(r"tpl1657444527697.png", record_pos=(0.08, -0.118), resolution=(1280, 720)))
    sleep(1)
    touch(exp)
    next_button = wait(Template(r"tpl1657434537493.png", record_pos=(0.366, 0.217), resolution=(1280, 720)))
    sleep(1)
    touch(next_button)
    continue_button = wait(Template(r"tpl1657434574237.png", record_pos=(0.155, 0.16), resolution=(1280, 720)))
    sleep(1)
    touch(continue_button)
