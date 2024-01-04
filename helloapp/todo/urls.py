from django.contrib import admin
from django.urls import include, path
from todo import views

urlpatterns = [
    path('todo/',views.index ,name='todo'),
    path('del/<str:item_id>', views.remove, name="del"),
]
