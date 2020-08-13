"""
gevent模块实现协程的步骤
1.导入模块
2.创建任务 work1 work2
3.创建gevent对象
4.主线程等待

"""
from gevent import monkey
monkey.patch_all()

import time
import gevent


def work1():
    while True:
        # gevent.getcurrent()获取当前正在执行的协程
        print("work1正在工作----", gevent.getcurrent())
        # tiem.sleep()不能被gevent自动识别
        time.sleep(0.5)
        # 方法一：可采用gevent.sleep()来解决
        # gevent.sleep(0.5)
        # 方法二：打补丁 目的：让gevent识别time.sleep()
        # 打补丁：在不修改程序源代码的情况下给代码添加新功能
        # 如何打补丁：
        # 1>导入模块 from gevent import monkey
        # 2>破解 monkey.patch_all()


def work2():
    while True:
        print("work2正在工作---- ***8***")
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建对象 gevent.spawn(函数名,参数1,....)
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # 主进程等待任务执行完
    g1.join()
    g2.join()


