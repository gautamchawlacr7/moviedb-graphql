import graphene
from graphene_django import DjangoObjectType
from .models import User
from lists.models import UserList

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(UserType, id=graphene.Int(), username=graphene.String())

    def resolve_users(self, info, id=None, username=None, **kwargs):
        if id:
            if User.objects.filter(pk=id).exists():
                return User.objects.filter(pk=id)

        if username:
            if User.objects.filter(user_name=username).exists():
                return User.objects.filter(user_name=username)

        users = User.objects.all()
        return users

class CreateUser(graphene.Mutation):
    user_name = graphene.String()

    class Arguments:
        user_name = graphene.String()

    def mutate(self, info, user_name):
        user = User.objects.create(user_name=user_name)
        user.save()

        return CreateUser(
            user_name=user.user_name
        )

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

