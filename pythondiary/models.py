from django.db import models
from django.conf import settings

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)