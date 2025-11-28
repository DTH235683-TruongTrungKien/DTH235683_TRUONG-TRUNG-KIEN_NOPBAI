from tkinter import *

def giaiPT():
    a = tbHeSoA.get()
    b = tbHeSoB.get()
    c = tbHeSoC.get()
    if a == 0:
        tbKetQua.set("Không phải phương trình bậc 2!")
    else:
        delta = b**2 - 4*a*c
        if(delta == 0):
            tbKetQua.set(f"Nghiệm kép: x1 = x2 = {-b/a}")
        elif(delta < 0):
            tbKetQua.set("Vô nghiệm")
        else:
            tbKetQua.set(f"x1 = {round((-b - delta**(1/2))/2*a, 2)}, x2 = {round((-b + delta**(1/2))/2*a, 2)}")

def tiepPT():
    tbHeSoA.set("")
    tbHeSoB.set("")
    tbHeSoC.set("")
    tbKetQua.set("")
    
def thoatPT():
    root.destroy()

root = Tk()

root.geometry(f"300x300+{int(root.winfo_screenwidth()/2-300/2)}+{int(root.winfo_screenheight()/2-300/2)}")

root.title("GIẢI PHƯƠNG TRÌNH")

lbTitle = Label(root, text="Phương trình Bậc 2", font=("Quicksand", 20), padx=30).grid(row = 0, column = 0, columnspan=2)

Label(root, text="Hệ số A: ").grid(row = 1, column = 0)

tbHeSoA = IntVar()
tbHeSoA.set("")
Entry(root, textvariable=tbHeSoA).grid(row = 1, column = 1)

Label(root, text="Hệ số B: ").grid(row = 2, column = 0)

tbHeSoB = IntVar()
tbHeSoB.set("")
Entry(root, textvariable=tbHeSoB).grid(row = 2, column = 1)

Label(root, text="Hệ số C: ").grid(row = 3, column = 0)

tbHeSoC = IntVar()
tbHeSoC.set("")
Entry(root, textvariable=tbHeSoC).grid(row = 3, column = 1)

frame = Frame(root)
frame.grid(row=4,column=1)
Button(frame, text = "Giải", command=giaiPT).pack(side=LEFT, padx=5)
Button(frame, text = "Tiếp", command=tiepPT).pack(side=LEFT, padx=5)
Button(frame, text = "Thoát", command=thoatPT).pack(side=LEFT, padx=5)

Label(root, text="Kết quả: ").grid(row=5, column=0)

tbKetQua = StringVar()
tbKetQua.set("")
Entry(root, textvariable=tbKetQua, state=DISABLED).grid(row = 5, column=1)

root.mainloop()

