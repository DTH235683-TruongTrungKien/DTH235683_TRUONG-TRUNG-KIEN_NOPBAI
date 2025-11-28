def checkPrime(n):
    return n > 1 and all(n % i for i in range(2, n))

lst = []
listLe = []
listChan = []
listPrime = []
listNonPrime = []

n = int(input("Nhap so luong phan tu: "))
for i in range(n):
    e = int(input("Nhap lst[" + str(i) + "]: "))
    lst.append(e)
    if(e & 1):
        listLe.append(e)
    else:
        listChan.append(e)
    if(checkPrime(e)):
        listPrime.append(e)
    else:
        listNonPrime.append(e)
print("Cac so chan:", *listChan, "- So luong:", len(listChan))
print("Cac so le:", *listLe, "- So luong:", len(listLe))
print("Cac so nguyen to:", *listPrime)
print("Cac so khong phai nguyen to:", *listNonPrime)