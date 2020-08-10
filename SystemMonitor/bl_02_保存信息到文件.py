import datetime
import psutil

"""
cpu_per : cpu使用率
memory_info : 内存信息
disk_iofo : 硬盘信息
ney_info ：网络信息
"""
cpu_per = psutil.cpu_percent(interval=0.5)
memory_iofo = psutil.virtual_memory()
disk_info = psutil.disk_usage("/")
net_info = psutil.net_io_counters()

current_time = datetime.datetime.now().strftime("%F, %T")
# 拼接字符串显示
log_str = "|--------------------|------------|-------------|------------|-----------------------|\n"
log_str += "|       监控时间      |  CPU使用率  |  内存使用率  |   硬盘使用率  |        网络发放量      |\n"
log_str += "|                    |  （共%d核）  |（总计%.2fG） |（总计%.2fG）|                       |\n" \
           % (psutil.cpu_count(), memory_iofo.total/2**30, disk_info.total/2**30)
log_str += "|--------------------|------------|------------|-------------|-----------------------|\n"
log_str += "|%s|    %.2f%%   |    %.2f%%  |     %.2f%%  |   收：%dkb/发：%dkb  |\n" \
           % (current_time, cpu_per, memory_iofo.percent, disk_info.percent,  net_info.bytes_recv/2**10, net_info.bytes_sent/2**10)
log_str += "|--------------------|------------|------------|-------------|-----------------------|\n"

print(log_str)

# 保存监控信息到日志文件
file = open("log.txt", "a")
file.write(log_str + "\n\n")
file.close()