# 单例设计模式 单例类
# 只有唯一的一个类对象


class MusicPlayer(object):

    # 记录第一个创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flog = False

    def __new__(cls, *args, **kwargs):
        print("new调用")
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3. 返回类属性保存的地址
        return cls.instance

    def __init__(self):

        # 1. 判断是否执行过初始化动作
        if MusicPlayer.init_flog is True:
            return
        # 2. 如果没执行过，执行初始化动作
        print("初始化对象")

        # 3. 修改标记为真
        MusicPlayer.init_flog = True


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)