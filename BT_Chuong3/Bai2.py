month = int(input("Nhap mot thang: "))
if(month != 2):
    if(month < 8):
        if(month % 2 != 0):
            print(31)
        else: print(30)
    else:
        if(month % 2 != 0):
            print(30)
        else: print(31)
else:
    year = int(input("Nhap nam: "))
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print(29)
    else: print(28)