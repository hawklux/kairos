from tkinter import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑음고딕 20")

def clicking():
    txtAll = lb.curselection()
    txt1 = lb.curselection()[0] # 선택한 번호 중 첫째 받기
    lab.config(text=txtAll)    
    print(txtAll)
    print(txt1)

#Listbox
lb = Listbox(win)
lb.config(selectmode = "multiple") # 복수선택
lb.insert(0, "1번")
lb.insert(1, "2번")
lb.insert(2, "3번")
lb.insert(3, "4번")
lb.pack()

#Button
btn = Button(win)
btn.config(text="옵션선택")
btn.config(command = clicking)
btn.pack()

#Label
lab = Label(win)
lab.pack()


win.mainloop()