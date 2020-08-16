import graphene
from graphene_django import DjangoObjectType
from .models import Movie
from django.db.models import Q
from tmdbv3api import TMDb
from tmdbv3api import Movie as mv
import os

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

#Query to get movies from the server
class Query(graphene.ObjectType):
    movies = graphene.List(MovieType, movie_id=graphene.Int())

    def resolve_movies(self, info, movie_id=None, **kwargs):

        if movie_id:

            if Movie.objects.filter(pk=movie_id).exists():
                return Movie.objects.filter(pk=movie_id)

            else:
                tmdb = TMDb()
                tmdb.api_key = os.environ.get("API_KEY")
                movie = mv()
                searched_movie = movie.details(movie_id)
                s_movie = Movie(id=searched_movie.id, name=searched_movie.title, avg_rating=searched_movie.vote_average)
                s_movie.save()
                return Movie.objects.filter(pk=movie_id)

        movies = Movie.objects.all()
        return movies

class CreateMovie(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    avg_rating = graphene.Float()

    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        avg_rating = graphene.Float()

    def mutate(self, info, id, title, avg_rating):
        movie = Movie(id=id, title=title, avg_rating=avg_rating)
        movie.save()

        return CreateMovie(
            id=movie.id,
            title=movie.title,
            avg_rating=movie.avg_rating,
        )

class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
