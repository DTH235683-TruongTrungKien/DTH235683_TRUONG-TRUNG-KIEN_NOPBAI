seconds = int(input("Nhap so giay: "))
hour = seconds // 3600
minute = (seconds % 3600) // 60
second = (seconds % 3600) % 60
format = "AM"
if(hour > 12):
    hour -= 12
    format = "PM"
print(hour, ":", minute, ":", second, format)