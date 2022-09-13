from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title