from django.apps import AppConfig
from tmdbv3api import Movie, Account, Authentication, TMDb
import os

popular = None
latest = None
upcoming = None

class MoviesConfig(AppConfig):
    name = 'movies'
    def ready(self):
        global popular
        global latest
        global upcoming
        tmdb = TMDb()
        tmdb.api_key = os.environ.get("API_KEY")
        movie = Movie()

        popular = movie.popular()
        latest = movie.latest()
        upcoming = movie.upcoming()
