from django.db import models

# Create your models here.

class Event(models.Model):
    eventName=models.CharField(max_length=200)
    eventDate=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    file=models.FileField(upload_to='/event')