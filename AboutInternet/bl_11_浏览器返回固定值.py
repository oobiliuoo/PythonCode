"""

1.导入模块
2.创建套接字
3.申请地址重用
4.绑定端口
5.设置监听
6.等待客户端连接
7.定义函数，实现客户端信息接收和响应
8.发送响应
9.关闭连接

"""

# 1.导入模块
import socket


def request_handler(this_socket, this_ip_port):
    """响应处理函数"""
    # 1>接受客户端发来的请求报文
    request_date = this_socket.recv(1024)
    # print(request_date)
    # 判断报文是否为空
    if not request_date:
        print("客户端【%s】已经下线" % str(this_ip_port))
        this_socket.close()
        return
    # 2>拼接响应报文
    # 1.响应行
    response_line = "HTTP/1.1 200 OK \r\n"
    # 2.响应头
    response_head = "Server:oobibiliu/1.1 \r\n"
    # 3.响应空行
    response_blank = "\r\n"
    # 4.响应主体
    response_body = "HelloWorld!"
    # 5.拼接成整体
    response_date = response_line + response_head + response_blank + response_body
    # 3>发送响应报文
    this_socket.send(response_date.encode())
    # 4>关闭当前连接
    this_socket.close()


def main():
    """主函数"""
    # 2.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3.申请地址重用------------------表示当前套接字     表示申请地址重用      为真
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 4.绑定端口
    tcp_server_socket.bind(("", 8080))
    # 5.设置监听
    tcp_server_socket.listen(128)

    while True:
        # 6.等待客户端连接
        new_client_socket, new_ip_port = tcp_server_socket.accept()
        print("新用户：%s 来了" % str(new_ip_port))
        # 7.定义函数，实现客户端信息接收和响应
        request_handler(new_client_socket, new_ip_port)

    # 8.关闭连接
    tcp_server_socket.close()


if __name__ == '__main__':
    main()