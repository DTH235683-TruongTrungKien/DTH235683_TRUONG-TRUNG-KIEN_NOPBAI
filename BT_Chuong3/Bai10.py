import math
def equation(x, n):
    result = 0
    for i in range(1, n+1):
        result+=(x**i)/(math.factorial(i))
    return result

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
result = equation(x, n)
print(result)