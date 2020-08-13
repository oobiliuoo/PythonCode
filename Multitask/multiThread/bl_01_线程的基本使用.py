"""
子线程的创建步骤
1.导入threading模块
2.使用threading.Thread()定义一个子线程对象
3.指定子线程执行的分支
4.使用 .start（）方法，启动子线程

"""

import time
import threading


def say_sorry():
    print("对不起，我错了...")
    time.sleep(0.5)


def main():
    for i in range(5):
        # 2.使用threading.Thread()定义一个子线程对象
        # 3.指定子线程执行的分支
        # threading.Thread(target=saySorry)
        thread_obj = threading.Thread(target=say_sorry)
        # 4.使用.start（）方法，启动子线程
        # 线程对象只有调用了start()反法才会执行
        thread_obj.start()
        # say_sorry()

    print("xxx")


if __name__ == '__main__':
    main()