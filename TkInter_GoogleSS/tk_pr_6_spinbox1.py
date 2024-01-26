from tkinter import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.title("Spinbox")

def clicking():
    spVal = sp.get()
    lab.config(text=spVal)
    
# Spinbox
sp = Spinbox(win)
sp.config(from_=-1, to=3)
sp.pack()

# Button
btn = Button(win)
btn.config(text="선택")
btn.config(command=clicking)
btn.pack()

# Label
lab = Label(win)
lab.pack()

win.mainloop()