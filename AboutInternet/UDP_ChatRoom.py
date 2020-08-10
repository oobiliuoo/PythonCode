import socket


def send_msg(udp_socket):
    """发送信息"""
    # 1.输入要发送到的IP和端口
    m_ip = input("请输入要发送到的IP号：")
    if len(m_ip) == 0:
        m_ip = "192.168.43.131"
        print("默认为%s" % m_ip)
    m_dk = input("端口号：")
    if len(m_dk) == 0:
        m_dk = 8080
        print("默认为%s" % m_dk)
    # 2.输入要发送的内容
    m_text = input("清输入要发送的内容：")
    # 3.对输入内容进行编码
    text = m_text.encode()
    # 4.发送信息
    udp_socket.sendto(text, (m_ip, int(m_dk)))
    print("信息发送中...")
    print("发送成功！")


def recv_msg(udp_socket):
    """接收信息"""
    # 1.接收信息
    recv_text = udp_socket.recvfrom(1024)
    # 2.解码信息
    text = recv_text[0].decode()
    address = recv_text[1]
    # 3.显示信息
    print("接受到来自【%s】【%d】的信息" % (address[0], address[1]))
    print("信息内容：%s" % text)


def main_menu():
    """菜单界面"""
    print("")
    print("*" * 25)
    print("     1.发送信息")
    print("     2.接收信息")
    print("     0.退出系统")
    print("*" * 25)


def main():
    """主程序"""
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口
    udp_socket.bind(("", 8080))
    while True:
        # 3.菜单界面
        main_menu()
        # 4.功能选择
        choise = input("请选择功能：")
        if choise == "1":
            send_msg(udp_socket)
        elif choise == "2":
            recv_msg(udp_socket)
        elif choise == "0":
            break
        else:
            print("输入有误，请重新输入")

    # 5.关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()