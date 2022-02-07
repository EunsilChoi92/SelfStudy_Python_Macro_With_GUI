from tkinter import *


win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial 20")

# Spinbox
sb = Spinbox(win)
sb.config(from_=-1, to=1)   # 최저치 ~ 최대치
sb.pack()


# Button
btn = Button(win)
btn.config(text="옵션선택")

def click():
    lab_text = sb.get()
    lab.config(text=lab_text)

btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()


win.mainloop()