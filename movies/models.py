from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField('First Name', max_length=50)

    updated_at = models.DateTimeField("updated at", auto_now=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)

class UserList(models.Model):
    codename = models.CharField("Code Name", max_length=50, unique=True)
    movie_list = models.JSONField("Movie List")