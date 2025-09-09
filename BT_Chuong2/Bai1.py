x = float(input("Nhap so tien: "))
lai = 0
for i in range(18):
    lai+=x*(0.6/100)
    if((i+1)%6 == 0):
        x+=lai
        lai = 0
print(x)