from tkinter import *
 
def keyPressed(event):
    # 키보드 문자하나 출력
    print(event.char)
 
root = Tk()
 
frame = Frame(root, width=100, height=100)
# Key 이벤트 바인딩
frame.bind('<Key>', keyPressed) 
frame.place(x=0, y=0)
 
# 키보드 포커를 갖게 한다
frame.focus_set()
 
root.mainloop()


from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog 
root = Tk()
 
# 버튼 클릭 이벤트 핸들러
def okClick(e):
    name = txt.get()
    messagebox.showinfo("이름", name)
    
def okClick2():
    #입력창
    # v= simpledialog.askstring('전화번호', '핸드폰번호 입력')#문자열   
    # messagebox.showinfo("핸드폰번호", v)
    v= simpledialog.askinteger('나이', '나이 입력') #정수
    messagebox.showinfo("나이", v)

# def txtReturn(e):
#     name = txt.get()
#     messagebox.showinfo("이름", name)
    
   
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)

txt = Entry(root)
txt.grid(row=0, column=1)
#txt.bind("<Return>",txtReturn) 
txt.bind("<Return>",okClick) 
# 버튼 클릭 이벤트와 핸들러 정의
##btn = Button(root, text="OK", command=okClick)  #command 방식은 이벤트객체전달 오류
btn = Button(root, text="OK")
btn.grid(row=1, column=0)
btn.bind("<Button-1>",okClick)
# 버튼 클릭 이벤트와 핸들러 정의
btn2 = Button(root, text="INPUT")
btn2.grid(row=1, column=1)
btn2.bind("<Button-1>",okClick2) 

 
root.mainloop()
