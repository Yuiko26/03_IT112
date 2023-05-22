from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('books/', views.book_list, name='book_list'),
               path('', views.index, name='index'),
               path('books/<int:pk>/', views.details, name='details')]
