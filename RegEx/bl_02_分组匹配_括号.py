

import re

result = re.match("(\d{3,4})-(\d{7,8})", "0121-1234567")

if result:
    print("success !")
    print("The all:", result.group())  # 默认提取全部
    print("The area number:", result.group(1))  # 提取第一个括号内容
    print("The tel number:", result.group(2))  # 提取第二个括号内容

else:
    print("fail")