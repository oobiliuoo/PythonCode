xiaomin = {"name": "小名",
           "age": "18",
           "gentle": "true",
           "weight": "75",
           "height":"170"}

print(xiaomin["name"])
xiaomin["cs"] = 0
# 删除
xiaomin.pop("cs")

print(len(xiaomin))
print(xiaomin)