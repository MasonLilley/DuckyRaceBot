import pyautogui
import pytesseract
import boto3
import requests
from PIL import Image

#client = boto3.client('rekognition', region_name='us-east-1')
URL = "https://api.ocr.space/parse/image"; 
APIKEY = "K88051715288957"

def capture_screen(region):
    return pyautogui.screenshot(region=region)

masonPCRegion = (850, 650, (1000-850), (700-650)) #Region to screenshot on Mason's PC

screenshot = capture_screen(masonPCRegion)
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
extracted_text = pytesseract.image_to_string(screenshot)
print("Extracted text:"+extracted_text)