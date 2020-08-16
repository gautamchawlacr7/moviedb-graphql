from tmdbv3api import Account, Authentication, TMDb
from tmdbv3api import Movie as mv
from movies.models import Movie
import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Seeding Movies into database from The Movie DB API"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        tmdb = TMDb()
        tmdb.api_key = os.environ.get("API_KEY")
        movie = mv()

        self.pop = movie.popular()
        self.lat = movie.latest()
        self.up = movie.upcoming()

        #print(self.pop)
        #print(self.lat)
        #print(self.up)

        self.popular_objs = [
            Movie(
                id=self.pop[i].id,
                name=self.pop[i].title,
                avg_rating=self.pop[i].vote_average
            )
            for i in range(len(self.pop))
        ]
        print(type(self.popular_objs[0]))

        self.upcoming_objs = [
            Movie(
                id=self.up[i].id,
                name=self.up[i].title,
                avg_rating=self.up[i].vote_average
            )
            for i in range(len(self.up))
        ]

        p_movies = Movie.objects.bulk_create(self.popular_objs, ignore_conflicts=True)
        if Movie.objects.filter(pk=self.lat.id).exists():
            pass
        else:
            l_movie = Movie.objects.create(id=self.lat.id, name=self.lat.title, avg_rating=self.lat.vote_average)
        u_movies = Movie.objects.bulk_create(self.upcoming_objs, ignore_conflicts=True)