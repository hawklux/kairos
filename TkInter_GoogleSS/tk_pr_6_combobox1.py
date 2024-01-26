from tkinter import *
from tkinter.ttk import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.title("Combobox")

def clicking():
    cboxVal = cbox.get()
    lab.config(text=cboxVal)

#Combobox
cbox_list = ["1", "2", "3"]
cbox = Combobox(win)
cbox.config(values = cbox_list)
cbox.pack()

#Button
btn = Button(win)
btn.config(text="선택")
btn.config(command=clicking)
btn.pack()

#Label
lab = Label(win)
lab.pack()

win.mainloop()