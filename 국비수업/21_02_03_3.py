from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

root = Tk()

# 버튼 클릭 이벤트 핸들러
def okClick():
    name = txt.get()
    messagebox.showinfo("이름",name)

def okClick2():
    # v = simpledialog.askstring('전화번호', '핸드폰번호')
    # messagebox.showinfo("핸드폰번호",v)
    v = simpledialog.askinteger('나이', '나이 입력')
    messagebox.showinfo("나이",v)

lbl = Label(root, text = "이름")
lbl.grid(row=0, column = 0)

txt = Entry(root)
txt.grid(row=0, column = 1)
txt.insert(0, '이름') # 글상자에 0번 자리에 기본값 '이름' 입력

#txt.bind("<Return>", txtReturn)
txt.bind("<Return>", okClick)
# 버튼 클릭 이벤트와 핸들러 정의
btn = Button(root, text="OK", command=okClick)

btn.grid(row=1, column=0)

btn = Button(root, text="Input", command=okClick)

btn.grid(row=1, column=1)

root.mainloop()