from tkinter import *
win = Tk()
win.title("Log-in")
win.geometry("700x400")
win.option_add("*Font", "맑은고딕 20")
win.title("라벨")
win.configure(bg="#6ba4ff")

def idInput():
    print(entID)

def pwInput():
    print(entPW)

def btnLogin():
    print("ID: ", entID.get())
    print("PW: ", entPW.get())
    lab3.config(text = "Welcome")

def clear(event):
    if entID.get() == "temp@temp.com":
        entID.delete(0, len(entID.get()))

# 이미지 삽입(라벨)
lab3 = Label(win)
img = PhotoImage(file = "arduino_oled_logo_1.png", master = win)
img = img.subsample(2)  # 이미지를 반으로 줄임
lab3.config(image=img)
lab3.pack()

# id 라벨
lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()

# id 입력창
entID = Entry(win)
entID.insert(0, "temp@temp.com")
entID.bind("<Button-1>", clear)
entID.pack()

# pw 라벨
lab2 = Label(win)
lab2.config(text="PW")
lab2.pack()

# pw 입력창
entPW = Entry(win)
entPW.config(show="*")
entPW.pack()

# login button
btn = Button(win)
btn.config(text="Sign On")
btn.config(command=btnLogin)
btn.pack()

# 환영 메시지
lab3 = Label(win)
lab3.pack()

win.mainloop()
