from django.db import models

# Create your models here.

class Hashtag(models.Model):
    name = models.CharField(max_length=200)
    hashtag = models.CharField(max_length=100)
    modified = models.DateTimeField('date modified', auto_now_add=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.name
