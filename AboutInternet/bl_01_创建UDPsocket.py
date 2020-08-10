# 1.导入模块
import socket

# 2.创建套接字，使用IPV4 UDP
"""
socket.socket(协议类型, 传输方式)
参数一：
socket.AF_INET 使用IPV4
socket.AF_INET6 使用IPV6
参数二“
socket.SOCK_DGRAM 使用UDP
ocket.SOCK_STREAM 使用TCP
"""
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""
绑定端口
socket.bind(address) 
address:是一个元组 1.字符串类型的IP号， 2.整型的端口号
绑定发送端的地址
""表示本机地址
"""
udp_socket.bind(("192.168.43.131", 2333))

# 3.数据传输
"""
发送数据：
sendto(要发送数据的二进制格式，对方的ip和端口号）
参数一： 要发送的数据的二进制格式
字符串转为二进制： 字符串.encode() 默认编码格式为UTF-8
参数二：对方的IP号和端口号
要以元组方式传递 1.字符串类型的IP号， 2.整型的端口号
"""
udp_socket.sendto("helloworld".encode(), ("192.168.124.12", 8080))

"""
接收数据：
recvform(1024) 从套接字中读取1024个字节数据
此方法会造成程序阻塞，接收到数据会自动解除
否之一直等待
recv_date 接收到一个元组 内容同上
"""
# recv_date = udp_socket.recvfrom(1024)

"""
解码数据：
decode(1.指定解玛格式，2.错误i处理)
参数一：
encoding="UTF-8", / “GBK”国标玛   “UTF-8”万国码
参数二：
error = "strict" 默认为严格
error = "ignore" 忽视错误
"""
# recv_text = recv_date[0].decode("GBK")

# 4.关闭套接字
udp_socket.close()