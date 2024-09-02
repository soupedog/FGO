# -*- encoding=utf8 -*-
__author__ = "Xavier"

from airtest.core.api import *

import ProcessControl
from entity.Apple import Apple
from entity.Friend import Friend


def check_and_eat_apple(apple: Apple, previous_number, max_number) -> int:
    if apple == Apple.GOLDEN:
        target = exists(
            Template(r"金苹果.png", threshold=0.7, rgb=True, record_pos=(-0.209, -0.032),
                     resolution=(1280, 720))
        )
    elif apple == Apple.SILVER:
        target = exists(
            Template(r"银苹果.png", threshold=0.7, rgb=True, record_pos=(-0.209, 0.084),
                     resolution=(1280, 720))
        )
    elif apple == Apple.BLUE:
        # 下拉条滚动到底部
        sleep(0.5)
        swipe((1000, 200), (1000, 400))
        sleep(0.5)
        target = exists(
            Template(r"蓝苹果.png", threshold=0.7, rgb=True, record_pos=(-0.209, 0.084),
                     resolution=(1280, 720))
        )
    elif apple == Apple.BRONZE:
        # 下拉条滚动到底部
        sleep(0.5)
        swipe((1000, 200), (1000, 400))
        sleep(0.5)
        target = exists(
            Template(r"铜苹果.png", threshold=0.7, rgb=True, record_pos=(-0.209, 0.084),
                     resolution=(1280, 720))
        )
    else:
        raise Exception("苹果请使用 Apple 枚举")

    result = previous_number
    if target:
        if previous_number >= max_number:
            raise Exception("已达苹果食用次数上限(%s 次)" % previous_number)
        sleep(1)
        touch(target)
        conform_button = wait(
            Template(r"体力_苹果决定.png", record_pos=(0.155, 0.159), resolution=(1280, 720))
        )
        sleep(1)
        touch(conform_button)

        result = previous_number + 1
        print("食用了 %s， 共计已食用 %d 次" % (apple.value, result))
        # 吃完苹果，预留时间搜索好友头像
        sleep(1)
    return result


def select_friend(friend_type: Friend):
    while True:
        ProcessControl.skip_system_friend(1)
        if friend_type == Friend.C呆_最终_牵绊:
            friend_image = Template(r"DL_C呆_最终_牵绊.png", threshold=0.80, rgb=True, record_pos=(-0.379, -0.057),
                                    resolution=(1280, 720))
        elif friend_type == Friend.C呆_最终_量子:
            friend_image = Template(r"DL_C呆_最终_量子.png", threshold=0.85, rgb=True, record_pos=(-0.379, -0.057),
                                    resolution=(1280, 720))
        elif friend_type == Friend.C呆_最终_任意:
            friend_image = Template(r"DL_C呆_最终_任意.png", threshold=0.80, rgb=True, record_pos=(-0.379, -0.057),
                                    resolution=(1280, 720))
        elif friend_type == Friend.杀狐_最终_牵绊:
            friend_image = Template(r"DL_杀狐_最终_牵绊.png", threshold=0.85, rgb=True, record_pos=(-0.379, -0.057),
                                    resolution=(1280, 720))
        elif friend_type == Friend.杀狐_最终_任意:
            friend_image = Template(r"DL_杀狐_最终_任意.png", threshold=0.85, rgb=True, record_pos=(-0.379, -0.057),
                                    resolution=(1280, 720))
        else:
            raise Exception("好友助战类型有误")

        friend = exists(friend_image)

        sleep(1)

        if friend:
            touch(friend)
            break
        else:
            refresh_button = exists(
                Template(r"助战_列表更新.png", record_pos=(0.227, -0.18), resolution=(1280, 720))
            )
            sleep(1)
            if refresh_button:
                touch(refresh_button)
                conform_button = wait(
                    Template(r"助战_列表更新确定.png", record_pos=(0.154, 0.159), resolution=(1280, 720))
                )
                sleep(1)
                touch(conform_button)
            else:
                sleep(8)


# 助战选择界面下滚跳过系统助战()
def skip_system_friend(amount):
    # 滚太多容易不是好友无意义，默认最长滚过 5 个
    height = 150

    if amount == 1:
        # 存在最小滚动单位，难以精确控制，实际上是滚过了 2 个位置
        height = 50
    if amount == 2:
        height = 60
    if amount == 3:
        height = 90
    if amount == 4:
        height = 120

    swipe((1250, 200), (1250, 200 + height))
    sleep(1)


def skip_animation():
    sleep(0.25)
    touch((10, 200), times=2)
    sleep(0.25)
    touch((10, 200), times=2)
    sleep(0.5)


def block_to_area_ready():
    wait(
        Template(r"指令卡_开始攻击.png", record_pos=(0.384, 0.15), resolution=(1280, 720)),
        timeout=60, interval=2)
    print("关卡就绪", flush=True)


def close_result(extra_hook):
    qian_ban = wait(
        Template(r"结算_牵绊.png", threshold=0.7, record_pos=(-0.351, -0.134), resolution=(1280, 720)),
        timeout=60, interval=2)
    sleep(1)
    touch(qian_ban)
    exp = wait(
        Template(r"结算_经验.png", threshold=0.7, record_pos=(0.08, -0.118), resolution=(1280, 720))
    )
    sleep(1)
    touch(exp)
    next_button = wait(
        Template(r"结算_下一步.png", threshold=0.7, record_pos=(0.366, 0.217), resolution=(1280, 720))
    )
    sleep(1)
    touch(next_button)

    if extra_hook is None:
        pass
    else:
        # 活动有额外奖励面板需要的额外结算行为
        extra_hook()

    continue_button = wait(
        Template(r"结算_连续出击.png", record_pos=(0.155, 0.16), resolution=(1280, 720))
    )
    sleep(1)
    touch(continue_button)
    sleep(1)
