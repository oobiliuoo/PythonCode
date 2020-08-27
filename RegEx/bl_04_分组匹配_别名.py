"""
给分组起别名
(?P<name>)
使用别名
(?P=name)
"""
import re

result = re.match("<(?P<name1>[a-zA-Z0-9]+)><(?P<name2>[a-zA-Z0-9]+)>.*</(?P=name2)></(?P=name2)>", "<html><h1>asdasvnbahishn</h1></html>")
if result:
    print("success !")
    print("The all:", result.group())

else:
    print("fail")
