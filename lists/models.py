from django.db import models
from movies.models import Movie
from users.models import User
# Create your models here.
class UserList(models.Model):
    codename = models.CharField("Code Name", max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_list = models.ManyToManyField(Movie)