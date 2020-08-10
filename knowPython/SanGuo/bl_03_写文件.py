# 1.打开文件
# file = open("README", "w")  # w 覆盖原有文件写入
file = open("README", "a")  # a 在末尾追加
# 2.写入文件
file.write("hello ")
# 3.关闭文件
file.close()