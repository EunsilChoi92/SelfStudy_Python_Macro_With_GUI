from tkinter import *
import random
from datetime import datetime

win = Tk()
win.title("AIM_GAME")
win.geometry("550x150")
win.option_add("*Font", "궁서 20")

# Label
lab = Label(win)
lab.config(text="표적 개수")
lab.grid(column=0, row=0, padx=20, pady=20)

# Entry
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

k = 1

# 처음 입력한 숫자보다 k가 낮으면 ran_btn 함수 호출
# 아니면 clear, 걸린 시간 표시
def cc():
    global k
    if k < num_t:
        k += 1
        btn.destroy()
        ran_btn()
    else:
        fin = datetime.now()
        dif_sec = round((fin - start).total_seconds(), 2)
        btn.destroy()
        lab = Label(win)
        lab.config(text="clear {} 초".format(dif_sec))
        lab.pack(pady=230)

# 랜덤으로 버튼 생성
def ran_btn():
    global btn
    btn = Button(win)
    btn.config(bg="red")
    btn.config(command=cc)
    btn.config(text=k)
    btn.place(relx=random.random(), rely=random.random())

# 제일 처음 버튼을 눌렀을 때
def btn_f():
    global num_t    # 전역변수로 선언
    global start
    num_t = int(ent.get())
    # win.grid_slaves()   # pack_slaves, place_slaves     : gird, pack, place를 사용한 리스트
    for wg in win.grid_slaves():
        wg.destroy()    # 요소 삭제
    win.geometry("500x500")
    ran_btn()
    start = datetime.now()


# Button
btn = Button(win)
btn.config(text="시작")
btn.config(command=btn_f)
btn.grid(column=0, row=1, columnspan=2)


win.mainloop()
