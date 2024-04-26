import pyautogui
import pytesseract
import time
import random

import masonConstents as c
# import maxConstents as c

botDetectionPrevention = False

custom_config = r'--oem 3 --psm 6 outputbase digits'

def capture_screen(region):
    return pyautogui.screenshot(region=region)

def solve_current_question():
    ssr1 = capture_screen(c.Region1)
    ssr2 = capture_screen(c.Region2)
    ssr1.save("r1.png")
    ssr2.save("r2.png")

    extNum1 = pytesseract.image_to_string("r1.png", config=custom_config)
    extNum2 = pytesseract.image_to_string("r2.png", config=custom_config)
    answer = str(int(extNum1) - int(extNum2))
    print("ExtNum1:"+extNum1)
    print("ExtNum2:"+extNum2)
    print("Answer:"+answer)
    for x in range(4):
        ssa = capture_screen(c.answer_regions[x])
        ssa.save("ssa"+str(x)+".png")
        extAns = pytesseract.image_to_string("ssa.png", config=custom_config).strip()

#     for x in range(4):
#         ssa = capture_screen(answer_regions[x])
#         extAns = pytesseract.image_to_string(ssa, config=custom_config).strip()

#         print("X:",x)
#         print("EXTANS:",extAns)
#         print("ANSWER:",answer)
#         if (extAns == answer):
#             print("WOW!")
#             pyautogui.press(str(x+1))

# while True:
#         solve_current_question()
#         if botDetectionPrevention:
#           time.sleep(0.01 + random.random())
#         else:
#           time.sleep(0.5)

solve_current_question()
while True:
    pyautogui.displayMousePosition()