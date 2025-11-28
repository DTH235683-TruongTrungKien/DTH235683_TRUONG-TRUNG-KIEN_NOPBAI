lst = []
n = int(input("Nhap so luong phan tu: "))
for i in range(n):
    e = int(input("Nhap lst[" + str(i) + "]: "))
    lst.append(e)
lst.sort(reverse = True)
print("List sau khi sap xep:", lst)