# Python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
] # assign a view called post_list to root URL - if someone enters website, gets redirected to views.post_list