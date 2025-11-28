year = int(input("Nhap vao nam: "))
if((year % 4 ==0 and year % 100 != 0) or year % 400 == 0):
    print("Day la nam nhuan")
else: print("Day khong la nam nhuan")