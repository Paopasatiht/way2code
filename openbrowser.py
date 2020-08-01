#print(('Hello World'+' '+'\n')*3)

'''

'''
import pyautogui as gui
import time
import webbrowser as wb
import pyperclip as cp

url = 'http://www.google.com'
wb.open(url)

#Ch = (525,1049)
SE = (684,498)

#gui.doubleClick(Ch, duration=2)
gui.doubleClick(SE, duration=2)

#time.sleep(3)
gui.write('Pyautogui writing')

gui.press('Enter')

def Search(word):
    time.sleep(3)
    for i in range(7):
        gui.press('tab')

    gui.press('backspace')
    gui.write(word)
    gui.press('Enter')
              
    time.sleep(3)
    gui.screenshot(word+'.png')

def SearchTH(word):
    time.sleep(3)
    for i in range(7):
        gui.press('tab')

    
    cp.copy(word)
    time.sleep(3)
    gui.hotkey('ctrl','v')
    gui.press('Enter')
              
    time.sleep(3)
    gui.screenshot(word+'.png')


#Search('JoJo')
#Search('www.time.com')
SearchTH('สวัสดีจ้า')

    
