"""import graphene
from graphene_django import DjangoObjectType
from .models import UserList, User

class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    movies = graphene.List(Movie)

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()

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

        return CreateLink(
            id=movie.id,
            title=movie.title,
            avg_rating=movie.avg_rating,
        )

class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()"""