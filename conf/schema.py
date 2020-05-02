import graphene
import graphql_jwt # implement JWT TOkens for user authentication

import links.schema
import users.schema


# inherits the query in links/schema.py
# to keep every schema isolated in apps
class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)