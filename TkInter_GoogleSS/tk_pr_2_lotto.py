from tkinter import *
import requests   # pip install requests
from bs4 import BeautifulSoup  # pip install BeautifulSoup4

# 로또 번호 크롤링으로 불러오기
def lotto():
    roundN = ent.get()  # 입력창의 입력값
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={roundN}"
    # div class="win_result"
    req = requests.get(url)
    htmlSrc = req.text
    soup = BeautifulSoup(htmlSrc, "html.parser")
    divTxt = soup.find("div", attrs={"class","win_result"}).get_text()
    winNum = divTxt.split("\n")[7:13]
    bonusNum = divTxt.split("\n")[-4]
    print("당첨번호", winNum)
    print("보너스번호", bonusNum)

# 입력창 만들기
win = Tk()
win.geometry("700x400")
win.option_add('*Font', 'Arial 20')
win.title("입력창")
win.configure(bg="#6ba4ff")

ent = Entry(win)
btn = Button(win)
btn.config(text= "로또당첨번호 확인")
btn.config(command=lotto)

btn.pack(pady=20)
ent.pack()
win.mainloop()

