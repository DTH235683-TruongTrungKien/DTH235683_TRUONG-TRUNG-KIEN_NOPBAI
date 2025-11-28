import math

while(True):
    month = int(input("Nhap vao thang: "))
    if(month >=1 and month <=10): break
    else: print("Thang khong hop le, nhap lai!")
quarter = math.ceil(month/3)
print("Thang nay la quy ", quarter)