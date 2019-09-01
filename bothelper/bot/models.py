from django.db import models
from api.models import TelegramUser

# Create your models here.

class Region(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Message(models.Model):
    title = models.CharField(max_length=200)
    number = models.IntegerField(default=0)

    text = models.TextField()

    def __str__(self):
        return self.title

class PaySystem(models.Model):
    title = models.CharField(max_length=200)

    token = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Setting(models.Model):
    title = models.CharField(max_length=200)

    token = models.CharField(max_length=200)

    paysystem = models.ManyToManyField(PaySystem, default="")

    def __str__(self):
        return self.title


class Admin(models.Model):
    title = models.CharField(max_length=200)

    user = models.ManyToManyField(TelegramUser)




