from tkinter import *

def giaiPT():
    a = tbHeSoA.get()
    b = tbHeSoB.get()
    if a == 0 and b != 0:
        tbKetQua.set("Vô nghiệm")
    elif a == 0 and b == 0:
        tbKetQua.set("Vô số nghiệm")
    else: tbKetQua.set(f"x = {-b/a}")

def tiepPT():
    tbHeSoA.set("")
    tbHeSoB.set("")
    tbKetQua.set("")
    
def thoatPT():
    root.destroy()

root = Tk()

root.geometry(f"300x300+{int(root.winfo_screenwidth()/2-300/2)}+{int(root.winfo_screenheight()/2-300/2)}")

root.title("GIẢI PHƯƠNG TRÌNH")

lbTitle = Label(root, text="Phương trình Bậc 1", font=("Quicksand", 20), padx=30).grid(row = 0, column = 0, columnspan=2)

Label(root, text="Hệ số A: ").grid(row = 1, column = 0)

tbHeSoA = IntVar()
tbHeSoA.set("")
Entry(root, textvariable=tbHeSoA).grid(row = 1, column = 1)

Label(root, text="Hệ số B: ").grid(row = 2, column = 0)

tbHeSoB = IntVar()
tbHeSoB.set("")
Entry(root, textvariable=tbHeSoB).grid(row = 2, column = 1)

frame = Frame(root)
frame.grid(row=3,column=1)
Button(frame, text = "Giải", command=giaiPT).pack(side=LEFT, padx=5)
Button(frame, text = "Tiếp", command=tiepPT).pack(side=LEFT, padx=5)
Button(frame, text = "Thoát", command=thoatPT).pack(side=LEFT, padx=5)

Label(root, text="Kết quả: ").grid(row=4, column=0)

tbKetQua = StringVar()
tbKetQua.set("")
Entry(root, textvariable=tbKetQua, state=DISABLED).grid(row = 4, column=1)

root.mainloop()

