from django.urls import path

# import views
from .views import QuizAPIView, QuestionAPIView, OptionAPIView, ResultAPIView

urlpatterns = [
    path('quiz_view/<int:pk>/', QuizAPIView.as_view()),
    path('question_view/', QuestionAPIView.as_view()),
    path('option_view/', OptionAPIView.as_view()),
    path('result_view/', ResultAPIView.as_view()),
]

