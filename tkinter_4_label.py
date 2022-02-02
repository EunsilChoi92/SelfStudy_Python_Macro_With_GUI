import time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By

win = Tk()
win.title("Daum Log-in")
win.geometry("400x300")
win.option_add("*Font", "궁서 20")

# 다음 로고
lab_d = Label(win)
img = PhotoImage(file="D:/WORKSPACE/workspace_python/macro_with_gui/daum_logo.png", master=win)
img = img.subsample(2) # 그림 크기 설정, 8 = 1/2로 줄이겠다는  뜻
lab_d.config(image=img)
lab_d.pack()

# id 라벨
lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()

# id 입력창
ent1 = Entry(win)
ent1.insert(0, "아이디")
def clear(event):
    if ent1.get() == "아이디":
        ent1.delete(0, len(ent1.get())) # 0부터 입력된 텍스트 길이 -1까지 삭제
ent1.bind("<Button-1>", clear)  # 왼쪽 마우스가 클릭되면 clear 함수 실행
ent1.pack()

# pw 라벨
lab2 = Label(win)
lab2.config(text="Password")
lab2.pack()

# 입력창
ent2 = Entry(win)
ent2.config(show="*")
ent2.pack()

# 로그인 버튼


btn = Button(win)
btn.config(text="로그인")
def login():
    my_id = ent1.get()
    my_pw = ent2.get()
    print(my_id, my_pw)

    # 로그인 과정
    driver = webdriver.Chrome("D:/temp/chromedriver.exe")
    url = "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net"
    driver.get(url)
    driver.implicitly_wait(5)

    xpath1 = "//input[@id='id']"
    driver.find_element(By.XPATH, xpath1).send_keys(my_id)
    driver.implicitly_wait(5)

    xpath2 = "//input[@id='inputPwd']"
    driver.find_element(By.XPATH, xpath2).send_keys(my_pw)
    driver.implicitly_wait(5)

    xpath3 = "//button[@id='loginBtn']"
    driver.find_element(By.XPATH, xpath3).click()

    # 로그인 성공 텍스트갸 뜸
    lab3.config(text="로그인 성공")

btn.config(command=login)
btn.pack()

# 메시지 라벨
lab3 = Label(win)
lab3.pack()


win.mainloop()