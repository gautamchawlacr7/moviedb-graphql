import graphene
import movies.schema
import users.schema


class Query(movies.schema.Query, users.schema.Query, graphene.ObjectType):
    pass

class Mutation(movies.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)