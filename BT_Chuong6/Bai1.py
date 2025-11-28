def checkPrime(n):
    return n > 1 and all(n % i for i in range(2, n))

lst = []
n = int(input("Nhap so luong phan tu: "))
for i in range(n):
    e = int(input("Nhap lst[" + str(i) + "]: "))
    lst.append(e)
k = int(input("Nhap vao k: "))
print("So luong", k, "trong list la: ", lst.count(k))
print("Tong so nguyen to la:", sum(i for i in lst if checkPrime(i)))
print("Mang sau khi duoc sap xep: ", sorted(lst))
del lst