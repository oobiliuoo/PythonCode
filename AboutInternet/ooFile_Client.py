"""
目标：./Desktop/PythonCode/AdvancedPython/AboutInternet/123.txt

到 :./Desktop/123.txt

客户端实现思路
1、导⼊模块
2、创建套接字
3、建⽴和服务器的连接
4、接收⽤户输⼊的⽂件名
5、发送⽂件名到服务器端
6、创建⽂件，准备接收服务端返回的⽂件数据
7、保存⽂件数据
8、关闭套接
"""
# 1、导⼊模块
import socket
# 2、创建套接字
ooFile_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3、建⽴和服务器的连接
#  输入服务器ip和端口号
server_ip = input("请输入要连接的IP号：")
if len(server_ip) == 0:
    server_ip = "192.168.43.131"
server_port = input("端口号：")
if len(server_port) == 0:
    server_port = 8080
ooFile_client_socket.connect((server_ip, int(server_port)))

# 4、接收⽤户输⼊的⽂件名
file_name = input("请输入要获取的文件名：")
# 5、发送⽂件名到服务器端
ooFile_client_socket.send(file_name.encode())
# 6、创建⽂件，准备接收服务端返回的⽂件数据
with open("/home/biliu/Desktop/" + file_name, "wb") as file:
    # 7、保存⽂件数据
    while True:
        file_date = ooFile_client_socket.recv(1024)
        if file_date:
            file.write(file_date)
        else:
            break

# 8、关闭套接
ooFile_client_socket.close()
