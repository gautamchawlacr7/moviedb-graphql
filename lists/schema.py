import graphene
from graphene_django import DjangoObjectType
from .models import UserList, User, Movie
from movies.schema import MovieType
from graphql import GraphQLError

class UserListType(DjangoObjectType):
    class Meta:
        model = UserList

class Query(graphene.ObjectType):
    user_lists = graphene.List(UserListType, user_id=graphene.Int(), codename=graphene.String())
    recommendations = graphene.List(MovieType, codename=graphene.String())

    def resolve_userlists(self, info, user_id=None, codename=None, **kwargs):
        if user_id:
            if User.objects.filter(pk=user_id).exists():
                user = User.objects.filter(pk=user_id)
                if UserList.objects.filter(user=user).exists():
                    user_lists = UserList.objects.filter(user=user)

                    return userlists
            else:
                raise GraphQLError("User Does Not Exist.")
        elif codename:
            if UserList.objects.filter(codename=codename).exists():
                user_lists = UserList.objects.filter(codename=codename)
            else:
                raise GraphQLError("No list exists with the given codename")

        return UserList.objects.all()

class CreateUserList(graphene.Mutation):
    user_id = graphene.Int()
    codename = graphene.String()

    class Arguments:
        user_id = graphene.Int()
        codename = graphene.String()

    def mutate(self, info, user_id, codename):
        if User.objects.filter(pk=user_id).exists():
            user = User.objects.filter(pk=user_id)

            if UserList.objects.filter(codename=codename).exists():
                raise GraphQLError("List with the given codename exists")
                userlist = UserList.objects.create(user=user, codename=codename)
                userlist.save()

                return CreateUserList(
                    user=userlist.user,
                    codename=userlist.codename,
                    movie_list = userlist.movie_list,
                )
