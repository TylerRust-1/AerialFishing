from random import random

import time

import pyautogui
import keyboard

if __name__ == '__main__':
    screenWidth, screenHeight = pyautogui.size()
    print(screenWidth, screenHeight)
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)

    im1 = pyautogui.screenshot()
    # im1.show()

    while (1):
        if keyboard.is_pressed('b'):
            break
        time.sleep(random())
        try:
            locate = pyautogui.locateOnScreen('Spot.png', confidence=.7,
                                              region=(700, screenHeight // 2, 1220, screenHeight))
        except:
            print("Item not found")

        '''
        try:
            #Right half of the screen
            #locate = pyautogui.locateOnScreen('Green.png', confidence=.3, region=(screenWidth//2, 0, screenWidth, screenHeight))

            #Bottom half of the screen
            locate = pyautogui.locateOnScreen('Green.png', confidence=.5,
                                              region=(700, screenHeight//2, 1220, screenHeight))

        except:
            try:
                # Right half of the screen
                #locate = pyautogui.locateOnScreen('Blue.png', confidence=.3,
                 #                                 region=(screenWidth//2, screenHeight//2, screenWidth, screenHeight))

                # Bottom half of the screen
                locate = pyautogui.locateOnScreen('Blue.png', confidence=.3,
                                                  region=(700, screenHeight//2, 1220, screenHeight))
     
            except:
                print("Item not found")
        print(locate)
        '''
        try:
            area = pyautogui.center(locate)
            pyautogui.moveTo(area)
            pyautogui.click()
        except:
            continue
