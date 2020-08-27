""""
一：定义函数获取列表页的内容页地址 get_movie_links()
1.定义列表的地址：https://www.ygdy8.net/html/gndy/dyzz/index.html
2.打开url地址，获取数据
3.解码获取得到的数据
4.使用正则得到所有影片内容页地址
二：主函数

解码不了，所以程序运行不了
"""
import urllib.request
import re


def get_movie_links():
    # 1.定义列表的地址：https: // www.ygdy8.net / html / gndy / dyzz / index.html
    film_list_url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
    # 2.打开url地址，获取数据
    response_list = urllib.request.urlopen(film_list_url)
    response_list_date = response_list.read()
    response_list_date = response_list_date[:27000]
    # print(response_list_date)
    # 3.解码获取得到的数据
    response_list_text = response_list_date.decode("GBK")

    # 4.使用正则得到所有影片内容页地址
    # print(response_list_text)
    # 4.1 使用findall()查找所有影片对应的内容也地址
    url_list = re.findall(r"<a href=\"(.*\.html)\" class=\"ulink\">(.*)</a>", response_list_text)
    # 4.2 保存地址
    # url_list=[(xxxx.html,xxx影片),(xxxx.html.xxx.影片),.....]
    # print("影片地址：", url_list)
    # 定义字典，保存影片信息
    film_dict = {}

    i = 1
    # 4.3 循环遍历 url_list
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
        result = re.search(r"bgcolor=\"#fdfddf\"><a href=\"(.*)\">", response_content_text)
        # print(result)
        film_dict[film_name] = result.group(1)
        print("已经获取%d条信息" % i)
        i += 1

    return film_dict


def main():
    films_dict = get_movie_links()

    # 把字典遍历输出
    for film_name, film_link in films_dict.items():
        print("%s | %s " % (film_name, film_link))


if __name__ == '__main__':
    main()