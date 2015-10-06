from django.shortcuts import render, get_object_or_404
from nat.rssparser import *


def home(request):
    parse_rss()
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'nat/home.html', context)


def about(request):
    return render(request, 'nat/about.html')


def login(request):
    return render(request, 'nat/login.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'nat/article.html', {'article': article})
