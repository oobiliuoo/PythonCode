
class MyList(object):
    """自定义列表类"""
    def __init__(self):
        """初始化方法"""
        # 定义实例属性，保存数据
        self.my_list = []

    def __iter__(self):
        """对外提供迭代器"""
        mylist_iterable = MyListIterable(self.my_list)
        return mylist_iterable

    def additer(self, value):
        """添加数据"""
        self.my_list.append(value)


class MyListIterable(object):
    """自定义列表迭代器类"""
    def __init__(self, his_list):
        """初始化方法"""
        # 定义实例属性，保存MyList传递过来的值
        self.my_list = his_list

        # 定义实例属性，保存迭代器当前迭代的位置
        self.current_index = 0

    def __iter__(self):
        """迭代器方法"""

        pass

    def __next__(self):
        """提供写一个元素值方法"""
        # 1.判断下标是否越界
        if self.current_index < len(self.my_list):
            # 2.根据下标获取对应元素
            date = self.my_list[self.current_index]
            # 3.当前下标+1
            self.current_index += 1
            # 4.返回获取的值
            return date

        # 如果越界，抛出异常
        else:

            # raise 用于主动抛出异常
            raise StopIteration


if __name__ == '__main__':
    # 创建自定义列表对象
    my_list = MyList()
    my_list.additer("张飞")
    my_list.additer("关羽")
    my_list.additer("刘备")

    # for循环的本质：
    # 1.iter(my_list) 获取迭代器
    # 2.next(迭代器) 获取下一个元素的值
    # 3.捕获异常
    for value in my_list:
        print(value)
