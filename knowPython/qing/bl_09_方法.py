class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1

    @classmethod # 标志下面的为类方法
    def show_count(cls):
        print("工具的总数量：%d" % cls.count)

    @staticmethod # 标志下面为静态方法
    def show():
        print("工具来自留梦泽工作室")


tool1 = Tool("斧头")
tool2 = Tool("扳手")
tool3 = Tool("螺丝刀")

Tool.show_count()
# tool2.__show_count()

Tool.show()