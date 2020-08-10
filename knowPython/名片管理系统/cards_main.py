#! /usr/bin/python3.8
import cards_tools
while True:

    # 显示功能菜单
    cards_tools.show_menu()
    choise = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】"% choise)
    # 1,2,3针对名片的操作
    if choise in ["1", "2", "3"]:
        # 新增名片
        if choise == "1":
            cards_tools.add_card()
        #  显示名片
        elif choise == "2":
            cards_tools.show_all()
        #  查询名片
        elif choise == "3":
            cards_tools.find_card()

        # pass 表示占位符，能够保证程序的代码结构正确
        # 程序运行时，pass 关键字不会做任何操作
    # TODO 退出系统
    elif choise == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    else:
        print("您输入的不正确，请重新选择")
