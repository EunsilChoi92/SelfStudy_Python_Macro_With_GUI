from tkinter import *
from datetime import datetime

win = Tk()
win.geometry("600x100")
win.title("What time?")
win.option_add("*Font", "궁서 20")


def what_time():
    date_now = datetime.now()
    btn.config(text=date_now)   # 버튼에 표시되는 텍스트를 현재 시간으로 바꿈

btn = Button(win)   # 버튼 만들기

btn.config(text="현재 시각")    # 버튼에 표시되는 텍스트
btn.config(width=30)    # 버튼 크기
btn.config(command=what_time)   # what_time 함수 실행

btn.pack()  # 버튼 배치

win.mainloop()
