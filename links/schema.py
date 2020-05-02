import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all() # return all the links


# defines a mutation class
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    # defines the data you can send to the server
    class Arguments:
        url = graphene.String()
        description = graphene.String()


    # the mutation method:
    # 1. creates a link in the DB
    # 2. returns CreateLink class with the data just created
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id = link.id,
            url = link.url,
            description = link.description,
        )


# creates a mutation class with a field to be resolved
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()