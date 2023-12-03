from django.contrib import admin
from django.urls import path,include
from health_assessment import views

urlpatterns = [
    path("",views.index,name='home'),
    path("bmi",views.bmi,name='bmi'),
    path("gr1",views.gr1,name='gr1'),    
]
