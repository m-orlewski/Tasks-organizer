from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.ListAuthor.as_view()),
    path('authors/<int:pk>/', views.DetailAuthor.as_view()),
    path('items/', views.ListToDoItem.as_view()),
    path('items/<int:pk>/', views.DetailToDoItem.as_view()),
]