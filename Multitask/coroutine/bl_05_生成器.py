"""
生成器本身是一个特殊的迭代器
生成器的创建方法：
一：列表推导式
二：函数使用yield返回

"""

# 列表推导式
list1 = [i * 2 for i in range(10)]
print(list1, end=" ")

# 创建生成器
# 方法一:列表推导式
list2 = (i * 2 for i in range(10))
print("")
print(list2)
value = next(list2)
print("--->", value)

# 方法二：函数返回yield
print("*" * 50)


def test():
    return 10


print(test())


def test2():
    yield 10


value = test2()
print(value)
print(next(value))


