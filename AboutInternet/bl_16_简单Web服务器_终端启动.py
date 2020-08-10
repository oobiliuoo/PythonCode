"""
在原有框架的基础上实现终端启动
1.导入sys模块
2.调用argv反法获取参数列表
3.判断参数个数是否为2，既 xxx.py 端口号
4.判断端口号参数是否为数字
5.获取端口号
6.在启动Web服务器的时候指定端口号

"""
# 1.导入模块
import sys
import socket
from application import app


class WebServer(object):
    def __init__(self, my_port):
        # 1.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.申请地址重用------------------表示当前套接字     表示申请地址重用      为真
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 3.绑定端口
        tcp_server_socket.bind(("", my_port))
        # 4.设置监听
        tcp_server_socket.listen(128)
        # 5.创建实例实现,保存套接字
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        print("Web服务器启动成功，正在等待客户端连接...")
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

    # 调用argv反法获取参数列表
    params_list = sys.argv
    print(params_list)
    # 判断参数个数是否为2，既 xxx.py 端口号
    if len(params_list) != 2:
        print("请输入正确内容：xxx.py 端口号")
        return
    # 判断端口号参数是否为数字
    if not params_list[1].isdigit():
        print("请输入正确端口号：【1024-65535】")
        return
    # 获取端口号
    my_port = int(params_list[1])
    # 在启动Web服务器的时候指定端口号
    web = WebServer(my_port)

    web.start()


if __name__ == '__main__':
    main()
