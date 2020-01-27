import pytesseract
from PIL import Image
import requests
import base64
import io

url="http://127.0.0.1:8000/image/"#-sync/"
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


with open("phototest.tiff", "rb") as image_file:
     encoded_string = base64.b64encode(image_file.read())

# print(mystr)
# doc=io.BytesIO(base64.b64decode(encoded_string))



dic={
'image_data':encoded_string,
# 'task_id':task_id
}

r = requests.post(url, data = dic)
# r=requests.get(url,data=dic)
# print (r.json()['text'])
print (r.json()['task_id'])
