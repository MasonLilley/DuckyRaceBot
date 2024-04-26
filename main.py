import pyautogui
import pytesseract
import time

custom_config = r'--oem 3 --psm 6 outputbase digits'

def capture_screen(region):
    return pyautogui.screenshot(region=region)

# Mason's PC Region Settings:
#first number
topLeftXfirst = 875
topLeftYfirst = 650
bottomRightXfirst = 920
bottomRightYfirst = 700
#second number
topLeftXsecond = 940
topLeftYsecond = 650
bottomRightXsecond = 990
bottomRightYsecond = 710
#first answer
topLeftX1 = 778
topLeftY1 = 733
bottomRightX1 = 800
bottomRightY1 = 770
#second answer
topLeftX2 = 875
topLeftY2 = 733
bottomRightX2 = 900
bottomRightY2 = 770
#third answer
topLeftX3 = 960
topLeftY3 = 733
bottomRightX3 = 1000
bottomRightY3 = 770
#fourth answer
topLeftX4 = 1050
topLeftY4 = 733
bottomRightX4 = 1100
bottomRightY4 = 770
Answer1 = (topLeftX1, topLeftY1, (bottomRightX1-topLeftX1), (bottomRightY1-topLeftY1))
Answer2 = (topLeftX2, topLeftY2, (bottomRightX2-topLeftX2), (bottomRightY2-topLeftY2))
Answer3 = (topLeftX3, topLeftY3, (bottomRightX3-topLeftX3), (bottomRightY3-topLeftY3))
Answer4 = (topLeftX4, topLeftY4, (bottomRightX4-topLeftX4), (bottomRightY4-topLeftY4))
Region1 = (topLeftXfirst, topLeftYfirst, (bottomRightXfirst-topLeftXfirst), (bottomRightYfirst-topLeftYfirst))
Region2 = (topLeftXsecond, topLeftYsecond, (bottomRightXsecond-topLeftXsecond), (bottomRightYsecond-topLeftYsecond))
answers_regions = [Answer1, Answer2, Answer3, Answer4]

def solve_current_question():
    ssr1 = capture_screen(Region1)
    ssr2 = capture_screen(Region2)
    ssr1.save("r1.png")
    ssr2.save("r2.png")

    extNum1 = pytesseract.image_to_string("r1.png", config=custom_config)
    extNum2 = pytesseract.image_to_string("r2.png", config=custom_config)
    answer = str(int(extNum1) - int(extNum2))
    print("ExtNum1:"+extNum1)
    print("ExtNum2:"+extNum2)
    print("Answer:"+answer)
    for x in range(4):
        ssa = capture_screen(answer_regions[x])
        ssa.save("ssa"+str(x)+".png")
        extAns = pytesseract.image_to_string("ssa.png", config=custom_config).strip()

#     for x in range(4):
#         ssa = capture_screen(answer_regions[x])
#         ssa.save("ssa.png")
#         extAns = pytesseract.image_to_string("ssa.png", config=custom_config).strip()

#         print("X:",x)
#         print("EXTANS:",extAns)
#         print("ANSWER:",answer)
#         if (extAns == answer):
#             print("WOW!")
#             pyautogui.press(str(x+1))

# while True:
#         solve_current_question()
#         time.sleep(3)
solve_current_question()