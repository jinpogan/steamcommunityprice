import turtle
import simpleaudio as sa
import time
from random import randint as rand
balarm = True
if balarm != True:
    wave_obj = sa.WaveObject.from_wave_file("./alarm.wav")
    play_obj = wave_obj.play()
    #playsound('''./alarm.mp3''')
turtle.setup(width = 1.0, height = 1.0)
turtle.colormode(255)
turtle.speed(0)
turtle.color(rand(0,255), rand(0,255), rand(0,255))
turtle.write("dlsjf", align="center",font=("Arial", 70, "normal"))
if balarm == True:
    for x in range(60):
        turtle.bgcolor(rand(0,255), rand(0,255), rand(0,255))
        print ('\a')
        time.sleep(0.5)

else:
    for x in range(60):
        turtle.bgcolor(rand(0,255), rand(0,255), rand(0,255))
        time.sleep(0.5)
