"""
1.导入模块
2.通过match()方法，验证正则
3.判断验证是否成功
4.如果成功，获取匹配结果

"""

# 1.导入模块
import re


def test_search():
    """
    一：search()的使用
    match()和search()的区别：
    match 从字符串开头位置开始，如果失败，返回None
    search 从整个字符串中搜索
    """
    result = re.search("\d+", "阅读次数：9999")
    # 判断验证是否成功
    if result:
        # 如果成功，获取匹配结果
        print("匹配成功")
        print("匹配结果：", result.group())

    else:
        print("匹配失败")


def test_findall():
    """
    二：findall()的使用
    一次查找所以符合规定的数，返回是一个列表
    """
    result = re.findall("\d+", "阅读次数：9999，转发次数：6666，评论次数：777")
    # 判断验证是否成功
    if result:
        # 如果成功，获取匹配结果
        print("匹配成功")
        print("匹配结果：", result)

    else:
        print("匹配失败")


def test_sub():
    """
    三：sub()的使用
    按照正则替换字符串
    sub("正则表达式","新的内容", "要替换的字符串")
    返回值：替换后的字符串
    """
    str1 = """
    <div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
    """
    # result = re.sub("\d+", "1000", "阅读次数：9999，转发次数：6666，评论次数：777")
    result = re.sub("<[^>]+>|\n| |&nbsp", "", str1)
    # 判断验证是否成功
    if result:
        # 如果成功，获取匹配结果
        print("匹配成功")
        print("匹配结果：", result)

    else:
        print("匹配失败")


def test_split():
    """
    四：split()使用
    split("正则表达式", “待拆分的字符串”）
    返回值是一个列表
    :return:
    """
    result = re.split(":| ", "info:hello@163.com zhangsan lisi")
    if result:
        # 如果成功，获取匹配结果
        print("匹配成功")
        print("匹配结果：", result)

    else:
        print("匹配失败")


if __name__ == '__main__':
    # test_search()
    # test_findall()
    # test_sub()
    test_split()