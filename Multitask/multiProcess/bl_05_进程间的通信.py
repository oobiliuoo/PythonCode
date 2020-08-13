"""
1.准备两个进程
2.准备一个队列
3.一个进行写入
4.一个进行读取

"""
import multiprocessing
import time


def write_queue(msg_queue):
    """向队列中写入数据"""
    for i in range(5):

        if msg_queue.full():
            print("this queue is full ! ")
            break

        msg_queue.put(i)
        print("write success the value:", i)
        time.sleep(0.5)


def read_queue(msg_queue):
    """读取队列中的数据"""
    for i in range(5):

        if msg_queue.empty():
            print("this queue is empty ！")
            break

        value = msg_queue.get()
        print("read the value :", value)
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建消息队列
    msg_queue = multiprocessing.Queue(5)

    # 创建进程
    obj_write_process = multiprocessing.Process(target=write_queue, args=(msg_queue, ))
    obj_read_process = multiprocessing.Process(target=read_queue, args=(msg_queue, ))

    obj_write_process.start()

    # 优先要写的进程完成
    obj_write_process.join()
    
    obj_read_process.start()