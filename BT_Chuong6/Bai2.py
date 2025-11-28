from random import randrange

def checkDoiXung(lst):
    return lst == lst.reverse()

lst = []
n = int(input("Nhap n: "))
for i in range(n):
    lst.append(randrange(-99, 100))

print("List:", *lst)
k = int(input("Nhap vao k: "))
if(lst.count(k) > 0): lst.remove(k) 
print("List sau khi xoa " + str(k) + ":", *lst)

if(lst == lst[::-1]):
    print("List doi xung")
else: print("List khong doi xung")
