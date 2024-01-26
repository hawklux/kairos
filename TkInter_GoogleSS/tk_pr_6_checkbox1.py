from tkinter import *

win = Tk()
win.geometry("700x500")
win.title("Checkbox")
win.option_add("*Font", "맑은고딕 20")
win.configure(bg="#6ba4ff")

def checking():
    cl = []
    if ch1.get() == 1: #주: 버튼(cb1)이 아닌 객체(cv1)의 값!
        cl.append(1)
    if ch2.get() == 1:
        cl.append(2)
    if ch3.get() == 1:
        cl.append(3)
    print(cl)

#Checkbox 생성
ch1, ch2, ch3 = IntVar(), IntVar(), IntVar()
cb1 = Checkbutton(win, text="1번", variable=ch1)
cb2 = Checkbutton(win, text="2번", variable=ch2)
cb3 = Checkbutton(win, text="3번", variable=ch3)
cb1.pack()
cb2.pack()
cb3.pack()

#Button
btn = Button(win)
btn.config(text="옵션 선택")
btn.config(command=checking)
btn.pack()

win.mainloop() 