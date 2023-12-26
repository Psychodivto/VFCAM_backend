import graphene

from graphene_django.types import DjangoObjectType

from sistema.models import Question, Userprofile

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "nombre", "anios", "peso", "imc", "objetivo", "cuentame", "pub_date", "user")

class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    all_users = graphene.List(QuestionType)
    

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return Userprofile.objects.all()
    

schema = graphene.Schema(query=Query)
