import time
import threading


def work():
    for i in range(10):
        print("工作中.....", i)
        time.sleep(0.5)


def main():
    thread_work = threading.Thread(target=work)
    # 线程守护，约定当主线程结束，子线程也结束
    thread_work.setDaemon(True)  # True 表示 子线程守护主线程
    thread_work.start()

    # 主线程睡眠2s后死亡
    time.sleep(2)
    print("Game over !!")
    exit()


if __name__ == '__main__':
    main()