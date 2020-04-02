from django.urls import path
from common import views

urlpatterns = [
    path('question/', views.question, name='question'),
    path('index/', views.index, name='index'),
    path('', views.index),
    path('question/<int:questionId>', views.question_detail)
]
