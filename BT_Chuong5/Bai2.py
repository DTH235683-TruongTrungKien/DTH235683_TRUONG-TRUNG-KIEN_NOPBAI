def toiUuChuoi(s):
    return ' '.join(s.split())

s = input("Nhap vao mot chuoi: ")
s = toiUuChuoi(s)
print("Chuoi sau khi duoc toi uu:", s)