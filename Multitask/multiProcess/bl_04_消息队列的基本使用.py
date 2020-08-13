"""
消息队列是multiprocessing模块提供的一个类
1.创建队列
2.放值
3.取值

"""
import multiprocessing
import time

def test01():
    """消息队列的基本使用"""
    # 1.创建队列
    mes_queue = multiprocessing.Queue(5)  # 5 表示队列长度

    # 2.放值
    mes_queue.put(1)
    mes_queue.put("hello")
    mes_queue.put([1, 2, 3])
    mes_queue.put((4, 5, 6))
    mes_queue.put({"a":100, "b":200})

    # 长度为5的队列，放入第6个值后，队列就进入了阻塞状态，
    # 默认会等待队列先取出值在放入新值
    # mes_queue.put(10)

    # put_mowait()放值时，如果队列已满，不再等待，直接报错
    # mes_queue.put_nowait(10)

    # 3.取值
    for i in range(5):
        value = mes_queue.get()
        print(value)
        print("-" * 20)

    print("值都取完拉！")

    # 当值全部取出后，再次取值，程序将会进入阻塞状态
    # 等待放入新值到队列，在取值
    # value2 = mes_queue.get()

    # 当队列已空时，不再等待，直接报错
    value3 = mes_queue.get_nowait()


def test02():
    """
    队列的判断
    1.队列已满
    2.队列以空
    3.取出队列中消息的个数
    """
    msg_queue2 = multiprocessing.Queue(1)

    msg_queue2.put_nowait(1)

    # 判断已满
    is_full = msg_queue2.full()
    print("is full ?-->", is_full)

    # 判断已空
    # 注意：结果有时不对，
    # 可以理解为放值和判断同时进行，造成错误
    # 调用sleep延迟可避免错误
    time.sleep(0.0001)
    is_empty = msg_queue2.empty()
    print("is empty ?-->", is_empty)

    # 取出消息中的个数
    print("num = ", msg_queue2.qsize())


if __name__ == '__main__':
    # test01()
    test02()
