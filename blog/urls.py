# Python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # assign a view called post_list to root URL - if someone enters website, gets redirected to views.post_list
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]