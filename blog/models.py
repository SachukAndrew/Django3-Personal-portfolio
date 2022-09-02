from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(max_length=250)