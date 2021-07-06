from rest_framework import serializers
from .models import Quiz, Question, Option, Answer, Result


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        field = '__all__'
        extra_kwargs = {'description': {'required': False}, 'enrollment_key': {'required': False},
                        'attempt': {'required': False}}


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        field = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        field = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        field = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        field = '__all__'
