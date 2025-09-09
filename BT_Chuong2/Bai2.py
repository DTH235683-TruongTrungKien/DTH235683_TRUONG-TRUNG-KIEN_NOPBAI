def calculator(a, b, ch):
    match ch:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            return "Sai cu phap"
            
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
ch = input("Nhap phep tinh: ")
kq = calculator(a, b, ch)
print("Ket qua: ", kq)