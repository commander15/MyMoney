from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField("id", primary_key=True)
    name = models.CharField("name", max_length=25)
    login = models.CharField("login", max_length=20)
    password = models.CharField("password", max_length=20)