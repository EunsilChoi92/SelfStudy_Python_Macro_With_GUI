from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.geometry("300x100")
win.option_add("*Font", "궁서 20")

# 입력창 생성
ent = Entry(win)
ent.pack()

# 회차를 입력하면 그 회차의 로또 당첨 번호를 받아서 출력하는 함수
def lotto_p():
    n = ent.get()   # 입력된 문자
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)   # 회차별 당첨번호 url
    req = requests.get(url) # url에서 데이터를 받아옴
    soup = BeautifulSoup(req.text, "html.parser")   # 받아온 데이터를 보기 쉽도록 정리
    txt = soup.find("div", attrs={"class","win_result"}).get_text() # 데이터에서 div 중 class 이름이 win_result인 태그의 text를 받아옴
    num_list = txt.split('\n')[7:13]    # 받아온 text를 개행으로 나누고 거기서 로또 번호만 슬라이싱함
    bonus = txt.split("\n")[-4]     # 보너스 번호만 슬라이싱

    print(num_list)
    print(bonus)

btn = Button(win)
btn.config(text="로또 당첨 번호 확인")
btn.config(command=lotto_p)
btn.pack()

win.mainloop()

