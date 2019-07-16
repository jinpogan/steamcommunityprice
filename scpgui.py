
def pickaduiofile():
    filepath = filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = (("mp3 files","*.mp3"),("wav files","*.wav"),("all files","*.*")))
    filename, file_extension = os.path.splitext(filepath)
    cp(filepath,"./alarm"+file_extension)
    if file_extension == ".mp3":
        sound = AudioSegment.from_mp3("./alarm.mp3")
        sound.export("./alarm.wav", format="wav")
def alarmt(text,balarm):
    if balarm != True:
        wave_obj = sa.WaveObject.from_wave_file("./alarm.wav")
        play_obj = wave_obj.play()
        #playsound('''./alarm.mp3''')
    turtle.setup(width = 1.0, height = 1.0)
    turtle.colormode(255)
    turtle.speed(0)
    turtle.color(rand(0,255), rand(0,255), rand(0,255))
    turtle.write(text, align="center",font=("Arial", 70, "normal"))
    if balarm == True:
        for x in range(60):
            time.sleep(0.5)
            turtle.bgcolor(rand(0,255), rand(0,255), rand(0,255))
            print ('\a')
    else:
        for x in range(60):
            turtle.bgcolor(rand(0,255), rand(0,255), rand(0,255))
            time.sleep(0.5)
def start():
    tk.destroy()
    print(gameappid.get())
    print(itemname.get())
    print(timebc.get())
    price=getprice(gameappid.get(),itemname.get())
    startprice = price
    while(1):
        price=getprice(gameappid.get(),itemname.get())
        print(price)
        if startprice != price:
            if startprice > price:

                try:
                    alarmt('''\\!PRICE DECREASED!/''',False)
                except:
                    try:
                        alarmt('''\\!PRICE DECREASED!/''',False)
                    except:
                        alarmt('''\\!PRICE DECREASED!/''',True)
            else:
                try:

                    alarmt('''\\!PRICE INDECREASED!/''',False)
                except:
                    try:
                        alarmt('''\\!PRICE INDECREASED!/''',False)
                    except:
                        alarmt('''\\!PRICE INDECREASED!/''',True)
        time.sleep(int(timebc.get()))

def getprice(appid,itemname):
    itemname=urllib.parse.quote(str(itemname)).replace("★","%E2%98%85")

    #print("=============",itemname)
    #print("s;dkfl;",'''curl "https://steamcommunity.com/market/priceoverview/?appid='''+appid+'''&currency=1&market_hash_name=''' + itemname +'''"''')
    pricejson = os.popen('''curl "https://steamcommunity.com/market/priceoverview/?appid='''+appid+'''&currency=1&market_hash_name=''' + itemname +'''"''').read()
    # example CSGO 730 Sticker%20|%20Kawaii%20Killer%20Terrorist PUBG 578080 %5BBATTLESTAT%5D%20Industrial%20Security%20-%20AKM
    pricejson = json.loads(pricejson)
    priceincents = pricejson["lowest_price"].replace("$","").replace(".","").replace(",","")
    return priceincents
import os
import time
import json
from random import randint as rand
import tkinter
import turtle
from pydub import AudioSegment
import simpleaudio as sa
from shutil import copy2 as cp
from tkinter import filedialog
import urllib.parse
from tkinter.constants import *
tk = tkinter.Tk()
tk.title("Steam Community Price Checker")
label = tkinter.Label(text="Steam Community Price Checker")
label.place(x=0,y=0)
tk.geometry("480x340")
e5=tkinter.Label(tk,text='''Steam game's appid:''').place(x=0,y=30)
e6=tkinter.Label(tk,text='''Item's full name:''').place(x=0,y=70)
e7=tkinter.Label(tk,text='''Seconds between each check:''').place(x=0,y=110)
e7=tkinter.Label(tk,text='''Alarm sound file (mp3/wav):''').place(x=0,y=150)

gameappid = tkinter.StringVar()
itemname = tkinter.StringVar()
timebc = tkinter.StringVar()
e1 = tkinter.Entry(tk,textvariable=gameappid)
e2 = tkinter.Entry(tk,textvariable=itemname)   #用*号代替用户输入的内容
e3 = tkinter.Entry(tk,textvariable=timebc)
e4=tkinter.Button(tk,text='Chose',command=pickaduiofile).place(x=220,y=150)
e1.place(x=220,y=30)
e2.place(x=220,y=70)
e3.place(x=220,y=110)
b2=tkinter.Button(tk,text='OK',command=start).place(x=20,y=190)
b3=tkinter.Button(tk,text='Quit',command=tk.destroy).place(x=80,y=190)
#Exterior: Field-Tested
help=tkinter.Message(tk,width=480,text='''If you are checking csgo prices,ou have include the exterior. For example,if you want to check ★ Flip Knife | Autotronic's with the field tested exterior. You should enter ★ Flip Knife | Autotronic (Field-Tested). If this still doesn't work, you should make the item name url friendly. For example: ★ Flip Knife | Autotronic (Field-Tested) will be %E2%98%85%20Flip%20Knife%20%7C%20Autotronic%20%28Field-Tested%29.    !!!App may freeze after you click start.!!!''').place(x=0,y=210)

tk.mainloop()
