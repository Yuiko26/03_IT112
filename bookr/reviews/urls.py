from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('books/', views.book_list, name='book_list'),
               path('', views.index, name='index'),
               path('book_search', views.book_search, name='book_search'),
               path('books/<int:pk>/', views.details, name='book_detail')]
