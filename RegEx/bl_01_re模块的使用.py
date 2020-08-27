"""
1.导入模块
2.通过match()方法，验证正则
3.判断验证是否成功
4.如果成功，获取匹配结果

"""

# 1.导入模块
import re


# 2.通过match()方法，验证正则
# re.match(正则表达式, 要验证的字符串)
# 如果验证成功，返回一个match object 的对象
# 如果验证失败，返回None
result = re.match("\w{4,20}@163\.com$", "hello@163.com")
# 3.判断验证是否成功
if result:
    # 4.如果成功，获取匹配结果
    print("匹配成功")
    print("匹配结果：", result.group())

else:
    print("匹配失败")
