from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = 'movies'

    def __init__(self):
        print("Hello WOrld")
