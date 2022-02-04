from tkinter import *

win = Tk()
win.geometry("600x300")
win.title("grid")
win.option_add("*Font", "궁서 20")

# 격자로 나누어서 배치하기
btn1 = Button(win)
btn1.config(text="(0,0)")
btn1.grid(column=0, row=0)

btn2 = Button(win)
btn2.config(text="(1,0)")
btn2.grid(column=1, row=0)

btn3 = Button(win)
btn3.config(text="(0,1)")
btn3.grid(column=0, row=1)

# 중간에 0,2가 없으므로 0,3으로 입력했더라도 0,2 위치에 배치됨
btn4 = Button(win)
btn4.config(text="(0,3)")
btn4.grid(column=0, row=3)

# 4 X 3 버튼 array 만들기
btn_list = []
col_num = 4
row_num = 4
for j in range(0, row_num):
    for i in range(0, col_num):
        btn = Button(win)
        btn.config(text="({}, {})".format(i, j))
        btn.grid(column=i, row=j, padx=10, pady=10)
        btn_list.append(btn)

btn = Button(win)
btn.config(text="new")
btn.grid(column=1, row=2, rowspan=2)
win.mainloop()