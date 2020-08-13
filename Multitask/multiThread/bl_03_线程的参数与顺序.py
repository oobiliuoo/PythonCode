import threading
import time


def sing(a, b, c):
    for i in range(5):
        print("%s,%s,%s正在唱歌..." % (a, b, c))
        time.sleep(0.5)


def dance():
    for i in range(5):
        print("正在跳舞......")
        time.sleep(0.5)


def main():
    # 线程中，传参数有三种方式：
    # 方式一：元组传递
    # threading.Thread(target=函数名, args=(参数1， 参数2， ...))
    # thread_sing = threading.Thread(target=sing, args=("a", "b", "c"))
    # 方式二：字典传递
    # threading.Thread(target=函数名, kwargs={"key":value,....})
    # thread_sing = threading.Thread(target=sing, kwargs={"a": "a2", "b": "b2", "c": "c2"})
    # 方式三：混合元组和字典
    # threading.Thread(target=函数名, kwargs={"key":value,....}, kwargs={"key":value,....})
    thread_sing = threading.Thread(target=sing, args=("a3", ), kwargs={"c":"c3", "b":"b3"})
    thread_dance = threading.Thread(target=dance)

    thread_sing.start()
    thread_dance.start()


if __name__ == '__main__':
    main()
