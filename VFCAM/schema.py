import graphene

import sistema.schemas.questions

class Query(sistema.schemas.questions.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)