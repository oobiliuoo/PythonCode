# 从模块中导入某个工具
# from 模块名1 import 工具名 ( * 表示导入全部工具)
# 导入后不需要通过模块名调用
# 可以直接使用的 模块提供的工具--全局变量、函数、类
# 注意
# 如果两个不同的模块中存在同名函数 会调用后导入的模块中的函数
# 起别名可解决此问题

from bl_11_测试模块1 import Dog
from bl_12_测试模块2 import say_hello
from bl_12_测试模块2 import say_hello as module2_say_hello
from bl_11_测试模块1 import say_hello

dog = Dog()
print(dog)

module2_say_hello()
say_hello()