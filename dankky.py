#in the command line type 'pip install PyAutoGUI' and 'pip install keyboard'
from time import sleep
import random
import keyboard
import pyautogui
import os

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

s=False

print('''
      Dank Memer HACKS
  -------------------------
  i ~ Information
  v ~ Version



By: User./Black Rose
''')

if keyboard.read_key() == 'i':
  clear()
  print('''
      Information
  ---------------------
  This is a Dank Memer Hack
  made my me "User./Black Rose" I have 
  tested this hack and it is
  almost impossible to get 
  banned but if you do you 
  are responsible for using 
  it to start the hack press
  "s"

  ''')
  sleep(10)
  clear()

if keyboard.read_key() == 'v':
  clear()
  print('Verson 0.0.1')

if keyboard.read_key() == 's':
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
def waste():
  profile = "pls profile"
  presteige = "pls prestige"
  shop = "pls presteige"
  meme = "pls meme"
  waste = [profile,presteige,shop,meme]
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
  waste()
  waitS()
  pyautogui.press('enter')
  waitL()

