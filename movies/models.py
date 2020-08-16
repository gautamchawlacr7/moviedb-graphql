from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField("Movie Id", primary_key=True)
    name = models.CharField("Movie Name", max_length=100)
    avg_rating = models.FloatField("Average Rating")