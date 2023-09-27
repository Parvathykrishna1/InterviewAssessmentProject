from django.db import models

# Create your models here.
class CapturedImage(models.Model):
    capturedimage=models.ImageField(upload_to='media/')
    emotion=models.CharField(max_length=100)
    confidence=models.FloatField()