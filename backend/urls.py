from django.urls import path
from . import views
from .views import About, Contact, UserRegistration
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('technology', views.home, name='technology'),
    path('', views.random_article, name='index'),
    path('top-headlines', views.top_headlines, name='top-headlines'),
    path('trending', views.trending, name='trending'),
    path('fashion', views.fashion, name='fashion'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('search', views.search, name='search'),
    path('register', UserRegistration.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='backend/login.html'), name='login'),
    #path('search', views.search, name='search'),
]
