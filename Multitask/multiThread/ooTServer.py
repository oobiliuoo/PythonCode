"""
在原有tcp_server的基础上
实现处理多客户端信息功能

"""

import socket
import threading


def client_handle(new_server_socket, new_ip_port):

    while True:
        recv_date = new_server_socket.recv(1024)
        if recv_date:
            recv_text = recv_date.decode("GBK")
            print("【%s】: %s" % (str(new_ip_port), recv_text))

        else:
            print("客户端：%s 下线" % str(new_ip_port))
            new_server_socket.close()
            break


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)
    while True:
        new_server_socket, new_ip_port = tcp_server_socket.accept()
        print("新用户上线：", new_ip_port)
        tcp_server_thread = threading.Thread(target=client_handle, args=(new_server_socket, new_ip_port))
        tcp_server_thread.setDaemon(True)
        tcp_server_thread.start()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()