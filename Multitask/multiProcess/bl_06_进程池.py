"""
1.创建一个函数，模拟文件的拷贝
2.创建一个进程池
3.用同步的方式执行
4.用异步的方式执行

"""
import time
import multiprocessing


def copy_task():
    print("文件拷贝中...." , multiprocessing.current_process())
    time.sleep(0.5)


if __name__ == '__main__':
    # 创建进程池
    # pool = multiprocessing.Pool(2)  # 2 表示进程池最多存在两个进程
    pool = multiprocessing.Pool(3)

    for i in range(10):
        # 1.同步执行 .apply(函数名，(参数1，...))
        # 进程池中的进程一个执行完毕后，另一个在进行，多个进程之间有先后顺序
        # pool.apply(copy_task)

        # 2.异步执行 .apply_async()
        # 多个进程同步执行，没有先后顺序
        # 注意：
        # 1> pool.close()表示不再接收新的任务
        # 2> pool.join()让主进程等待子进程执行完再结束
        pool.apply_async(copy_task)

    # 1> pool.close()表示不再接收新的任务
    pool.close()
    # 2> pool.join()让主进程等待子进程执行完再结束
    pool.join()