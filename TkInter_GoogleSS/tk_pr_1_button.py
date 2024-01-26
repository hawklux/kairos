from tkinter import *
from datetime import datetime

def alert():
    cur = datetime.now()
    cur_str = cur.strftime("%Y년 %m월 %d일 %H:%M:%S")
    cur_w = len(str(cur))  # 현재시간 글자수
    btn.config(width=cur_w+2, height=2) # 버튼폭 = 글자수+2
    btn.config(text = f"{cur_str}")
    print(cur)

win = Tk()
win.geometry("700x500")  # 픽셀
win.title("Remo")
win.option_add("*Font","맑은고딕 25")
win.configure(bg="#6ba4ff")

btn = Button(win)
btn.config(width=7, height=2) # 글자 폰트 크기*7, 폰트 크기*2
btn.config(text="현재 시각")
btn.config(command=alert) 
# command 옵션에 alert 함수를 할당해둠.
# alert함수를 실행해서 command에 대입하는 것이 아니므로 alert()이 아님.

btn.pack(pady = 20)
win.mainloop()