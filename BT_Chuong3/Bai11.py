def ktSoNguyenTo(n):
    if(n < 2): return False
    for i in range(2, n):
        if(n % i == 0): return False
    return True

while(True):
    number = int(input("Nhap vao 1 so: "))
    if(ktSoNguyenTo(number)): print("Day la so nguyen to")
    else: print("Day khong phai la so nguyen to")
    exit = input("Tiep tuc? (Y/N): ")
    if(exit == "N"): break
