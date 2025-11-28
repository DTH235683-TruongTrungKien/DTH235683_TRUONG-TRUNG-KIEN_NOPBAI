def lastDayCheck(day, month, year):
    if(month != 2):
        if(month < 8):
            if(month % 2 != 0 and day == 31):
                return True   
            elif(day == 30): return True
        else:
            if(month % 2 != 0 and day == 30):
                return True
            elif(day == 31): return True
    else:
        if(((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and day == 29):
            return True
        elif(day == 28): return True
    return False

while True:
    day = int(input("Nhap ngay: "))
    month = int(input("Nhap thang: "))
    year = int(input("Nhap nam: "))
    if(lastDayCheck(day, month, year)): break
    else: print("Sai dinh dang, nhap lai.")

if(lastDayCheck(day, month, year)):
    day = 1
    month+=1
    if(month > 12):
        month = 1
        year+=1
else:
    day+=1

print("Ngay tiep theo la: ", day, "/", month, "/", year)