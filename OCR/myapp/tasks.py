from OCR.celery import app
from myapp.models import MyOCR
import io
import base64
from PIL import Image
import pytesseract

@app.task
def Delayed_OCR(this_task_id):
    undone_task= MyOCR.objects.get(task_id=this_task_id)
    this_text= OCR(undone_task.image)
    undone_task.text=this_text
    undone_task.save()


@app.task
def OCR(encoded_string):
    # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    if encoded_string !='':
        img=io.BytesIO(base64.b64decode(encoded_string))
        imgfile=Image.open(img)
        this_text= pytesseract.image_to_string(imgfile)
        imgfile.close()
    return this_text
