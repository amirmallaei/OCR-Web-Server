import os
import django

from celery import Celery

from django.conf import settings

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

os.environ.setdefault('DJANGO_SETTINGS_MODULE','OCR.settings')
django.setup()

app=Celery('OCR')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
