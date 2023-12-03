from django.contrib import admin
from django.urls import path,include
from health_score import views

urlpatterns = [
    path("",views.index,name='home'),
    path("health_index",views.health_index,name='health_index'),
]
