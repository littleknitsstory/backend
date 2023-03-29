import graphene

import src.apps.blog.schema
from src.apps.blog.schema import Mutation


class Query(src.apps.blog.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
