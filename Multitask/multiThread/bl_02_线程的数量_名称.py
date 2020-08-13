import threading


def sing():
    for i in range(5):
        print(threading.current_thread())
        print("正在唱歌...")
        time.sleep(0.5)


def dance():
    for i in range(5):
        print(threading.current_thread())
        print("正在跳舞......")
        time.sleep(0.5)


def main():
    # 获取线程名称
    # (threading.current_thread() 获取当前线程对象，对象中含有名称
    print(threading.current_thread())
    # threading.enumerate()获取活跃的线程列表
    thread_list = threading.enumerate()
    print("1当前线程数：%d" % len(thread_list))

    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)
    thread_list = threading.enumerate()
    print("2当前线程数：%d" % len(thread_list))

    thread_sing.start()
    thread_dance.start()

    # 每0.5秒获取一次线程数
    while True:
        thread_list = threading.enumerate()
        print("3当前线程数：%d" % len(thread_list))
        if len(thread_list) <= 1:
            break

        time.sleep(0.5)


if __name__ == '__main__':
    main()