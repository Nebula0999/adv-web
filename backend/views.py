from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
import requests
from django.views.generic import ListView
from django.http import HttpResponse
import random
from .forms import UserRegistrationForm
from .models import User

API_KEY = '7f0a7839b5704f76aff87ad71ac1553c'

def search(request):
    query = request.GET.get('q', '')  # Get the search term from the query parameters
    articles = []

    if query:
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])

    context = {
        'query': query,
        'articles': articles,
    }
    return render(request, 'backend/search_results.html', context)

def home(request):
    url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7f0a7839b5704f76aff87ad71ac1553c'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    random_article = random.choice(articles) if articles else None
    random_2 = random.choice(articles) if articles else None
    random_3 = random.choice(articles) if articles else None
    random_4 = random.choice(articles) if articles else None
    more_n = random.choice(articles) if articles else None
    additional = random.choice(articles) if articles else None
    extra = random.choice(articles) if articles else None

    context = {
        'article': random_article,
        'random_1': random_2,
        'random_0': random_3,
        'random_5': random_4,
        'more': more_n,
        'additional': additional,
        'extra': extra

    }
    return render(request, 'backend/home.html', context)


def random_article(request):
    url = f'https://newsapi.org/v2/everything?domains=wsj.com&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    # Select a random article if articles are available
    random_article = random.choice(articles) if articles else None
    random_2 = random.choice(articles) if articles else None
    random_3 = random.choice(articles) if articles else None
    random_4 = random.choice(articles) if articles else None
    more_n = random.choice(articles) if articles else None
    additional = random.choice(articles) if articles else None
    extra = random.choice(articles) if articles else None

    context = {
        'article': random_article,
        'random_1': random_2,
        'random_0': random_3,
        'random_5': random_4,
        'more': more_n,
        'additional': additional,
        'extra': extra

    }
    return render(request, 'backend/index.html', context)

def top_headlines(request):
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    # Select a random article if articles are available
    random_article = random.choice(articles) if articles else None
    random_2 = random.choice(articles) if articles else None
    random_3 = random.choice(articles) if articles else None
    random_4 = random.choice(articles) if articles else None
    more_n = random.choice(articles) if articles else None
    additional = random.choice(articles) if articles else None
    extra = random.choice(articles) if articles else None

    context = {
        'article': random_article,
        'random_1': random_2,
        'random_0': random_3,
        'random_5': random_4,
        'more': more_n,
        'additional': additional,
        'extra': extra

    }
    return render(request, 'backend/business.html', context)
# Create your views here.
def trending(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    # Select a random article if articles are available
    random_article = random.choice(articles) if articles else None
    random_2 = random.choice(articles) if articles else None
    random_3 = random.choice(articles) if articles else None
    random_4 = random.choice(articles) if articles else None
    more_n = random.choice(articles) if articles else None
    additional = random.choice(articles) if articles else None
    extra = random.choice(articles) if articles else None

    context = {
        'article': random_article,
        'random_1': random_2,
        'random_0': random_3,
        'random_5': random_4,
        'more': more_n,
        'additional': additional,
        'extra': extra

    }
    return render(request, 'backend/trending.html', context)
def fashion(request):
    url = f'https://newsapi.org/v2/everything?q=apple&from=2025-03-22&to=2025-03-22&sortBy=popularity&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    # Select a random article if articles are available
    random_article = random.choice(articles) if articles else None
    random_2 = random.choice(articles) if articles else None
    random_3 = random.choice(articles) if articles else None
    random_4 = random.choice(articles) if articles else None
    more_n = random.choice(articles) if articles else None
    additional = random.choice(articles) if articles else None
    extra = random.choice(articles) if articles else None

    context = {
        'article': random_article,
        'random_1': random_2,
        'random_0': random_3,
        'random_5': random_4,
        'more': more_n,
        'additional': additional,
        'extra': extra

    }
    return render(request, 'backend/fashion.html', context)

class About(View):
    def get(self, request):
        return render(request, 'backend/about.html')
    
class Contact(View):
    def get(self, request):
        return render(request, 'backend/contacts.html')
    
class UserRegistration(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'backend/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form is valid, redirecting to Home page")
            return redirect('index')
        else:
            print("Form is not valid")
        return render(request, 'backend/register.html', {'form': form})
    
    class Login(View):
        def get(self, request):
            return render(request, 'backend/login.html')
# Create your views here.
