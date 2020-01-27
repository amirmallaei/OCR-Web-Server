from django.shortcuts import render
import pytesseract
import io
import base64
from PIL import Image
import requests
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from myapp.models import MyOCR
from django.utils.crypto import get_random_string
from myapp.tasks import Delayed_OCR

#the image_sync function which return OCR instantly via REST API
@csrf_exempt
def image_sync(request):
    if request.method == "POST":
        try:
            encoded_string=request.POST.get('image_data')
            this_text=OCR(encoded_string)
        except:
            this_text=''

        return JsonResponse({'text':this_text
        },  encoder=JSONEncoder,content_type="application/json", charset='utf-8')




# the image Function which gives OCR string by post Method and return by get method
@csrf_exempt
def image(request):

    if request.method=="POST":

        try:
            encoded_string=request.POST.get('image_data')
            this_task_id=get_random_string(length=15)
            newOCR= MyOCR.objects.create(task_id=this_task_id,image=encoded_string,text='')
            Delayed_OCR.delay(this_task_id)
        except:
            this_text=None




        return JsonResponse({'task_id':this_task_id
        },  encoder=JSONEncoder,content_type="application/json", charset='utf-8')

    if request.method=="GET":

        this_task_id=request.GET.get('task_id')

        if MyOCR.objects.filter(task_id=this_task_id).exists():
            Requested_OCR= MyOCR.objects.get(task_id=this_task_id)

            if Requested_OCR !='':
                this_text=Requested_OCR.text
            else:
                this_text=None

        return JsonResponse({'task_id':this_text
        },  encoder=JSONEncoder,content_type="application/json", charset='utf-8')



# The OCR  base64 function
def OCR(encoded_string):
    # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    if encoded_string !='':
        img=io.BytesIO(base64.b64decode(encoded_string))
        imgfile=Image.open(img)
        this_text= pytesseract.image_to_string(imgfile)
        imgfile.close()
    return this_text
