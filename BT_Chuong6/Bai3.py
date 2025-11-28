from random import randrange

def taoMaTran(lst, n, m):
    tmpList = []
    for i in range(n):
        for j in range(m):
            tmpList.append(randrange(-99, 100))
        lst.append(tmpList)
        tmpList = []

def xuatMaTran(option : str, lst, index):
    if(option.lower() == "dong"):
        if(index < 1 or index + 1 > len(lst)):
            print("So dong khong hop le")
            return []
        else:
            print(*lst[index-1])
    elif(option.lower() == "cot"):
        if(index < 1 or index + 1 > len(lst[0])):
            print("So cot khong hop le")
            return []
        else:
            for i in range(n):
                print(lst[i][index-1], end=' ')
    else: print("Lua chon khong hop le")

def maxMaTran(lst):
    return max(max(i) for i in lst)
lst = []
n = int(input("Nhap n dong cua ma tran: "))
m = int(input("Nhap m cot cua ma tran: "))
taoMaTran(lst, n, m)
print("Ma tran la: ")
for i in range(n):
    print(lst[i])

r = int(input("Nhap vao so dong bat ky: "))
xuatMaTran("dong", lst, r)
c = int(input("Nhap vao so cot bat ky: "))
xuatMaTran("cot", lst, c)
print()
maxNumber = maxMaTran(lst)
print("So lon nhat trong ma tran la: ", maxNumber)

