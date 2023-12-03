from django.contrib import admin
from django.urls import path
from health_guidelines import views

urlpatterns = [
    path("",views.index,name='home'),
    # path("reduce_stress/",views.reduce_stress,name='reduce_stress'),
]
