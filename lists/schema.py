import graphene
from graphene_django import DjangoObjectType
from .models import UserList, Movie
from movies.schema import MovieType
from graphql import GraphQLError
from django.contrib.auth import get_user_model
from django.db.models import Q
from tmdbv3api import TMDb
from tmdbv3api import Movie as mv
import os
from users.schema import UserType

def get_movie(movie_id):
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

class UserListType(DjangoObjectType):
    class Meta:
        model = UserList

class Query(graphene.ObjectType):
    user_lists = graphene.List(UserListType, codename=graphene.String())
    #recommendations = graphene.List(MovieType, codename=graphene.String())

    def resolve_user_lists(self, info, codename=None, **kwargs):
        user = info.context.user
        print(user.id)
        if user.is_active:
            if UserList.objects.filter(user=user).exists():
                user_lists = UserList.objects.filter(user=user)
                if codename:
                    if user_lists.filter(codename=codename).exists():
                        user_lists = user_lists.filter(codename=codename)
                    else:
                        raise GraphQLError("No list exists with the given codename")

                return user_lists
            else:
                raise GraphQLError("No list exists by the current user")
        else:
            raise GraphQLError("Authentication Failure.")
        #return UserList.objects.all()



class CreateUserList(graphene.Mutation):
    codename = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        codename = graphene.String()

    def mutate(self, info, codename):
        user = info.context.user
        if user.is_active:
            if UserList.objects.filter(codename=codename).exists():
                raise GraphQLError("List with the given codename exists")
            else:
                user_list = UserList(user=user, codename=codename)
                user_list.save()

                return CreateUserList(
                    user=user_list.user,
                    codename=user_list.codename,
                    # movie_list=user_list.movie_list,
                )

        else:
            raise GraphQLError("Authentication Failure")

class AddMovie(graphene.Mutation):
    codename = graphene.String()
    movie_id = graphene.Int()
    class Arguments:
        codename = graphene.String()
        movie_id = graphene.Int()

    def mutate(self, info, codename, movie_id):
        user = info.context.user
        if user.is_active:
            if UserList.objects.filter(user=user).exists():
                user_lists = UserList.objects.filter(user=user)
                if UserList.objects.filter(codename=codename).exists():
                    user_list = user_lists.filter(codename=codename)
                    user_list.movie_list.add(get_movie(movie_id))

                    return AddMovie(
                        user=user_list.user,
                        codename=user_list.codename,
                        movie_list=user_list.movie_list,
                    )

                else:
                    raise GraphQLError("List with the given codename does not exist.")

        else:
            raise GraphQLError("Authentication Failure")



class Mutation(graphene.ObjectType):
    create_list = CreateUserList.Field()
    add_movie = AddMovie.Field()
