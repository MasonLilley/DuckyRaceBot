import pyautogui
import pytesseract
import time
import os

#client = boto3.client('textract')

#import masonConstants as c
import maxConstents as c

botDetectionPrevention = False

answer = 0

clear = lambda: os.system('cls')

custom_config = '--oem 3 --psm 6 outputbase digits tessedit_char_whitelist=12345689 tessedit_char_blacklist=.-'

def capture_screen(region):
    shot = pyautogui.screenshot(region=region)
    shot.save("View.png")
    return shot

def read_image(image):
    return pytesseract.image_to_string(image, config=custom_config).strip()

def solve_current_question():
    global answer
    
    try:
        box = capture_screen(c.answerbox)
        boxText = read_image(box)
        answer = eval(boxText)
        print("Answer:",answer)
    except Exception as e:
        print("ERROR:",e)

        for x in range(4):
            ssa = capture_screen(c.answer_regions[x])\

            try:
                extAns = int(pytesseract.image_to_string(ssa, config=custom_config).strip())
            except Exception as e:
                print("Error:",e)

            if (extAns == answer):
                clear()
                print("ANSWER FOUND! BUTTON PRESSED:"+str(x+1))
                pyautogui.press(str(x+1))
                return

print("hi")
while True:
    solve_current_question()
    time.sleep(1)
    #pyautogui.displayMousePosition()
    

