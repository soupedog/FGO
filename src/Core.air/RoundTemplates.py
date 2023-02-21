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
