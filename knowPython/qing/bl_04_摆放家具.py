# 需求**
#
# 1. **房子(House)** 有 **户型**、**总面积** 和 **家具名称列表**
#    * 新房子没有任何的家具
# 2. **家具(HouseItem)** 有 **名字** 和 **占地面积**，其中
#    *  **席梦思(bed)** 占地 `4` 平米
#    *  **衣柜(chest)** 占地 `2` 平米
#    *  **餐桌(table)** 占地 `1.5` 平米
# 3. 将以上三件 **家具** **添加** 到 **房子** 中
# 4. 打印房子时，要求输出：**户型**、**总面积**、
#    **剩余面积**、**家具名称列表


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具名称：%s 占地面积: %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s, 总面积: %.2f, 剩余面积：%.2f, 家具：%s"
                % (self.house_type, self.area,
                   self.free_area,self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        if item.area > self.free_area:
            print("%s的面积过大，不能添加到房子" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


def test02():
    my_home = House("两室一厅", 60)
    print(my_home)
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)

    my_home.add_item(bed)
    my_home.add_item(chest)
    my_home.add_item(table)
    print(my_home)


test02()
