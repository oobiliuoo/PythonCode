def multiple_table():
    """ 九九乘法表"""
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            sum = i * j
            print("%d * %d = %d" % (j, i, sum), end="\t")
            j += 1
        print()
        i += 1


name = "heima"


def text(num, num2):
    """
    text gon neng
    :param num: 1
    :param num2: 2
    """
    num = num2
