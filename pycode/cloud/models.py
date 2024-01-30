from django.db import models
from django.urls import reverse

class Document(models.Model):
    title = models.CharField(max_length=255)
    docfile = models.FileField(upload_to='documents')
    owner = models.CharField(max_length=40)