import graphene

from graphene_django.types import DjangoObjectType

from sistema.models import Question, Userprofile

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

        
class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()

schema = graphene.Schema(query=Query)
