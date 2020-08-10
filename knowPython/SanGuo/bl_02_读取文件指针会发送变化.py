# 1.打开文件
file = open("README")
# 2.读取文件

text = file.read()
print(text)
print(len(text))

print("-" * 50)
# 由于文件指针🕐已经移动到末尾 故再次读取读不到数据
text = file.read()
print(text)
print(len(text))

# 3.关闭文件
file.close()
