class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def sleep(self):
        print("睡")

    def run(self):
        print("跑")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def bark(self):
        # 对父类进行重写
        print("神一样的叫换......")
        # super(). 对父类进行扩展
        super().bark()
        print("%$%$%$%$%$%")


dog = XiaoTianQuan()
dog.eat()
dog.drink()
dog.run()
dog.sleep()
dog.bark()
