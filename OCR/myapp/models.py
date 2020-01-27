from django.db import models

# Create your models here.
class MyOCR(models.Model):
    task_id=models.CharField(max_length=15,unique=True)
    image=models.TextField()
    text=models.TextField()


    def __str__(self):
        return self.task_id
