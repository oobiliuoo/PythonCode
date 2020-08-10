# 目标**
#
# 1. 强化 **多个条件** 的 **逻辑运算**
# 2. 体会 `import` 导入模块（“工具包”）的使用
#
# **需求**
#
# 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 2. 电脑 **随机** 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 3. 比较胜负
import random
player = int(input("请输入拳头：石头（1） 剪刀（2） 布（3）"))
computer = random.randint(1, 3)
print("玩家出的：%d  电脑出的: %d" % (player, computer))
if ((player == 1 and computer == 2)
         or (player == 2 and computer == 3)
         or (player == 3 and computer == 1)):

    print("噢耶，电脑弱爆了！")
elif player == computer:
    print("平局")
else:
    print("不服气，决战到天亮")