def checkDoiXung(s):
    if(s == s[::-1]): return True
    return False

while(True):
    s = input("Nhap vao 1 chuoi: ")
    if(checkDoiXung(s)):
        print(s, "la chuoi doi xung")
    else:
        print(s, "khong la chuoi doi xung")
    option = input("Tiep tuc? (Y/N): ")
    if(option.lower() == "n"): break
