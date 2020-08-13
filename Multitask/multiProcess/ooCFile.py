"""
文件夹拷贝器

拷贝目标
./test  ------> ~/Desktop/test

思路：
1.定义变量，保存源文件夹和目标文件夹的所在的路径
2.在目标路径创建新的文件夹
3.获取源文件夹中的所有文件（列表）
4.遍历列表，得到所有文件名
5.调用函数，进行拷贝

文件拷贝函数
参数：源文件夹路径，目标文件夹路径，文件名
1.拼接源文件的具体路径
2.打开源文件，创建目标文件
3.读取源文件内容，写入到目标文件

"""
import os
import multiprocessing


def copy_file(source_dir, target_dir, file_name):
    """根据参数拷贝文件"""
    # 1.拼接源文件的具体路径
    source_path = source_dir + "/" + file_name
    # 2.打开源文件，创建目标文件
    target_path = target_dir + "/" + file_name
    # 3.读取源文件内容，写入到目标文件
    with open(source_path, "rb") as s_file:
        with open(target_path, "wb") as t_file:
            while True:
                s_text = s_file.read(1024)
                if s_text:
                    print(s_text)
                    t_file.write(s_text)
                else:
                    t_file.close()
                    s_file.close()
                    break


if __name__ == '__main__':
    # 源文件夹所在路径
    source_dir = "./test"
    # 目标文件夹路径
    target_dir = "/home/biliu/Desktop/test"

    try:
        # 在指定路径创建文件夹
        os.mkdir(target_dir)
    except Exception as e:
        print("文件夹已经存在")

    # 获取源文件夹中所有文件名列表
    file_list = os.listdir(source_dir)

    # 遍历获得所有文件名
    for file_name in file_list:
        # 调用拷贝函数
        # copy_file(source_dir, target_dir, file_name)

        # 创建子进程
        copy_file_process = multiprocessing.Process(target=copy_file, args=(source_dir, target_dir, file_name))

        copy_file_process.start()

