from django.contrib import admin
from django.urls import path
from yoga import views

urlpatterns = [
    path("",views.index,name='home'),
    path("yoga/",views.index,name='home'),
    path('yoga/<str:yoga_name>/', views.yoga_view, name='yoga_view'),
]
