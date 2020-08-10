from application import utils


def parse_request(request_date, this_ip_port):
    """解析请求报文，返回客户端的请求资源的路径"""
    # 1.根据客户端浏览器请求的资源路径，返回请求内容
    # 1.1 解码，得到请求报文的字符串
    request_text = request_date.decode()
    # 1.2 得到请求行
    #   1.2.1 找到第一个出现\r\n的位置 loc
    loc = request_text.find("\r\n")
    #   1.2.2 对字符串进行切片，截取从开始到loc的片段
    request_line = request_text[:loc]
    # print(request_line)
    # 2.把请求行按空格拆分，得到列表
    request_line_list = request_line.split(" ")
    # 3.得到资源路径
    file_path = request_line_list[1]
    print("客户端：%s 正在请求：%s" % (str(this_ip_port), file_path))
    # 4.设置默认页面
    if file_path == "/":
        file_path = "/index.html"
    # 返回请求的文件路径
    return file_path


def application(current_path, request_date, this_ip_port):
    """根据请求报文，创建并返回响应报文"""
    # 1.调用parse_request函数解析请求报文，返回资源路径
    file_path = parse_request(request_date, this_ip_port)
    # 2.创建变量保存资源路径
    resource_path = current_path + file_path
    # 3.创建响应报文
    try:
        # 返回指定页面
        with open(resource_path, "rb") as file:
            response_body = file.read()
        response_date = utils.creat_http_response("200 OK", response_body)
    except Exception as e:
        # 1)重新修改响应行
        response_line = "HTTP/1.1 404 NO FOUND\r\n"
        # 2）响应内容为错误
        response_body = "Error! (%s)" % str(e)
        # 3）编码
        response_body = response_body.encode()
        response_date = utils.creat_http_response("404 NO FOUND", response_body)

    return response_date
