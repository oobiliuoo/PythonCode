class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("蹦蹦跳跳的玩耍")


class XiaoTianQuan(Dog):
    def game(self):
        print("飞到天上去玩耍")


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dag):
        print("%s和%s一起玩耍" % (self.name, dag.name))
        dag.game()


# wancai = Dog("旺财")
wancai = XiaoTianQuan("飞天旺财")
xiaomin = Person("小明")
xiaomin.game_with_dog(wancai)