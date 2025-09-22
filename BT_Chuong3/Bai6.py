def numberConvert(number):
    match(number):
            case 1: return "Một"
            case 2: return "Hai"
            case 3: return "Ba"
            case 4: return "Bốn"
            case 5: return "Năm"
            case 6: return "Sáu"
            case 7: return "Bảy"
            case 8: return "Tám"
            case 9: return "Chín"
            case 10: return "Mười"  

def numberCheck(number):
    if (number % 10 == 0): return numberConvert(number)
    else: 
        second = number % 10
        first = number // 10
        result = ""
        match(first):
            case 1: result = "Mười "
            case 2: result = "Hai mươi "
            case 3: result = "Ba mươi "
            case 4: result = "Bốn mươi "
            case 5: result = "Năm mươi "
            case 6: result = "Sáu mươi "
            case 7: result = "Bảy mươi "
            case 8: result = "Tám mươi "
            case 9: result = "Chín mươi "
        return result + numberConvert(second)

number = int(input("Nhap 1 so: "))
print(numberCheck(number))