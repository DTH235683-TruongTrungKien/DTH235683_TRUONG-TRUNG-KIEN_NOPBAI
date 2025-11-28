def checkPrime(n):
    for i in range(2, n):
        if(n % i == 0): return False
    return True

count = 0
evenNumber = 0
negativeNumber = 0
primeNumber = 0
averageNumber = 0
s = input("Nhap vao chuoi so: ")
arr = s.split(';')
for x in arr:
    n = int(x) 
    if(n % 2 == 0): evenNumber += 1
    if(n < 0): negativeNumber += 1
    if(checkPrime(n)): primeNumber += 1
    count += 1
    averageNumber += (n - averageNumber)/count

print("So chan:", evenNumber)
print("So am:", negativeNumber)
print("So nguyen to:", primeNumber)
print("Trung binh:", averageNumber)