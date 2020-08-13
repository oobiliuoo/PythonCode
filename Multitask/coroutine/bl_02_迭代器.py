"""
iter()获取迭代器
next()获取下一个元素值

"""

mlist = [1, 2, 3]

list_iter = iter(mlist)
for i in range(3):
    print(next(list_iter))