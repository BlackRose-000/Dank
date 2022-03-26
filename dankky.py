#in the command line type 'pip install PyAutoGUI' and 'pip install keyboard'
from time import sleep
import random
import keyboard
import pyautogui
import os
from ctypes import windll, Structure, c_long, byref
from datetime import datetime
import threading
s=False

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


beg = True
dig=True
hunt =True
fish=True
search=True
pm=True
sell = True
crime=True
Setting = input('''

┏━━━┓╋╋┏┓╋┏┓
┃┏━┓┃╋┏┛┗┳┛┗┓
┃┗━━┳━┻┓┏┻┓┏╋┳━┓┏━━┳━━┓
┗━━┓┃┃━┫┃╋┃┃┣┫┏┓┫┏┓┃━━┫
┃┗━┛┃┃━┫┗┓┃┗┫┃┃┃┃┗┛┣━━┃
┗━━━┻━━┻━┛┗━┻┻┛┗┻━┓┣━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛

Type the letters of the commands you want to remove then press 'Enter' you do not
need to add any spaces if you don't want to remove any then press 'Enter' or you can
do 'N' if you do not want anything that might make you die

DISCLAIMER - Regradless of what the bot does there is still a chance for you to die.

b ~ Beg
d ~ Dig
h ~ Hunt
f ~ Fish
s ~ Search
p ~ Pm 
                                      Input: ''')


Setting1 = input('Do you have a \'Tip Jar\' (y/n): ')
tipjar=False
if 'b' in Setting:
  beg = False
if 'd' in Setting:
  dig = False
if 'h' in Setting:
  hunt= False
if 'f' in Setting:
  fish = False
if 's' in Setting:
  search = False
if 'p' in Setting:
  pm = False
if 'N' in Setting:
  search = False
  crime = False
if 'y' in Setting1:
  tipjar=True
else:
  tipjar == False
isint = True
while (isint):
    Setting2 =input("How many 'Pizzas' do you want to use : ")
    try:
        Setting2 =int(Setting2)
        isint=False
    except ValueError:
        print("Type in a number.")
        sleep(2)
        clear()
clear()
print('''
  
██████╗░░█████╗░███╗░░██╗██╗░░██╗
██╔══██╗██╔══██╗████╗░██║██║░██╔╝
██║░░██║███████║██╔██╗██║█████═╝░
██║░░██║██╔══██║██║╚████║██╔═██╗░
██████╔╝██║░░██║██║░╚███║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

IMPORTANT: Use the command  'pls sell' and put your mouse above\nthe confirm button until it says ready and the ding sound is \nplayed you have 20 Sec.if the mouse is not moving to the right way\nstop rerun the bot

GITHUB: https://github.com/BlackRose-000/Dank-Memer-Bot

INSTALLED VERSION: v0.2.2
''')

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    sleep(20)
    windll.user32.GetCursorPos(byref(pt))
    print('Dank : READY\n')
    return pt.x, pt.y
s=True
pos=queryMousePosition()


def waste():
  profile = "pls profile"
  presteige = "pls prestige"
  shop = "pls shop"
  meme = "pls meme"
  waste = [profile,shop,meme]
  randomw = random.choice(waste)
  pyautogui.typewrite(randomw)  
def wastee():
  profile = "pls profile"
  shop = "pls shop"
  meme = "pls meme"
  waste = [profile,shop,meme]
  randomw = random.choice(waste)
  pyautogui.typewrite(randomw)  

def waitL():
  timeL=[37,40,45,47]
  timeL = random.choice(timeL)
  sleep(timeL)

def waitS(): 
  timeS=[2,3.5,4.6,1]
  timeS = random.choice(timeS)
  sleep(timeS)




current_time = datetime.now()
Dank='\033[32m[Dank]\u001b[0m'
x=0
def pizza():
  global Setting2,x
  if Setting2 != x:
    pyautogui.press("enter")
    pyautogui.typewrite('pls use pizza') 
    pyautogui.press("enter")
    Setting2 -= 1
    

def tip():
  pyautogui.press("enter")
  pyautogui.typewrite('pls use tipjar') 
  pyautogui.press("enter")
pmin = 60*15
while (s):
  if tipjar== True:
    threading.Timer(360, tip).start()
  
  threading.Timer(pmin, pizza).start()
  
  if dig == True:
    pyautogui.typewrite("pls dig")
    waitS()
    pyautogui.press("enter")
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls dig' ")
  if fish==True:
    pyautogui.typewrite("pls fish")
    waitS()
    pyautogui.press('enter')
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls fish' ")
    waitS()
    pyautogui.moveTo(pos)
    pyautogui.leftClick(pos)
    pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
    pyautogui.leftClick(pos)
  if hunt==True:
    pyautogui.typewrite("pls hunt")
    waitS()
    pyautogui.press('enter')
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls hunt' ")
    waitS()
    pyautogui.moveTo(pos)
    pyautogui.leftClick(pos)
    pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
    pyautogui.leftClick(pos)
  if beg == True:
    pyautogui.typewrite("pls beg")
    waitS()
    pyautogui.press('enter')
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls beg' ")
  if search == True:
    pyautogui.typewrite('pls search')
    waitS()
    pyautogui.press('enter')
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls search' ")
    waitS()
    pyautogui.moveTo(pos)
    pyautogui.leftClick(pos)
    pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
    pyautogui.leftClick(pos)
  if crime == True:
    pyautogui.typewrite('pls crime')
    waitS()
    pyautogui.press('enter')
    waitS()
    pyautogui.moveTo(pos)
    pyautogui.leftClick(pos)
    pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
    pyautogui.leftClick(pos)
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls crime' ")
  if pm == True:
    pyautogui.typewrite('pls pm')
    waitS()
    pyautogui.press('enter')
    waitS()
    pyautogui.moveTo(pos)
    pyautogui.leftClick(pos)
    pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
    pyautogui.leftClick(pos)
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls pm' ")

  pyautogui.typewrite('pls sell')
  waitS()
  pyautogui.press('enter')
  waitS()
  pyautogui.moveTo(pos)
  pyautogui.leftClick(pos)
  pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
  print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls sell' ")
  pyautogui.leftClick(pos)
  waste()
  waitS()
  pyautogui.press('enter')
  waitL()

