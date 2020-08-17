import graphene
import movies.schema
import users.schema
import graphql_jwt
import lists.schema

class Query(movies.schema.Query, users.schema.Query, lists.schema.Query, graphene.ObjectType):
    pass

class Mutation(movies.schema.Mutation, users.schema.Mutation, lists.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)