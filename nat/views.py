from django.shortcuts import render, get_object_or_404
from rssparser import *
from models import *


def home(request):
    parse_rss()
    articles = Article.objects.all()
    newscategories = NewsCategory.objects.all()
    rssfeeds = RssFeed.objects.all()
    context = {
        'articles': articles,
        'newscategories': newscategories,
        'rssfeeds': rssfeeds,
    }
    return render(request, 'nat/home.html', context)


def about(request):
    return render(request, 'nat/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'nat/article.html', {'article': article})


def show_category(request, newscategory_id):
    category = get_object_or_404(NewsCategory, id=newscategory_id)
    articles = category.article_set.all()
    context = {
        'articles': articles,
        'category': category,
    }
    return render(request, 'nat/category.html', context)


def show_feed(request, feed_id):
    feed = get_object_or_404(RssFeed, id=feed_id)
    articles = feed.article_set.all()
    context = {
        'articles': articles,
        'feed': feed,
    }
    return render(request, 'nat/feed.html', context)
