"""
重写__init__时要记得调用父类方法
在调用的.start()方法中，包含有调用.run()方法

"""

import time
import threading


class MyThread(threading.Thread):
    def __init__(self, num):
        # 调用父类方法
        super().__init__()
        self.num = num

    def run(self):
        for i in range(10):
            print("run方法调用中...", self.name, self.num)
            time.sleep(0.5)


def main():
    my_thread = MyThread(num=100)
    my_thread.start()


if __name__ == '__main__':
    main()