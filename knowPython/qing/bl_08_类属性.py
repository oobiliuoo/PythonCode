class Tool(object):
    count = 0

    def __init__(self):
        Tool.count += 1


tool1 = Tool()
tool2 = Tool()
tool3 = Tool()

print(Tool.count)
# 向上查找机制
print(tool1.count)

# 在内部创建了实例属性 不会修改类属性
tool1.count = 99

print(tool1.count)
print(Tool.count)
