from django.urls import path
from .views import (
    quiz_view, quiz_data_view, save_quiz_view
)
from . import views

app_name = 'quizes'

urlpatterns = [
    #path('quizindex', QuizListView.as_view(), name='main-view'),
    path('quizindex', views.main_view, name='main-view'),
    path('quizindex/<pk>/', quiz_view, name='quiz-view'),
    path('quizindex/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('quizindex/<pk>/save/', save_quiz_view, name='save-view'),

]