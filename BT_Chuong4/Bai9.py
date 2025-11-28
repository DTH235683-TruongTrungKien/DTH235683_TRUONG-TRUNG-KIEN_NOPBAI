import math

n = int(input("Nhap n: "))
result = 0
for i in range(n):
    result = math.sqrt(result + 2)
print("S(n) = ", result)