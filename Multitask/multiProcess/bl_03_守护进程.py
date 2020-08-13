import time
import multiprocessing


def work1():
    for i in range(10):
        print("正在运行 work1...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建进程对象
    obj_process = multiprocessing.Process(target=work1)
    # 方法1.守护主进程
    obj_process.daemon = True
    # 启动进程
    obj_process.start()
    # 结束主进程
    time.sleep(2)
    print("我要死")
    # 方法2.终止子进程的执行
    obj_process.terminate()
    exit()
