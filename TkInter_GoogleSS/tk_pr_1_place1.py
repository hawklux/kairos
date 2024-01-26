from tkinter import *

win = Tk()
win.geometry("700x500")
win.title("Place")
win.option_add("*Font", "맑은고딕 20")

# 절대좌표: 창 크기가 바뀌어도 위치 불변 (x= , y= )
x_, y_ = 20, 30
btnA = Button(win)
btnA.config(text=f"({x_},{y_})")
btnA.place(x=x_, y=y_)

# 상대좌표: 창 크기에 따라 위치 변함 (relx= , rely= )
btnR = Button(win)
relx_, rely_ = 0.2, 0.3
btnR.config(text=f"({relx_},{rely_})")
btnR.place(relx=relx_, rely=rely_)

win.mainloop()