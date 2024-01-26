from tkinter import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕")
win.title("Scale Slidebar")

def clicking():
    scVal=sc.get()
    lab.config(text=scVal)

# Scale
sc = Scale(win)
sc.config(from_=0, to=180, orient=HORIZONTAL)
sc.config(length=500, tickinterval=10) # 눈금. 없어도 됨.
sc.pack()

# Button
btn = Button(win)
btn.config(text="선택")
btn.config(command=clicking)
btn.pack()

# Label
lab = Label(win)
lab.pack()


win.mainloop()