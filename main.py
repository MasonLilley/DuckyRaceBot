import pyautogui
import pytesseract
import time
import random
import os

import masonConstants as c
# import maxConstents as c

botDetectionPrevention = False

answer = 0

clear = lambda: os.system('cls')

custom_config = r'--oem 3 --psm 6 outputbase digits'

def capture_screen(region):
    return pyautogui.screenshot(region=region)

def read_image(image):
    return pytesseract.image_to_string(image, config=custom_config).strip()

def solve_current_question():
    global answer
    try:
        extNum1 = str(abs(int(read_image(capture_screen(c.Region1)))))
        extNum2 = str(abs(int(read_image(capture_screen(c.Region2)))))
        capture_screen(c.Region1).save("r1.png")
        capture_screen(c.Region2).save("r2.png")
        print("extNum1:"+extNum1+"ExtNum2:"+extNum2)
        answer = str(int(extNum1) - int(extNum2))
    except ValueError as ve:
        print("ValueError occurred:", ve)
        ValError=True
    except Exception as e:
        print("ERROR:",e,". RETAKING ANSWER SS")

    for x in range(4):
        ssa = capture_screen(c.answer_regions[x])
        ssa.save("SSATEST.png")
        extAns = pytesseract.image_to_string(ssa, config=custom_config).strip()

        print("X:",x)
        print("EXTANS:",extAns)
        print("ANSWER:",answer)
        if ((extAns == answer)):
            clear()
            print("ANSWER FOUND! BUTTON PRESSED:"+str(x+1))
            pyautogui.press(str(x+1))
            return

while True:
        solve_current_question()

# solve_current_question()