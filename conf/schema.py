import graphene

import links.schema


# inherits the query in links/schema.py
# to keep every schema isolated in apps
class Query(links.schema.Query, graphene.ObjectType):
    pass


class Mutation(links.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)