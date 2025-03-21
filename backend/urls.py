from django.urls import path
from . import views

urlpatterns = [
    path('technology', views.home, name='technology'),
    path('', views.random_article, name='index'),
]
