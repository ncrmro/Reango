from graphene import Node, AbstractType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from .models import Question as QuestionModal, Choice as ChoiceModal


class Question(DjangoObjectType):
    class Meta:
        model = QuestionModal
        interfaces = (Node,)

class Choice(DjangoObjectType):
    class Meta:
        model = ChoiceModal
        interfaces = (Node,)


class PollQueries(AbstractType):
    questions = DjangoFilterConnectionField(Question)