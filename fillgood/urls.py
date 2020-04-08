from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('survey/', views.survey, name='survey'),
    path('nutritionary/', views.nutritionary, name='nutritionary'),
    path('article/', views.article, name='article'),
    path('write/', views.write, name='write'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
]