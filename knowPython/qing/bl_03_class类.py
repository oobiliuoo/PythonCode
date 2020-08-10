""""
需求**

1. **小明** **体重** `75.0` 公斤
2. 小明每次 **跑步** 会减肥 `0.5` 公斤
3. 小明每次 **吃东西** 体重增加 `1` 公斤
"""


class Person:
    """人类"""
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫：%s, 我的体重是：%.2f" % (self.name,
                                               self.weight)

    def run(self):
        """跑步"""
        print("%s跑步中" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s吃饭中" % self.name)
        self.weight += 1


xiaoming = Person("xiaoming", 50)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
print(xiaoming)