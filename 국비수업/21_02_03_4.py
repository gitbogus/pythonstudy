from tkinter import *
root = Tk()
 
def click(event):
    print("클릭위치", event.x, event.y)
 
 
frame = Frame(root, width=300, height=300, background='skyblue')
 
 #왼쪽 마우스 버튼 바인딩
frame.bind("<Button-1>", click) 
 
frame.pack()
root.mainloop()