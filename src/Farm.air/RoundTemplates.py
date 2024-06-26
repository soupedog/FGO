import MasterControl
import ProcessControl
import ServantControl


def 达芬奇QP冲浪():
    # 一面
    ProcessControl.block_to_area_ready()
    ServantControl.skill(1, 1, None)

    ServantControl.skill(2, 1, None)
    ServantControl.skill(2, 2, 1)
    ServantControl.skill(2, 3, 1)

    ServantControl.skill(3, 1, None)
    ServantControl.skill(3, 2, 1)
    ServantControl.skill(3, 3, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 二面
    ProcessControl.block_to_area_ready()
    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 三面
    ProcessControl.block_to_area_ready()
    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)


def 宇宙凛狗粮冲浪():
    # 一面
    ProcessControl.block_to_area_ready()
    ServantControl.skill(1, 1, None)
    ServantControl.skill(1, 3, None)

    ServantControl.skill(2, 3, 1)

    ServantControl.skill(3, 3, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 二面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(2, 1, None)
    ServantControl.skill(2, 2, 1)

    ServantControl.skill(3, 2, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 三面
    ProcessControl.block_to_area_ready()

    # 宇宙凛 2 技能选蓝卡宝具
    ServantControl.skill(1, 2, 2)

    MasterControl.master_skill(1, None)

    ServantControl.skill(3, 1, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)


# 晕人服限定
def 大英雄狂娜双杀狐():
    # 一面
    ProcessControl.block_to_area_ready()
    ServantControl.skill(1, 3, None)

    MasterControl.master_skill(1, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 二面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(1, 1, None)
    ServantControl.skill(1, 2, None)

    ServantControl.skill(2, 3, 1)

    ServantControl.skill(3, 3, 1)

    # MasterControl.master_skill(1, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 三面
    ProcessControl.block_to_area_ready()

    # 1 号位晕眩
    # MasterControl.change_enemy(1)
    # MasterControl.master_skill(2, None)

    ServantControl.skill(2, 1, 1)
    # ServantControl.skill(2, 2, 1)

    ServantControl.skill(3, 1, 1)
    # ServantControl.skill(3, 2, 1)

    ServantControl.skill(1, 1, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)


def 狂娜双杀狐奥伯龙():
    # 一面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(1, 1, None)
    ServantControl.skill(1, 2, None)

    ServantControl.skill(2, 3, 1)
    ServantControl.skill(3, 3, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 二面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(2, 1, 1)
    # ServantControl.skill(2, 2, 1)

    ServantControl.skill(3, 1, 1)
    # ServantControl.skill(3, 2, 1)

    ServantControl.skill(1, 1, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 三面
    ProcessControl.block_to_area_ready()

    MasterControl.change_my_servant(3, 2, 6)

    ServantControl.skill(1, 2, None)

    ServantControl.skill(2, 1, None)
    ServantControl.skill(2, 2, 1)
    ServantControl.skill(2, 3, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)


def 摩根宝石翁双杀狐():
    # 一面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(2, 3, 1)
    ServantControl.skill(3, 3, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 二面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(1, 1, None)
    ServantControl.skill(1, 2, 1)

    ServantControl.skill(2, 1, 1)
    ServantControl.skill(2, 2, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 三面
    ProcessControl.block_to_area_ready()

    MasterControl.master_skill(2, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)

# cd 服限定
def 月姬双杀狐():
    # 一面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(1, 1, None)
    ServantControl.skill(1, 2, None)

    ServantControl.skill(2, 3, 1)
    ServantControl.skill(3, 3, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 二面
    ProcessControl.block_to_area_ready()

    ServantControl.skill(2, 1, 1)
    ServantControl.skill(3, 1, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 三面
    ProcessControl.block_to_area_ready()

    # 减 cd
    MasterControl.master_skill(3, 1)

    ServantControl.skill(1, 1, None)
    ServantControl.skill(1, 2, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)


def 一面自启动换人狂娜双杀狐():
    # 一面
    ProcessControl.block_to_area_ready()
    ServantControl.skill(1, 1, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 二面
    ProcessControl.block_to_area_ready()

    MasterControl.change_my_servant(3, 1, 4)

    ServantControl.skill(1, 1, None)
    ServantControl.skill(1, 2, None)

    ServantControl.skill(2, 3, 1)

    ServantControl.skill(3, 3, 1)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
    # 三面
    ProcessControl.block_to_area_ready()

    # 2 号位晕眩
    MasterControl.change_enemy(2)
    MasterControl.master_skill(2, None)

    ServantControl.skill(2, 1, 1)
    ServantControl.skill(2, 2, 1)

    ServantControl.skill(3, 1, 1)
    ServantControl.skill(3, 2, 1)

    ServantControl.skill(1, 1, None)

    ServantControl.start_attack()
    ServantControl.attack_single_ultimate_combo(1)
