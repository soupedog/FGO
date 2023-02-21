# -*- encoding=utf8 -*-
__author__ = "Xavier"

from airtest.core.api import *

from entity.Apple import Apple


def check_and_eat_apple(apple: Apple, previous_number, max_number) -> int:
    if apple == Apple.GOLDEN:
        target = exists(Template(r"金苹果.png", threshold=0.8, rgb=True, record_pos=(-0.209, -0.032),
                                 resolution=(1280, 720)))
    elif apple == Apple.SILVER:
        target = exists(Template(r"银苹果.png", threshold=0.8, rgb=True, record_pos=(-0.209, 0.084),
                                 resolution=(1280, 720)))
    else:
        raise Exception("苹果请使用 Apple 枚举，并且目前不支持铜苹果")

    result = previous_number
    if target:
        if previous_number >= max_number:
            raise Exception("已到达最大苹果限制 %s" % previous_number)
        sleep(1)
        touch(target)
        conform_button = wait(Template(r"体力_苹果决定.png", record_pos=(0.155, 0.159), resolution=(1280, 720)))
        sleep(1)
        touch(conform_button)

        result = previous_number + 1
        print("吃掉了一个 %s,共计已吃 %d 个苹果" % (apple.value, result))
    return result


def select_friend():
    while True:
        friend = exists(
            Template(r"DL_C呆_最终_量子.png", threshold=0.85, rgb=True, record_pos=(-0.379, -0.057), resolution=(1280, 720)))
        if friend:
            touch(friend)
            break
        else:
            refresh_button = exists(Template(r"助战_列表更新.png", record_pos=(0.227, -0.18), resolution=(1280, 720)))

            if refresh_button:
                touch(refresh_button)
                conform_button = wait(Template(r"助战_列表更新确定.png", record_pos=(0.154, 0.159), resolution=(1280, 720)))
                sleep(1)
                touch(conform_button)
            else:
                sleep(8)


def block_to_area_ready():
    wait(Template(r"指令卡_开始攻击.png", record_pos=(0.384, 0.15), resolution=(1280, 720)), timeout=60, interval=2)
    sleep(2)
    print("关卡就绪", flush=True)


def close_result():
    qian_ban = wait(Template(r"结算_羁绊.png", record_pos=(-0.351, -0.134), resolution=(1280, 720)), timeout=60,
                    interval=2)
    sleep(1)
    touch(qian_ban)
    exp = wait(Template(r"结算_经验.png", record_pos=(0.08, -0.118), resolution=(1280, 720)))
    sleep(1)
    touch(exp)
    next_button = wait(Template(r"结算_下一步.png", record_pos=(0.366, 0.217), resolution=(1280, 720)))
    sleep(1)
    touch(next_button)
    continue_button = wait(Template(r"结算_连续出击.png", record_pos=(0.155, 0.16), resolution=(1280, 720)))
    sleep(1)
    touch(continue_button)
