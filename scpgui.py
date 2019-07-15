def rstart():
    thread = threading.Thread(target=start, args=())
    thread.daemon = True                            # Daemonize thread
    thread.start()
def start():



    stop = False
    print(gameappid.get())
    print(itemname.get())
    print(timebc.get())

    if stop == True:
        pass
    else:
        price=getprice(gameappid.get(),itemname.get())
        startprice = price
        while(1):


            if stop == True:
                break
            price=getprice(gameappid.get(),itemname.get())
            print(price)
            if startprice != price:
                if startprice > price:
                    print("sdafasFDasfda")
                else:
                    print("sdaf")
            tk.after(int(timebc.get())*1000)

def getprice(appid,itemname):
    pricejson = os.popen('''curl "https://steamcommunity.com/market/priceoverview/?appid='''+appid+'''&currency=1&market_hash_name=''' + itemname +'''"''').read()
    # example CSGO 730 Sticker%20|%20Kawaii%20Killer%20Terrorist PUBG 578080 %5BBATTLESTAT%5D%20Industrial%20Security%20-%20AKM
    pricejson = json.loads(pricejson)
    priceincents = pricejson["lowest_price"].replace("$","").replace(".","").replace(",","")
    return priceincents
def stopr():
    global stop
    if stop == True:
        tk.destroy()
        quit()
    stop=True
import threading
import os
import json
import tkinter
stop=True
#from tkinter.constants import *
tk = tkinter.Tk()
tk.title("Steam Community Price Checker")
label = tkinter.Label(text="Steam Community Price Checker")
label.place(x=0,y=0)
tk.geometry("480x190")
e5=tkinter.Label(tk,text='''Steam game's appid:''').place(x=0,y=30)
e6=tkinter.Label(tk,text='''Item's full name:''').place(x=0,y=70)
e7=tkinter.Label(tk,text='''Seconds between each check:''').place(x=0,y=110)
gameappid = tkinter.StringVar()
itemname = tkinter.StringVar()
timebc = tkinter.StringVar()
e1 = tkinter.Entry(tk,textvariable=gameappid)
e2 = tkinter.Entry(tk,textvariable=itemname)   #用*号代替用户输入的内容
e3 = tkinter.Entry(tk,textvariable=timebc)
e1.place(x=220,y=30)
e2.place(x=220,y=70)
e3.place(x=220,y=110)
b2=tkinter.Button(tk,text='OK',command=rstart).place(x=20,y=150)
b3=tkinter.Button(tk,text='Cancel',command=stopr).place(x=80,y=150)
tk.mainloop()
