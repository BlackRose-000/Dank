from tkinter import *
import random
import pyautogui
from time import sleep
import keyboard
s=False
clicked=True
slicked=True
def Start():
    global s,clicked
    if clicked==True:
        s=True
        clicked=False
    elif clicked == False:
        s=False
        clicked=False
    if slicked:
        pass
        

    
    def waitL():
        timeL=[37,40,45,47]
        timeL = random.choice(timeL)
        sleep(timeL)

    def waitS(): 
        timeS=[2,3.5,4.6,1]
        timeS = random.choice(timeS)
        sleep(timeS)
    def waste():
        profile = "pls profile"
        presteige = "pls prestige"
        shop = "pls presteige"
        meme = "pls meme"
        waste = [profile,presteige,shop,meme]
        randomw = random.choice(waste)
        pyautogui.typewrite(randomw)  

    while(s):
        waitS()
        pyautogui.typewrite("pls dig")
        waitS()
        pyautogui.press("enter")
        pyautogui.typewrite("pls fish")
        waitS()
        pyautogui.press('enter')
        pyautogui.typewrite("pls hunt")
        waitS()
        pyautogui.press('enter')
        pyautogui.typewrite("pls beg")
        waitS()
        pyautogui.press('enter')
        waste()
        waitS()
        pyautogui.press('enter')
        waitL()



root = Tk()
title = Label(root,text='Dank Bot')
title.pack()

start=Button(root,text ='Start',command=Start)
start.pack()
version=Label(root,text="Version 0.0.1")
version.config(borderwidth=0)
version.pack()
root.mainloop()

