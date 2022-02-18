from tkinter import *
root = Tk()
 
lbl = Label(root, text="이름")
lbl.pack()
 
txt = Entry(root)
txt.pack()
 
btn = Button(root, text="OK")
btn.pack()
 
root.mainloop()

#%%
from tkinter import *
root = Tk()
root.geometry("400x200") # 메인창의 너비와 높이(크기단위 픽셀) 
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)

btn = Button(root, text="OK", width=15) # 버튼 크기단위 글자 
btn.grid(row=1, column=0)
btn2 = Button(root, text="Cancle", width=15)
btn2.grid(row=1, column=1) 
root.mainloop()