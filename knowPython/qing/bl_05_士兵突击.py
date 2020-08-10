class Gun:
    """枪类"""
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def __str__(self):
        return "型号：%s" % self.model

    def add_bullet(self, count):
        self.bullet_count = count
        print("装弹%d发完毕" % self.bullet_count)

    def shut(self):
        if self.bullet_count <= 0:
            print("请先装子弹!")
            return
        print("射出一颗子弹！嗒嗒嗒")
        self.bullet_count -= 1


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def __str__(self):
        return "士兵：%s 佩枪 %s 报道！" % (self.name, self.gun.model)

    def fire(self):
        if self.gun is None:
            print("没有枪！")
            return
        print("冲阿......【%s】" % self.name)

        self.gun.add_bullet(50)

        self.gun.shut()


ak47 = Gun("AK-47")
xusanduo = Soldier("许三多", ak47)
print(xusanduo)
xusanduo.fire()

