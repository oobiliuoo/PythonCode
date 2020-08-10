import yagmail
"""
user: 发件人邮箱
password ：邮箱授权码
host : 邮件发送服务器
"""
# 建立邮箱对象
yag = yagmail.SMTP(user="biliu819@163.com", password="GRDCGOUASMNEBSTH", host="smtp.163.com")
# 邮件正文
text = ["这是为了测试，刘淑是个大美女"]
# 发送邮件
yag.send("1910344608@qq.com", 'subject', text)

