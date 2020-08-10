try:

    num = int(input("请输入一个整数: "))
    result = 8 / num
    print(result)

# except ZeroDivisionError:
#     print("除0错误")
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
finally:
    print("无论是否成功，都会执行")

print("-" * 50)
