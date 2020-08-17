import graphene
from graphene_django import DjangoObjectType
from .models import User
from lists.models import UserList

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(UserType, username=graphene.String())

    def resolve_users(self, username=None, **kwargs):
        if username:
            if User.objects.filter(pk=username).exists():
                user = User.objects.filter(pk=username)
                return {"user":user, "list_of_movies":UserList.objects.filter(user=user)}

            else:
                return {"message": "User Does Not Exist"}

        users = User.objects.all()
        return users

class CreateUser(graphene.Mutation):
    user_name = graphene.String()

    class Arguments:
        user_name = graphene.String()

    def mutate(self, user_name):
        user = User.objects.create(user_name=user_name)
        user.save()

        return CreateUser(
            user_name=user.user_name,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

