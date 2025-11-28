lst = []
n = int(input("Nhap n: "))
i = 0
while(i < n):
    e = int(input("Nhap lst[" + str(i) + "]: "))
    if(i > 0 and e <= lst[i-1]):
        print("Phan tu khong hop le, hay nhap lai")
    else:
        lst.append(e)
        i += 1
print(lst)