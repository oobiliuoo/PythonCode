"""
创建 creat_http_response() 函数完成响应报文的拼接
返回响应报文
"""


def creat_http_response(status, response_body):

    # 3.拼接响应报文
    #   1.响应行
    response_line = "HTTP/1.1 %s \r\n" % status
    #   2.响应头
    response_head = "Server:oobibiliu/1.1 \r\n"
    #   3.响应空行
    response_blank = "\r\n"
    # 5.拼接成整体
    response_date = (response_line + response_head + response_blank).encode() + response_body

    return response_date
