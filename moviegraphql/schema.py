import graphene

import movies.schema


class Query(movies.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)