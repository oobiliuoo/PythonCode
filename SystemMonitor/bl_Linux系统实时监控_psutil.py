# 1.导入模块
import datetime
import psutil

# 2.获取CPU信息
# 2.1 获取核心数
print(psutil.cpu_count())
# 获取物理核心数
print(psutil.cpu_count(logical=False))
# 2.2 获取使用率
print(psutil.cpu_percent(interval=0.5))
# 获取每一核的使用率
print(psutil.cpu_percent(interval=0.5, percpu=True))

# 3.获取内存信息
# 获取内存总体信息
print(psutil.virtual_memory().total/2**30)
# 获取内存使用率
print(psutil.virtual_memory().percent)

# 4.获取硬盘信息
# 4.1 获取硬盘的分区信息
print(psutil.disk_partitions())
# 4.2 获取指定目录的磁盘信息
print(psutil.disk_usage("/"))
# 4.3 硬盘的使用率
print(psutil.disk_usage("/").percent)

# 5.获取网络信息
# 5.1 获取收到的数据包数量
print(psutil.net_io_counters().bytes_recv)
# 5.1 获取发送的数据包数量
print(psutil.net_io_counters().bytes_sent)

# 6 获取开机时间
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d	%H:%M:%S") )
