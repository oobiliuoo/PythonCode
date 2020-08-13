"""
greenlet模块实现协程的步骤
1.导入模块
2.创建任务 work1 work2
3.创建greenlet对象
4.手动switch切换

"""
import time
from greenlet import greenlet


def work1():
    while True:
        print("work1正在工作----")
        time.sleep(0.5)
        # 遇到阻塞，切换任务
        g2.switch()


def work2():
    while True:
        print("work2正在工作---- ***8***")
        time.sleep(0.5)
        g1.switch()


if __name__ == '__main__':
    # 创建对象 greenlet(函数名)
    g1 = greenlet(work1)
    g2 = greenlet(work2)
    # 切换任务
    g1.switch()

