import pyautogui
import pytesseract
import boto3
import requests
from PIL import Image
from pytesseract import pytesseract
import easyocr

reader = easyocr.Reader(['en'])

#client = boto3.client('rekognition', region_name='us-east-1')
custom_config = r'--oem 3 --psm 6 outputbase digits'
URL = "https://api.ocr.space/parse/image"; 
APIKEY = "K88051715288957"

def capture_screen(region):
    return pyautogui.screenshot(region=region)

masonPCRegion = (850, 650, (1000-850), (700-650)) #Region to screenshot on Mason's PC
maxPCRegion = (40, 600, 700, 270,) #Window in top left conner of creen, scrolled all the way up. screen as big as it expands, then stop

#screenshot = capture_screen(masonPCRegion)
screenshot = capture_screen(maxPCRegion)
screenshot.save("screenshot.png")

#with open('screenshot.png', 'rb') as f:
    # OCR.SPACE!!
    # payload = {
    #     'apikey': APIKEY,
    #     'language': 'eng',
    # }

    # response = requests.post(URL, files={'file': f}, data=payload)

    # AWS!!
    #response = client.detect_text(Image={'Bytes': f.read()})

# AWS!!
#extracted_text = '\n'.join([text['DetectedText'] for text in response['TextDetections']])
# Tesseract!!

image = Image.open("screenshot.png")
extracted_text = pytesseract.image_to_string(image)
print("Extracted text:"+extracted_text)

#result = reader.readtext('screenshot.png', detail=0)
#print(result)

extracted_text = pytesseract.image_to_string("screenshot.png", config=custom_config)
print("Extracted text:"+extracted_text+"END")

