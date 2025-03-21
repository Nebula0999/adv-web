from django.shortcuts import render
import requests
from django.views.generic import ListView
from django.http import HttpResponse
import random

API_KEY = '7f0a7839b5704f76aff87ad71ac1553c'

def home(request):
    url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7f0a7839b5704f76aff87ad71ac1553c'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    paginate_by = 6

    context = {
        'articles': articles
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
# Create your views here.
