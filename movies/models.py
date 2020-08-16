from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField('First Name', max_length=50)

    updated_at = models.DateTimeField("updated at", auto_now=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)

class Movie(models.Model):
    id = models.IntegerField("Movie Id", primary_key=True)
    name = models.CharField("Movie Name", max_length=100)
    avg_rating = models.FloatField("Average Rating")

class UserList(models.Model):
    codename = models.CharField("Code Name", max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_list = models.ManyToManyField(Movie)