from django.contrib import admin
from django.urls import path
from exercises import views

urlpatterns = [
    path("",views.index,name='home'),
    path("exercise/",views.index,name='home'),
    path('exercise/<str:exercise_name>/', views.exercise_view, name='exercise_view'),
]
