from tkinter import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.title("Radio Button")

def clicking():
    a = rv.get()
    lab.config(text=a)

# Radio Button
rv = IntVar()
rb1 = Radiobutton(win, text="#1", value=0, variable=rv)
rb2 = Radiobutton(win, text="#2", value=1, variable=rv)
rb3 = Radiobutton(win, text="#3", value=2, variable=rv)
rb1.pack()
rb2.pack()
rb3.pack()

# button
btn = Button(win)
btn.config(text="선택")
btn.config(command=clicking)
btn.pack()

# Label
lab = Label(win)
lab.pack()

win.mainloop()