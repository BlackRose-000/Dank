#in the command line type 'pip install PyAutoGUI' and 'pip install keyboard'
from time import sleep
import random
import keyboard
import pyautogui
import os
from ctypes import windll, Structure, c_long, byref
from datetime import datetime
s=False

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


beg = True
dig=True
hunt =True
fish=True
crime=True
search=True
pm=True
sell = True

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
need to add any spaces if you don't want to remove any then press 'Enter' 

b ~ Beg
d ~ Dig
h ~ Hunt
f ~ Fish
c ~ Crime 
s ~ Search
p ~ Pm


''')

if 'b' in Setting:
  beg = False
if 'd' in Setting:
  dig = False
if 'h' in Setting:
  hunt= False
if 'f' in Setting:
  fish = False
if 'c' in Setting:
  crime = False
if 's' in Setting:
  search = False
if 'p' in Setting:
  pm = False


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
  waste = [profile,presteige,shop,meme]
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



while(s):
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
  if hunt==True:
    pyautogui.typewrite("pls hunt")
    waitS()
    pyautogui.press('enter')
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls hunt' ")
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
  print(f"[{current_time}] - [{Dank}] | Successfully sent commmand 'pls sell' ")
  pyautogui.leftClick(pos)
  waste()
  waitS()
  pyautogui.press('enter')
  waitL()

