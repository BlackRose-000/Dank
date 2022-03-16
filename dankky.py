#in the command line type 'pip install PyAutoGUI' and 'pip install keyboard'
from time import sleep
import random
import keyboard
import pyautogui
import os
from ctypes import windll, Structure, c_long, byref


clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

s=False
sc=False
print('''
        IMPORTANT 
  ----------------------
  Use the command  pls sell 
  and put your mouse above the 
  confirm button until it says
  ready and the ding sound is 
  played you have 20 Sec.if the
  mouse is not moving to the right 
  stop rerun the bot
''')

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    sleep(20)
    windll.user32.GetCursorPos(byref(pt))
    clear()
    print("READY ")
    sleep(3)
    clear()
    return pt.x, pt.y

pos=queryMousePosition()




print('''
      Dank Memer BOT 
  -------------------------
  1 ~ Information
  2 ~ Version
  3 ~ Normal Run 
  4 ~ Crime # if you are ok with crimes
         

                        Vers 0.2.1
''')

choice = input("Chocie: ")

if choice == '1':
  clear()
  print('''
          Information
  -----------------------------
  This is a Dank Memer Bot
  made my me "User./Black Rose" 
  I have tested this bot/script and
  it is almost impossible to get 
  banned but if you do you 
  are responsible for using 
  this make sure to have a lot
  of life savers
  

  ''')
  sleep(20)
  clear()

elif choice == '2':
  clear()
  print('Verison 0.2.1')
  sleep(3)
  clear()

elif choice == '3':
  clear()
  print('The Bot will start in 5 ...')
  sleep(1)
  clear()
  print('The Bot will start in 4 ...')
  sleep(1)
  clear()
  print('The Bot will start in 3 ...')
  sleep(1)
  clear()
  print('The Bot will start in 2 ...')
  sleep(1)
  clear()
  print('The Bot will start in 1 ...')
  sleep(1)
  s = True
  clear()
elif choice == '4':
  clear()
  print('The Bot will start in 5 ...')
  sleep(1)
  clear()
  print('The Bot will start in 4 ...')
  sleep(1)
  clear()
  print('The Bot will start in 3 ...')
  sleep(1)
  clear()
  print('The Bot will start in 2 ...')
  sleep(1)
  clear()
  print('The Bot will start in 1 ...')
  sleep(1)
  sc = True
  clear()
else:
  clear()
  print('That is not one of the options...')
  sleep(3)


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


while(s):
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
  pyautogui.typewrite('pls search')
  waitS()
  pyautogui.press('enter')
  waitS()
  pyautogui.moveTo(pos)
  pyautogui.leftClick(pos)
  pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
  pyautogui.leftClick(pos)
  pyautogui.typewrite('pls sell')
  waitS()
  pyautogui.press('enter')
  waitS()
  pyautogui.moveTo(pos)
  pyautogui.leftClick(pos)
  pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
  pyautogui.leftClick(pos)
  waste()
  waitS()
  pyautogui.press('enter')
  waitL()

while(s):
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
  pyautogui.typewrite('pls search')
  waitS()
  pyautogui.press('enter')
  waitS()
  pyautogui.moveTo(pos)
  pyautogui.leftClick(pos)
  pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
  pyautogui.leftClick(pos)
  pyautogui.typewrite('pls crime')
  waitS()
  pyautogui.press('enter')
  waitS()
  pyautogui.moveTo(pos)
  pyautogui.leftClick(pos)
  pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
  pyautogui.leftClick(pos)
  pyautogui.typewrite('pls sell')
  waitS()
  pyautogui.press('enter')
  waitS()
  pyautogui.moveTo(pos)
  pyautogui.leftClick(pos)
  pyautogui.move(0, 50 , 1 , pyautogui.easeInQuad) 
  pyautogui.leftClick(pos)
  waste()
  waitS()
  pyautogui.press('enter')
  waitL()

