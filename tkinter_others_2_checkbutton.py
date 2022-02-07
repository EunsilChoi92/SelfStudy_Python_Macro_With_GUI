from tkinter import *


win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial 20")

# Check button
cv = IntVar()   # 정수 형태의 변수
cb = Checkbutton(win, text="1번", variable=cv)   # 버튼의 상태에 따라서 cv값이 바뀐다고 생각하면 됨
cb.pack()

# Button
btn = Button(win)
btn.config(text="옵션선택")

def click():
    text = cv.get() # cv에 저장된 값
    print(text)

btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()


win.mainloop()