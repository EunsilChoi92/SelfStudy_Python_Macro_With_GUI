from tkinter import *

win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial 20")

# Scale
sc = Scale(win)
sc.config(length=1000, tickinterval=10, from_=0, to=50, orient="horizontal")    # tickinterval = 인터발 표시
sc.pack()

# Button
btn = Button(win)
btn.config(text="옵션선택")

def click():
    lab_text = sc.get()
    lab.config(text=lab_text)

btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()


win.mainloop()