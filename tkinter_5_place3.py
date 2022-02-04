from tkinter import *

win = Tk()
win.geometry("600x300")
win.title("place")
win.option_add("*Font", "궁서 20")

# 절대좌표 또는 상대좌표에 배치
xx = 30
yy = 50

btn = Button(win)
btn.config(text="({},{})".format(xx, yy))
btn.place(x=xx, y=yy)   # 상대좌표는 relx, rely(전체 창 크기에 따라 달라짐)

win.mainloop()