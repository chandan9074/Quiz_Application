from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializer import QuestionSerializer, QuizSerializer, AnswerSerializer, OptionSerializer, ResultSerializer
from .models import Quiz, Question, Answer, Option, Result


# Create your views here.

# view quiz by their users api

class QuizAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (Quiz.objects.filter(user_profile=pk)).exists():
            serializer_data = Quiz.objects.filter(user_profile=pk)
            serializer = QuizSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        quiz_objects = Quiz.objects.get(id=pk)
        serializer = QuizSerializer(quiz_objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create quiz api

class CreateQuizAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view question by quiz id api

class QuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (Question.objects.filter(quiz=pk)).exists():
            seializer_data = Question.objects.filter(quiz=pk)
            serializer = QuestionSerializer(seializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        ques_object = Question.objects.get(id=pk)
        serializer = QuestionSerializer(ques_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create question api

class CreateQuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view options by their question id api

class OptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if(Option.objects.filter(question=pk)).exists():
            seializer_data = Option.objects.filter(question=pk)
            serializer = OptionSerializer(seializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        option_object = Option.objects.get(id=pk)
        serializer = OptionSerializer(option_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create option api

class CreateOptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view answer by it question id api

class AnswerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (Answer.objects.filter(question=pk)).exists():
            seializer_data = Answer.objects.get(question=pk)
            serializer = AnswerSerializer(seializer_data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# create answer api

class CreateAnswerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view results by its quiz api

class ResultAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (Result.objects.filter(quiz=pk)).exists():
            seializer_data = Result.objects.filter(quiz=pk)
            serializer = ResultSerializer(seializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# create results api

class CreateResultAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)