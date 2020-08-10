student = [{"name":"Bob",
            "age":"18",
            "sex":"boy"},
           {"name":"Andiy",
            "age":"17",
            "sex":"girl"}]
find_name = "Andiy"
for nam in student:
    print(nam)
    if nam["name"] == find_name:
        print("find it")
        break
else:
    print("not find")
print("end of for")