"""
引用分组
\num（分组号）
"""
import re
# 由于\有其他意思，在单纯想表达\时，需使用\\
# \1表示引用第一个分组，使其保持一致
# result = re.match("<([a-zA-Z0-9]+)>.*</\\1>", "<html>asdasvnbahishn</html>")

result = re.match("<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>", "<html><h1>asdasvnbahishn</h1></html>")
if result:
    print("success !")
    print("The all:", result.group())

else:
    print("fail")
