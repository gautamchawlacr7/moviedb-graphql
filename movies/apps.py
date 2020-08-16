from django.apps import AppConfig
from tmdbv3api import Movie, Account, Authentication, TMDb
import os

class MoviesConfig(AppConfig):
    name = 'movies'
    def ready(self):
        tmdb = TMDb()
        tmdb.api_key = os.environ.get("API_KEY")
        movie = Movie()

        popular = movie.popular()
        latest = movie.latest()
        upcoming = movie.upcoming()

