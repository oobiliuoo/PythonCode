"""
age = 18
if age >= 18:
    print("成年")
    print("可以快乐")
else:
    print("未成年")
"""

"""
# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
age = int(input("你多大了？"))
if 18 <= age <= 120:
    print("成年了，可以快乐")
    print("have a good time")
else:
    print("go back ")
"""

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
python_score = int(input("python score: "))
c_score = int(input("c score:"))
if python_score >= 60 and c_score >= 60:
    print("pass")
else:
    print("out")