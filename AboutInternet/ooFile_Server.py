"""
服务端书写思路
1、导⼊模块
2、创建套接字
3、绑定地址和端⼝
4、开始监听，设置套接字为被动监听模式
5、等待客户端连接（如果有新客户端连接，会创建新的套接字)
6、接收客户端发来的⽂件名
7、根据⽂件名读取⽂件数据
8、把读取的⽂件数据发送给客户端（循环）
9、关闭和客户端的连接
10、关闭服务器
"""
# 1、导⼊模块
import socket

# 2、创建套接字
ooFile_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3、绑定地址和端⼝
# 输入IP地址号和端口号
my_ip = input("请输入IP地址（默认为本机）：")
if len(my_ip) == 0:
    my_ip = ""
my_port = input("开放的端口(默认8080)：")
if len(my_port) == 0:
    my_port = 8080

ooFile_server_socket.bind((my_ip, int(my_port)))
# 4、开始监听，设置套接字为被动监听模式
ooFile_server_socket.listen(128)
while True:
    # 5、等待客户端连接（如果有新客户端连接，会创建新的套接字)
    new_server_socket, client_ip_port = ooFile_server_socket.accept()
    print("欢迎【%s】" % str(client_ip_port))
    # 6、接收客户端发来的⽂件名
    new_server_date = new_server_socket.recv(1024)
    file_name = new_server_date.decode("GBK")
    try:
        # 7、根据⽂件名读取⽂件数据
        with open(file_name, "rb") as file:
             # 8、把读取的⽂件数据发送给客户端（循环）
             while True:
                file_date = file.read(1024)
                if file_date:
                    new_server_socket.send(file_date)
                else:
                    break
    except Exception as e:
        print("文件[%s]下载失败" % file_name)
    else:
        print("文件[%s]下载成功" % file_name)
    # 9、关闭和客户端的连接
    new_server_socket.close()
# 10、关闭服务器
ooFile_server_socket.close()
