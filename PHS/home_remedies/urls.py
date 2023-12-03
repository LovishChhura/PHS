from django.contrib import admin
from django.urls import path
from home_remedies import views

urlpatterns = [
    path("",views.index,name='home'),
    path("home_remedies/",views.index,name='home'),
    path('home_remedies/<str:home_remedies>/', views.home_remedies_view, name='home_remedies_view'),
]
