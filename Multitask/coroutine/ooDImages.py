"""
1.定义要下载的图片路径
2.调用文件下载的函数。专门下载图片

文件下载函数：
1.根据url地址请求网络资源
2.在本地创建文件，准备保存
3.读取网络资源数据
4.把读取的网络资源写入本地文件
5.异常捕获

"""
from gevent import monkey
monkey.patch_all()
import urllib.request
import gevent


def images_download(image_path, file_name):
    try:
        # 根据url地址请求网络资源
        ulr_date = urllib.request.urlopen(image_path)  # 打开⽹址并返回对应的内容（⼆进制流）
        # 打开要保存的本地文件
        with open(file_name, "wb") as file:
            while True:
                image_date = ulr_date.read(1024)
                if image_date:
                    file.write(image_date)
                else:
                    break
    # 异常捕获
    except Exception as e:
        print("文件%s--下载失败！" % file_name)
    else:
        print("文件%s--下载成功！" % file_name)


def main():
    # 定义目标图片路径
    image_1 = "http://img.mp.itc.cn/upload/20170716/8e1b835f198242caa85034f6391bc27f.jpg"
    image_2 = "http://img.mp.sohu.com/upload/20170529/d988a3d940ce40fa98ebb7fd9d822fe2.png"
    image_3 = "http://image.uczzd.cn/11867042470350090334.gif?id=0&from=export"

    # 调用图片下载函数
    # images_download(image_1, "1.gif")
    # images_download(image_2, "2.gif")
    # images_download(image_3, "3.gif")

    # 协程
    # gevent.joinall([协程列表]) 批量给协程join()
    gevent.joinall([
        gevent.spawn(images_download, image_1, "./images/1.gif"),
        gevent.spawn(images_download, image_2, "./images/2.gif"),
        gevent.spawn(images_download, image_3, "./images/3.gif")
    ])

    # g1 = gevent.spawn(images_download, image_1, "1.gif")
    # g2 = gevent.spawn(images_download, image_2, "2.gif")
    # g3 = gevent.spawn(images_download, image_3, "3.gif")


if __name__ == '__main__':
    main()