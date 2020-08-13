"""
可迭代对象：列表，元组，字符串，字典，range()
不可迭代对象： 100(值)和自定义的myclass（类）
当myclass定义了__iter__方法后，myclass才是一个迭代对象

判断是否可迭代：isinstance((判断对象), Iterable)
可迭代对象的本质：对象所属类中是否包含__iter__（）方法

"""

from collections.abc import Iterable


class MyClass(object):
    def __iter__(self):
        pass
    pass


t = isinstance([1, 2, 3], Iterable)
print(t)
print("-" * 20)

t = isinstance((1, 2, 3), Iterable)
print(t)
print("-" * 20)

t = isinstance("hello", Iterable)
print(t)
print("-" * 20)

t = isinstance({"name": "Bob", "age": 18}, Iterable)
print(t)
print("-" * 20)

myclass = MyClass()
t = isinstance(myclass, Iterable)
print(t)
print("-" * 20)

t = isinstance(100, Iterable)
print(t)
print("-" * 20)