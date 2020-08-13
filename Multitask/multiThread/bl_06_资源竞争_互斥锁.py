"""
1.创建一个互斥锁
2.锁死
3.释放锁

原则：锁的资源尽可能少
"""


import threading
import time

g_num = 0


def work1():
    global g_num
    lock1.acquire()  # 加锁
    for i in range(1000000):

        g_num += 1
    lock1.release()  # 解锁

    print("work1......", g_num)


def work2():
    global g_num
    lock1.acquire()
    for i in range(1000000):
        g_num += 1
    lock1.release()

    print("work2-----", g_num)


if __name__ == '__main__':

    # 创建互斥锁
    lock1 = threading.Lock()

    w1 = threading.Thread(target=work1)
    w2 = threading.Thread(target=work2)

    w1.start()
    # w1.join()  # 表示线程1结束后在调用线程2
    w2.start()

    if len(threading.enumerate()) != 1:
        time.sleep(1)

    print("main ......", g_num)