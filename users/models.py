from django.db import models
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# Create your models here.
class User(models.Model):
    user_name = models.CharField('User Name', max_length=50, unique=True, default=get_random_string(10))

    updated_at = models.DateTimeField("updated at", auto_now=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
