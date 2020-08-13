import time
import os
import multiprocessing


def work1():
    for i in range(10):
        # 获取子进程名
        # print("正在运行 work1...", multiprocessing.process.current_process(),
        # multiprocessing.process.current_process().pid)
        # 获取进程的父id
        print("正在运行 work1...：", os.getpid(), "this->父id", os.getppid())
        time.sleep(0.5)


if __name__ == '__main__':
    # 获取主进程名称
    print(multiprocessing.process.current_process())
    # 获取主进程PID process id --> pid
    # 1>方法一 调用.pid直接获取
    # print("主进程pid:", multiprocessing.process.current_process().pid)
    # 2>方法二 调用os模块的.getpid()方法获取
    print("主进程编号：", os.getpid())
    # 创建进程对象 name :指定进程名
    obj_process = multiprocessing.Process(target=work1, name="P1")
    # 启动进程
    obj_process.start()
