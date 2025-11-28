import re

s = input("Nhap vao 1 chuoi: ")

negativeNumber = r"-\d+"

result = re.findall(negativeNumber, s)

print("Cac so am la:", *result)