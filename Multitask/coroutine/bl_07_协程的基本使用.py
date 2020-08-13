"""
协程：在不开辟新的线程的基础上实现多任务
协程是一个特殊的生成器


定义两个函数
使用next()反法调用

"""
import time


def work1():
    while True:
        print("work1正在工作----")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("work2正在工作---- ***8***")
        yield
        time.sleep(0.5)


if __name__ == '__main__':
    w1 = work1()
    w2 = work2()

    while True:
        next(w1)
        next(w2)