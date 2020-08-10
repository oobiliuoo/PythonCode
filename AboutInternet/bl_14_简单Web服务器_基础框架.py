"""
在原有WebServer的基础上，
析出核心代码到模块app的application()方法上
"""
# 1.导入模块
import socket
from application import app


class WebServer(object):
    def __init__(self):
        # 1.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.申请地址重用------------------表示当前套接字     表示申请地址重用      为真
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 3.绑定端口
        tcp_server_socket.bind(("", 8080))
        # 4.设置监听
        tcp_server_socket.listen(128)
        # 5.创建实例实现,保存套接字
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            # 1.等待客户端连接
            new_client_socket, new_ip_port = self.tcp_server_socket.accept()
            print("新用户：%s 来了" % str(new_ip_port))
            # 2.调用方法，实现客户端信息接收和响应
            self.request_handler(new_client_socket, new_ip_port)

        self.tcp_server_socket.closs()

    def request_handler(self, this_socket, this_ip_port):
        """响应处理函数"""
        # 1.接受客户端发来的请求报文
        request_date = this_socket.recv(1024)
        # print(request_date)
        # 2.判断报文是否为空
        if not request_date:
            print("客户端【%s】已经下线" % str(this_ip_port))
            this_socket.close()
            return
        # 3.调用app模块的application函数处理
        response_date = app.application("static", request_date, this_ip_port)
        # 4.发送响应报文
        this_socket.send(response_date)
        # 5.关闭当前连接
        this_socket.close()


def main():
    """主函数"""
    web = WebServer()

    web.start()


if __name__ == '__main__':
    main()
