from django.urls import path

# import views
from .views import QuizAPIView, QuestionAPIView, OptionAPIView, AnswerAPIView, ResultAPIView, CreateQuizAPIView, CreateQuestionAPIView, CreateAnswerAPIView,\
    CreateOptionAPIView, CreateResultAPIView

urlpatterns = [
    path('quiz_view/<int:pk>/', QuizAPIView.as_view()),
    path('question_view/<int:pk>/', QuestionAPIView.as_view()),
    path('option_view/<int:pk>/', OptionAPIView.as_view()),
    path('answer_view/<int:pk>/', AnswerAPIView.as_view()),
    path('result_view/<int:pk>/', ResultAPIView.as_view()),

    path('create_quiz/', CreateQuizAPIView.as_view()),
    path('create_question/', CreateQuestionAPIView.as_view()),
    path('create_option/', CreateOptionAPIView.as_view()),
    path('create_answer/', CreateAnswerAPIView.as_view()),
    path('create_result/', CreateResultAPIView.as_view()),
]

