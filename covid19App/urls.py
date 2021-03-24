from django.contrib import admin
from django.urls import path,include
from covid19App import views

urlpatterns = [
    path('',views.index,name='index')
]
