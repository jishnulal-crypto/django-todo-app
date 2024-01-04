from django.contrib import admin
from django.urls import include, path
from hello import views


sample = 12

urlpatterns = [
    path('',views.index ,name='home')
]
