def test():
    print("sadfasdfasdfasdf")
import tkinter
#from tkinter.constants import *
tk = tkinter.Tk()
tk.title("Steam Community Price Checker")
label = tkinter.Label(text="Steam Community Price Checker")
label.place(x=0,y=0)
tk.geometry("360x260")
e5=tkinter.Label(tk,text='''Steam game's appid:''').place(x=0,y=30)
e6=tkinter.Label(tk,text='''Item's full name:''').place(x=0,y=70)
e7=tkinter.Label(tk,text='''Time between each check:''').place(x=0,y=110)
v1 = tkinter.StringVar()
v2 = tkinter.StringVar()
v3 = tkinter.StringVar()

e1 = tkinter.Entry(tk,textvariable=v1)
e2 = tkinter.Entry(tk,textvariable=v2)   #用*号代替用户输入的内容
e3 = tkinter.Entry(tk,textvariable=v3)
e1.place(x=160,y=30)
e2.place(x=160,y=70)
e3.place(x=160,y=110)
b2=tkinter.Button(tk,text='OK',command=test).place(x=20,y=150)
tk.mainloop()
