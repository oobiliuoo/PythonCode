"""


"""


class Fibonacci(object):
    """解决斐波那契数列的迭代器"""
    def __init__(self, num):

        # 1.定义实例属性，保存数列的最大列数
        self.num = num

        # 2.定义实例属性，保存当前迭代器的位置
        self.current_index = 0

        # 3.定义数列的第一，二列
        self.a = 1
        self.b = 1

    def __iter__(self):
        # 返回自己
        return self

    def __next__(self):

        # 1.判断是否超出最大列数
        if self.current_index < self.num:
            # 1>进行数据交换
            # 实现方法 a=b, b=a+b
            date = self.a

            self.a, self.b = self.b, self.a + self.b

            # 2>当前下标+1
            self.current_index += 1

            return date
        else:
            raise StopIteration


if __name__ == '__main__':
    fibo = Fibonacci(10)

    # 迭代器本身又是一个迭代器
    for value in fibo:
        print(value)

    # for i in range(10):
    #     fibo_iter = iter(fibo)
    #     value = next(fibo_iter)
    #     print(value)
