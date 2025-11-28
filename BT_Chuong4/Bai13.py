def checkPerfectNumber(n):
    result = 0
    for i in range(1, n//2 + 1):
        if(n % i == 0):
            result += i
    if(result == n): return True

def checkAbundantNumber(n):
    result = 0
    for i in range(1, n//2 + 1):
        if(n % i == 0):
            result += i
    if(result > n): return True


n = int(input("Nhap mot so nguyen n: "))

if(checkPerfectNumber(n)): print(n, " la so hoan hao")
else: print(n, " khong la so hoan hao")

if(checkAbundantNumber(n)): print(n, " la so an khang thinh vuong van su nhu y phat tai phat loc")
else: print(n, " khong la so an khang thinh vuong van su nhu y phat tai phat loc")