from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Question, Choice


class QuestionSerializer(ModelSerializer):
    """Django polls Question model serializer"""

    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(ModelSerializer):
    """Django polls Question model serializer"""

    class Meta:
        model = Choice
        fields = '__all__'
