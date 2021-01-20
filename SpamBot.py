import pyautogui
import time

print("1 - Text File Spam")
print("2 - Customized message spam")
print("3 - CSGO All Chat")

x = int(input("Which option would you like?"))
if x == 1:
    while True:
        filename = str(input('Input a file name:'))
        f = open(filename, "r")
        n = input("start spam?: y/n")
        time.sleep(5)
        if n == 'y':
            for word in f:
                pyautogui.typewrite(word)
                pyautogui.press('enter')
        else:
            time.sleep(5)
elif x == 2:
    word = input("Input message you would like to spam:")
    t = int(input("Set delay:"))
    while True:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(t)
elif x ==3:
    word = input("Input message you would like to spam:")
    t = int(input("Set delay:"))
    while True:
        pyautogui.press('y')
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(t)
        

