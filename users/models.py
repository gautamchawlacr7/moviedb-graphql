from django.db import models
import random
import string

# Create your models here.
class User(models.Model):
    user_name = models.CharField('User Name', max_length=50)

    updated_at = models.DateTimeField("updated at", auto_now=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
