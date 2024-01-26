from tkinter import *

win = Tk()
win.geometry("500x700")
win.option_add("*Font", "맑은고딕 20")
win.config(bg="#6ba4ff")
win.title("Slider")

def sliding(v):
    label.config(text=f"현재값: {v}")

# 슬라이더 생성
sl = Scale(win, from_=0, to_=180, orient=HORIZONTAL, command=sliding) # TkInter는 command가 자동으로 sliding 함수에 현재값을 전달하도록 되어있으므로 v를 받아야 함.
sl.pack(pady=20)

label = Label(win, text="현재값: 0")
label.pack(pady=10)


win.mainloop()