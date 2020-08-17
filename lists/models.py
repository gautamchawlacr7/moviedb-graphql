from django.db import models
from movies.models import Movie
from django.contrib.auth import get_user_model
# Create your models here.
class UserList(models.Model):
    codename = models.CharField("Code Name", max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie_list = models.ManyToManyField(Movie, blank=True)