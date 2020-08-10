"""
1. 导入模块
2. 创建套接字
3. 建立连接
4. 建立请求
5. 发送请求
6. 保存响应
7. 关闭套接字
"""

# 1. 导入模块
import socket
# 2. 创建套接字
tcp_client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. 建立连接
tcp_client_Socket.connect(("www.icoderi.com", 80))

# 4. 拼接请求协议
# 4.1 请求行
request_line = "GET /HTTP/1.1 \r\n"
# 4.2 请求头
request_head = "Host:www.rcoderi.com \r\n"
# 4.3 请求空行
request_blank = "\r\n"
# 4.4 整体拼接
request_date = request_line + request_head + request_blank

# 5. 发送请求
tcp_client_Socket.send(request_date.encode())

# 6. 接收来自服务器的响应
recv_date = tcp_client_Socket.recv(4096)
# 6.1 解码
recv_text = recv_date.decode()
print(recv_text)

# 7. 保存内容
# 7.1 查找“\r\n\r\n"的位置
loc = recv_text.find("\r\n\r\n")
# 7.2 截取字符串
html_date = recv_text[loc:]
print(html_date)
# 7.3 保存内容到文件
with open("index.html", "w") as file:
    file.write(html_date)

# 8. 关闭套接字
tcp_client_Socket.close()





