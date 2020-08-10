"""
在bl_13_简单Web服务器_返回指定页面的基础上
将其封装成类WebServer
调用start()方法即可开始运行

"""

# 1.导入模块
import socket


class WebServr(object):
    def __init__(self):
        # 1.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.申请地址重用------------------表示当前套接字     表示申请地址重用      为真
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 3.绑定端口
        tcp_server_socket.bind(("", 8080))
        # 4.设置监听
        tcp_server_socket.listen(128)
        # 5.设置实例属性，保存套接字
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            # 6.等待客户端连接
            new_client_socket, new_ip_port = self.tcp_server_socket.accept()
            print("新用户：%s 来了" % str(new_ip_port))
            # 7.定义函数，实现客户端信息接收和响应
            self.request_handler(new_client_socket, new_ip_port)
        # 8.关闭连接
        tcp_server_socket.close()

    def request_handler(self, this_socket, this_ip_port):
        """响应处理函数"""
        # 1>接受客户端发来的请求报文
        request_date = this_socket.recv(1024)
        # print(request_date)
        # 判断报文是否为空
        if not request_date:
            print("客户端【%s】已经下线" % str(this_ip_port))
            this_socket.close()
            return

        # 根据客户端浏览器请求的资源路径，返回请求内容
        # 解码，得到请求报文的字符串
        request_text = request_date.decode()
        # 得到请求行
        #   找到第一个出现\r\n的位置 loc
        loc = request_text.find("\r\n")
        #   对字符串进行切片，截取从开始到loc的片段
        request_line = request_text[:loc]
        # print(request_line)
        # 把请求行按空格拆分，得到列表
        request_line_list = request_line.split(" ")
        file_path = request_line_list[1]
        print("客户端：%s 正在请求：%s" % (str(this_ip_port), file_path))
        # 设置默认页面
        if file_path == "/":
            file_path = "/index.html"

        # 2>拼接响应报文
        # 1.响应行
        response_line = "HTTP/1.1 200 OK \r\n"
        # 2.响应头
        response_head = "Server:oobibiliu/1.1 \r\n"
        # 3.响应空行
        response_blank = "\r\n"
        # 4.响应主体
        try:
            # 返回指定页面
            with open("static" + file_path, "rb") as file:
                response_body = file.read()
        except Exception as e:
            # 1)重新修改响应行
            response_line = "HTTP/1.1 404 NO FOUND\r\n"
            # 2）响应内容为错误
            response_body = "Error! (%s)" % str(e)
            # 3）编码
            response_body = response_body.encode()
        # 5.拼接成整体
        response_date = (response_line + response_head + response_blank).encode() + response_body
        # 3>发送响应报文
        this_socket.send(response_date)
        # 4>关闭当前连接
        this_socket.close()


def main():
    """主函数"""
    ws = WebServr()
    ws.start()


if __name__ == '__main__':
    main()
