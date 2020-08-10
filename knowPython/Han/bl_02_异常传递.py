def test01():
    return int(input("请输入一个整数"))


def test02():
    return test01()


try:
    print(test02())
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)

