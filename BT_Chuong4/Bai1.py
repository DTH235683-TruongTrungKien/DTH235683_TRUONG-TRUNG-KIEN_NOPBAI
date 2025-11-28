import math


def ktTamGiac(a, b, c):
    if(a + b <= c or b + c <= a or c + a <= b):
        return False
    else:
        return True

def tinhDienTich(a, b, c):
    cv = a + b + c
    p = cv/2
    dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return dt

while(True):
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))
    if(ktTamGiac(a, b, c)): break
    print("Tam giac khong hop le!")

dt = tinhDienTich(a, b, c)
print("Dien tich la: ", dt)