from dataclasses import dataclass

@dataclass
class Point():
    x: float = 0
    y: float = 0
    def pointInput(self):
        self.x = int(input("Nhap toa do x: "))
        self.y = int(input("Nhap toa do y: "))

def tinhDoDai(A, B):
    dAB = ((B.x - A.x)**2 + (B.y - A.y)**2)**(1/2)
    return dAB

A = Point()
B = Point()
print("Nhap toa do diem A: ")
A.pointInput()
print("Nhap toa do diem B: ")
B.pointInput()
print("Do dai AB la: ", tinhDoDai(A, B))



