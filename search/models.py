from django.db import models


class History(models.Model):
    title = models.TextField()


class Data(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()
    category = models.TextField(null=True, default="other")

class Org(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()

class News(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()

class Research(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()

class Academic(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()

# Create your models here.
