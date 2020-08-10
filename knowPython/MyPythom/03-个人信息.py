
"""
* 定义变量保存小明的个人信息
* 姓名：**小明**
* 年龄：**18** 岁
* 性别：**是**男生
* 身高：**1.75** 米
* 体重：**75.0** 公斤

"""

name = "小明"
age = 18
num = 1
sex = "男"
height = 1.75
weight = 75.0
# print(type(name))
"""
name = input("姓名")
print("修改后%s" % name)
"""
age = float(input("年龄："))
print(age)
print("%.02f" % height)
# 输出0000001
print("%06d" % num)