def squareFunction(a, b, c):
    delta = b**2 - (4 * a * c)
    if(delta < 0): return "Phuong trinh vo nghiem"
    elif(delta == 0):
        x = -b / (2*a)
        return x
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return x1, x2

print("Phuong trinh bac 2 co dang ax^2 + bx + c = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

solution = squareFunction(a, b, c)
print(solution)
