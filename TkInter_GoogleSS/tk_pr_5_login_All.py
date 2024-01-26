from tkinter import *
# Daum 로그인 해보기 (Chrome Webdriver 필요)
from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.by import By

win = Tk()
win.title("Log-in")
win.geometry("700x400")
win.option_add("*Font", "맑은고딕 20")
win.title("라벨")
win.configure(bg="#6ba4ff")

def idInput():
    print(entID)

def pwInput():
    print(entPW)

def clear(event):
    if entID.get() == "temp@temp.com":
        entID.delete(0, len(entID.get()))

def logon():
    # ChromeOptions 객체 생성
    chrome_options = webdriver.ChromeOptions()

    # 같은 폴더 아니면 절대경로
    chrome_path = "C:/Users/AI06/Documents/_Pr_1/Python/py_spreadsheet/chromedriver-win64"

    # WebDriver 생성 시에 options 매개변수로 ChromeOptions 객체 전달
    driver = webdriver.Chrome(options=chrome_options)

    # Daum 로그인 페이지
    url = "https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net#login"
    driver.get(url)
    driver.implicitly_wait(3) # 연결 시간을 주고 기다림. 그 전이라도 연결되면 넘어감.

    xpath1 = "//input[@name='loginId']"
    xpath2 = "//input[@name='password']"
    xpath3 = "//button[@class='btn_g highlight submit']"
    driver.implicitly_wait(3) 

    # 글자 입력
    driver.find_element(By.XPATH, xpath1).send_keys(entID.get())
    driver.implicitly_wait(3) 
    driver.find_element(By.XPATH, xpath2).send_keys(entPW.get())
    driver.implicitly_wait(3) 
    driver.find_element(By.XPATH, xpath3).click()
    driver.implicitly_wait(3) 
    # 브라우저 열린 상태 유지
    # 주: 이 명령을 맨 마지막에 진행하지 않으면 이후 코드도 진행이 안 됨.
    input("Press Enter to close.")  # 터미널 입력 받을 때까지 대기.

    # 브라우저 종료
    lab3.config(text = "Welcome")
    driver.quit()

# 이미지 삽입(라벨)
lab3 = Label(win)
img = PhotoImage(file = "arduino_oled_logo_1.png", master = win)
img = img.subsample(2)  # 이미지를 반으로 줄임
lab3.config(image=img)
lab3.pack()

# id 라벨
lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()

# id 입력창
entID = Entry(win)
entID.insert(0, "temp@temp.com")
entID.bind("<Button-1>", clear)
entID.pack()

# pw 라벨
lab2 = Label(win)
lab2.config(text="PW")
lab2.pack()

# pw 입력창
entPW = Entry(win)
entPW.config(show="*")
entPW.pack()

# login button
btn = Button(win)
btn.config(text="Sign On")
btn.config(command=logon)
btn.pack()

# 환영 메시지
lab3 = Label(win)
lab3.pack()

win.mainloop()
