from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'), 
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('questions/', views.questions_view, name='questions'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('answer/<int:pk>/like/', views.like_answer, name='like_answer'),
]
