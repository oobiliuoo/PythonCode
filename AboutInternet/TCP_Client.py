# 1.导入模块
import socket
# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
"""

tcp_client_socket.connect(address)
address -> ("ip", 端口)
"""
tcp_client_socket.connect(("192.168.43.1", 8080))

# 4.数据传输
# 发送数据
tcp_client_socket.send("约马？".encode())
# 接收数据
recv_date = tcp_client_socket.recv(1024)
print(recv_date.decode("GBK"))
# 5.关闭套接字
tcp_client_socket.close()