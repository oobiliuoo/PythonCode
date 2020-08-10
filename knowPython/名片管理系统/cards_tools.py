# 记录所以名片
card_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print(" " * 8, end="1. 新增名片\n")
    print(" " * 8, end="2. 显示名片\n")
    print(" " * 8, end="3. 查询名片\n")
    print(" " * 8, end="0. 退出系统\n")
    print("")


def add_card():
    """新赠名片"""
    print("-" * 50)
    name_str = input("清输入姓名：")
    phone_str = input("清输入电话：")
    qq_str = input("清输入QQ：")
    email_str = input("清输入邮箱：")

    card_dist = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    card_list.append(card_dist)

    print("添加名片成功")
    pass


def show_all():
    """显示名片"""
    print("-" * 50)
    if len(card_list) == 0:
        print("当前没有任何记录")
        return
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))


def find_card():
    """查询名片"""
    print("-" * 50)
    find_name = input("请输入要搜索的姓名")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("没有找到此人")


def deal_card(find_dict):
    action_str = input("请选择要执行的操作 "
                       "[1] 修改 [2] 删除 [0] 返回")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱")
        print("修改成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功")
        pass


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 查找到的名片
    :param tip_message: 提示信息
    :return: 修改后的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
