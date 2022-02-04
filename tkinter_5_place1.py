from tkinter import *

win = Tk()
win.geometry("400x200")
win.title("pack")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack(side="top")

btn = Button(win)
btn.config(text="버튼")

def aa():
    # btn.pack(side=ent.get())  # top, bottm, left, right
    btn.pack(pady=ent.get())    # 10, 30 등등 입력 숫자만큼 띄우기

btn.config(command=aa)
btn.pack()

btn2 = Button(win)
btn2.config(text="temp")
btn2.pack()

win.mainloop()