from django.db import models

class Data(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()
# Create your models here.
