""""
在原有基础上将其封装程对象

"""
import urllib.request
import re
import threading
import time

class OoMovie(object):

    def __init__(self):
        # 定义实例属性，保存影片信息
        self.film_dict = dict()
        self.i = 1
        # 定义互斥锁，防止资源竞争
        self.lock = threading.Lock()

    def link_decode(self, film_list_url, regex_str):
        """
        获取目标电影网站的地址

        :param film_list_url: 目标列表网站地址
        :return: 地址
        """
        # 1.打开url地址，获取数据
        response_list = urllib.request.urlopen(film_list_url)
        response_list_date = response_list.read()
        # 此处切片是因为后续有代码解码不出，因此获得的影片不会齐全
        response_list_date = response_list_date[:27000]
        # print(response_list_date)
        # 2.解码获取得到的数据
        response_list_text = response_list_date.decode("GBK")

        # 3.使用正则得到所有影片内容页地址
        # 4.1 使用findall()查找所有影片对应的内容也地址
        url_list = re.findall(regex_str, response_list_text)
        return url_list

    def get_movie_links(self, url_list, regex_str):
        try:
            for content_url, film_name in url_list:
                content_url = "https://www.ygdy8.net" + content_url
                # print("影片名称：%s, 内容页地址：%s" % (film_name, content_url))
                # 1）打开网页地址
                response_content = urllib.request.urlopen(content_url)
                # 2) 读取网页数据
                response_content_date = response_content.read()
                # 3) 解码
                response_content_text = response_content_date.decode("GBK")
                # print(response_content_text)
                # 4) 使用search()查找
                result = re.search(regex_str, response_content_text)
                # print(result)
                self.lock.acquire()
                film_text = result.group(1)
                pos = film_text.rfind("/")
                film_addr =film_text[:pos+1]
                self.film_dict[film_name] = film_addr
                print("下载成功---", self.i)
                self.i += 1
                self.lock.release()
        except Exception as e:
            print("出错---", e)
            return

    def start(self):

        # 1.定义列表的地址：https: // www.ygdy8.net / html / gndy / dyzz / index.html
        film_list_url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
        # 2.1定义列表网站中提取所有电影内容页地址的正则表达式
        regex_str_1 = r"<a href=\"(.*\.html)\" class=\"ulink\">(.*)</a>"
        # 2.2定义电影内容页中提取下载地址的正则表达式
        regex_str_2 = r"bgcolor=\"#fdfddf\"><a href=\"(.*)\">"
        # 3.获取列表网站中所有电影的电影名和内容页地址
        url_list = self.link_decode(film_list_url, regex_str_1)

        url_list_1 = url_list[:7]
        url_list_2 = url_list[7:14]
        url_list_3 = url_list[14:]

        # 4.获取电影下载连接
        my_thread_1 = threading.Thread(target=self.get_movie_links, args=(url_list_1, regex_str_2))
        my_thread_2 = threading.Thread(target=self.get_movie_links, args=(url_list_2, regex_str_2))
        my_thread_3 = threading.Thread(target=self.get_movie_links, args=(url_list_3, regex_str_2))

        my_thread_1.setDaemon(True)
        my_thread_2.setDaemon(True)
        my_thread_3.setDaemon(True)

        # my_thread_1.join()
        my_thread_1.start()
        my_thread_2.start()
        my_thread_3.start()
        # self.get_movie_links(url_list_1,regex_str_2)


def main():

    movie = OoMovie()
    movie.start()

    while True:
        if movie.i > 19:
            break
        else:
            time.sleep(1)

    # 把字典遍历输出
    for film_name, film_link in movie.film_dict.items():
        print("%s | %s " % (film_name, film_link))


if __name__ == '__main__':
    main()
