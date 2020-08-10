mq_num = ["张三", "李四", "王五"]
mq_num2 =["追加1", "追加2"]

# 1.取值和取索引
print(mq_num[0])
print(mq_num.index("王五"))  # .index()获取索引 查询内容要存在 否则报错

# 2.修改
mq_num[0] = "赵六"

# 3.增加
mq_num.insert(3, "张七")    # 若指定值已存在，则进行插入 若指定索引不是末尾 自动改成末尾
mq_num.append("张八")  # 列表末尾追加
mq_num.extend(mq_num2)  # 扩展到末尾

# 4.删除
# del 本质上将一个变量从内存删除
# del 删除后变量被删除
del mq_num[6]
# 删除指定内容元素
mq_num.remove("追加1")
# pop默认删除最后 指定参数删除指定位置
mq_num.pop()
mq_num.pop(0)
# 删除全部数据
mq_num.clear()

print(mq_num)
