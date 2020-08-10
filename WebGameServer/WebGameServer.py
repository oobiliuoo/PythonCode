"""
1.在类中配置一个实例属性，用来保存游戏路径
如： project_dict = {"2048": 2048,,,,,,"植物大战僵尸": zwdzjs-v1}
2.在类中配制一个实例方法，用来初始化项目
2.1便利项目字典
2.2对项目进行显示
2.3保存用户选择
3.配置用户选择，打开对应页面
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
        # 创建实例属性，保存要发布的游戏的路径
        self.project_dir = ""
        # 6.创建实例属性，保存项目
        self.projects_dict = dict()  # dict()表示建立空字典
        self.projects_dict['植物⼤战僵⼫-普通版'] = "zwdzjs-v1"
        self.projects_dict['植物⼤战僵⼫-外挂版'] = "zwdzjs-v2"
        self.projects_dict['保卫萝⼘'] = "tafang"
        self.projects_dict['2048'] = "2048"
        self.projects_dict['读⼼术'] = "dxs"
        # 7.初始化项目
        self.init_project()

    def init_project(self):
        """初始化项目"""
        # 1.显示可发布的游戏菜单
        keys_list = list(self.projects_dict.keys()) # 取出字典KEY 并且转化为列表
        # eumerate(key_list) 会将列表转化成🗂索引元组
        # [（0，2048），（1，dxs) ,,,,]
        for indeax, game_name in enumerate(keys_list):
            print("%d.%s" % (indeax, game_name))
        # 2.接受用户选择
        sel_no = int(input("请选择要发布的游戏序号：\n"))
        # 3.根据用户选择发布指定的项目（保存用户选择所对应的游戏的路径）
        # 3.1根据用户的选择，得到指定游戏的名称 key值
        key = keys_list[sel_no]
        # 3.1根据字典KEY得到项目具体路径
        current_dir = self.projects_dict[key]
        self.project_dir = current_dir
        print(key, current_dir)

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
        response_date = app.application("gamebox/" + self.project_dir, request_date, this_ip_port)
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
