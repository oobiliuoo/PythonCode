"""
1.导入multiprocessing模块
2.创建进程对象
3.启动子进程

"""
import time
import multiprocessing


def work1():
    for i in range(10):
        print("正在运行 work1...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建进程对象
    obj_process = multiprocessing.Process(target=work1)
    # 启动进程
    obj_process.start()