"""
1.创建一个生成器
    目标：实现斐波那契数列
    1>定义变量保存第一列，第二列的值
    2>定义变量保存当前生成器的位置
    3>循环生存数据 条件 （当前位置 < 最大列数）
    4>保存a的值
    5>修改a/b的值 （a=b,b=a+b)
    6>返回a的值 yield

2.定义变量保存生成器
3.next()得到下一个元素的值
"""


def febonacci(num):
    max_num = num  # 最大列数
    a = 1  # 第一列
    b = 1  # 第二列
    index = 0  # 当前生成器位置
    while index < max_num:
        date = a
        a, b = b, a + b
        index += 1
        # yield 能充当return 返回结果
        # 还能保存程序当前状态，暂停程序执行
        # 下一次从yield 向下执行
        yield date
        print("-" * index)


if __name__ == '__main__':

    febo = febonacci(10)
    i = 1
    for value in febo:
        print("第%d列 ：%d" % (i, value))
        i += 1
