from django.urls import path
from . import views

urlpatterns = [
    path('scroll', views.index, name ='index'),
    path('scroll/post', views.post, name = 'post'),
]