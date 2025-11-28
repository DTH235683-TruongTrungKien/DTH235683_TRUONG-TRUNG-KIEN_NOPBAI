from random import randrange

lst = []
n = int(input("Nhap n: "))
for i in range(n):
    lst.append(i)

for i in range(n):
    j = randrange(n)
    lst[i], lst[j] = lst[j], lst[i]

print(lst)