import pyautogui
import pytesseract
import time
import random
import os
import boto3

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
    #client.get_document_analysis(image)

def solve_current_question():
    global answer
    try:
        # try:
        #     extNum1 = int(read_image(capture_screen(c.Region1)))
        # except ValueError as ve:
        #     print("first shot error:", ve)
        #     extNum1 = 7
        # try:
        #     extNum2 = int(read_image(capture_screen(c.Region2)))
        # except ValueError as ve:
        #     print("second shot error:" , ve)
        #     extNum2 = 7
        #capture_screen(c.Region1).save("r1.png")
        #capture_screen(c.Region2).save("r2.png")
        box = capture_screen(c.answerbox)
        boxText = read_image(box)
        hasVal = False
        for i in range(boxText.len()):
            if (boxText[i] == "-"):
                numEnd = i
                i = boxText.len()
            if (not hasVal):
                try:
                    int(boxText[i])
                except:
                    hasVal = False
                else:
                    val = int(boxText[i])
                    hasVal = True
                if (hasVal):
                    try: 
                        int(boxText[i+1])
                    except:
                        doubdig = False
                    else:
                        valtwo = int([i+1])
                        doubdig = True
        
        if (doubdig):
            extNum1 = (val * 10) + (valtwo)
        else:
            extNum1 = val

        hasVal = False
        for i in range(boxText.len() - numEnd):
            j = i + numEnd
            if (not hasVal):
                try:
                    int(boxText[j])
                except:
                    hasVal = False
                else:
                    val = int(boxText[j])
                    hasVal = True
                if (hasVal):
                    try: 
                        int(boxText[j+1])
                    except:
                        doubdig = False
                    else:
                        valtwo = int([j+1])
                        doubdig = True
        
        if (doubdig):
            extNum2 = (val * 10) + (valtwo)
        else:
            extNum2 = val
            
        print("extNum1:"+extNum1+"ExtNum2:"+extNum2)
        answer = (extNum1) - (extNum2)
    except ValueError as ve:
        print("ValueError occurred:", ve)
        ValError=True
    except Exception as e:
        print("ERROR:",e,". RETAKING ANSWER SS")

    try:
        for x in range(4):
            ssa = capture_screen(c.answer_regions[x])
            #ssa.save("SSATEST.png")
            extAns = int(pytesseract.image_to_string(ssa, config=custom_config).strip())

            print("X:",x)
            print("EXTANS:",extAns)
            print("ANSWER:",answer)
            if ((extAns == answer)):
                clear()
                print("ANSWER FOUND! BUTTON PRESSED:"+str(x+1))
                pyautogui.press(str(x+1))
                return
    except ValueError as ve:
        print("ValueError occurred:", ve)
        ValError=True
    except Exception as e:
        print("ERROR:",e,". RETAKING ANSWER SS")
    

while True:
    solve_current_question()
    time.sleep(1)
    #pyautogui.displayMousePosition()
    

# solve_current_question()