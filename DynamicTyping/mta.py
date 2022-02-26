# mixed type array
list = [[] for i in range(100)]
list[0].append("Name")
list[0].append(12345678)
list[0].append(100.00)
print(list[0])
for obj in list[0]:
    print(type(obj))