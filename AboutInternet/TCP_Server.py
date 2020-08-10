"""
1.导入模块
2.创建套接字
3.绑定IP和端口
4.开启监听（设置套接字为被动模式）
5.等待客户端连接
6.收发数据
7.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.绑定IP和端口
tcp_server_socket.bind(("", 8080))

# 4.开启监听（设置套接字为被动模式）
# tcp_server_socket.listen(128)
# 方法作用： 设置服务端为被动监听模式，不能主动发送数据
# 128 表示最大连接数 注意：Windows 有效 Linux 无效
tcp_server_socket.listen(128)

# 5.等待客户端连接
# accept(): 开始接受客户端连接
# 进入阻塞状态，等待连接，有连接就解锁
# recv_date 数据有两部分：
# 1.返回了一个新的套接字socket 对象
# 2.客户端的IP地址和端口号 元组
# recv_date = tcp_server_socket.accept()
# 此处while True 为了多用户连接
while True:
    new_server_socket, client_ip_port = tcp_server_socket.accept()
    print("新客户端『%s』上线" % str(client_ip_port))

    while True:
        # 6.收发数据
        new_server_date = new_server_socket.recv(1024)
        new_text = new_server_date.decode("GBK")
        if len(new_text) != 0:
            print("接收到【%s】的信息：【%s】" % (str(client_ip_port), new_text))
        else:
            print("客户端『%s』断开连接" % str(client_ip_port))
            break

    # new_server_socket.close() 表示不再和当前客户端进行通信
    new_server_socket.close()

# 7.关闭套接字 不再接受新的客户端连接，已经连接的可以继续服务
tcp_server_socket.close()




