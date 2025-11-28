import re

linkPattern = r"[a-zA-Z]:\\\\\w+\\\w+\.mp3"
filePattern = r'\w+\.mp3'
namePattern = r'\w+'
s = input("Nhap vao mot chuoi: ")
if(re.fullmatch(linkPattern, s)):
    file = ''.join(re.findall(filePattern, s))
    name = file.replace('.mp3', '')
    print("File:", file)
    print("Name:", name)
else:
    print("Sai dinh dang!")
