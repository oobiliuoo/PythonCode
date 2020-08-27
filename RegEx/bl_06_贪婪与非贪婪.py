"""
贪婪：在满足正则的条件下，尽可能多的取内容  默认为贪婪模式
非贪婪：尽可能少的取内容
贪婪改非贪婪：在+ * ？ {} 后面 + ?即可
"""
# 1.导入模块
import re


result = re.match("aaa\d+?", "aaa111")
# 3.判断验证是否成功
if result:
    # 4.如果成功，获取匹配结果
    print("匹配成功")
    print("匹配结果：", result.group())

else:
    print("匹配失败")
