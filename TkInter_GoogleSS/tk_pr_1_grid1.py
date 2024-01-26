from tkinter import *

win = Tk()
win.geometry("700x500")
win.title("Grid n Place")
win.option_add("*Font", "맑은고딕 20")

# 4x3 버튼 array
btn_list = []
col_num = 4
row_num = 3
for i in range(0, row_num):
    for j in range(0, col_num):
        btn = Button(win)
        btn.config(text=f"({i},{j})")
        btn.grid(column=j, row=i, padx=2, pady=2)
        btn_list.append(btn)

# 버튼 병합 = 큰 새버튼으로 위를 덮어쓰는 방식임. 그리드는 편집될 수 없음.
btn_long = Button(win)
btn_long.config(text="(2,0)")
btn_long.grid(column = 3, row = 0, rowspan=2)
btn_long.config(width=5, height=3)

btn_wide = Button(win)
btn_wide.config(text="(1,2)")
btn_wide.grid(column=1, row=2, columnspan=2)
btn_wide.config(width=10, height=1)

# for b in btn_list:
#     print(b.cget("text"))
win.mainloop()
