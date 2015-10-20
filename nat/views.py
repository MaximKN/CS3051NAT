from django.shortcuts import render, get_object_or_404
from rssparser import *
from models import *
from nat.rssparser import *

region_specifier = 0;

def home(request):
    articles = Article.objects.all()
    newscategories = NewsCategory.objects.all()
    rssfeeds = RssFeed.objects.all()
    context = {
        'region_specifier': region_specifier,
        'articles': articles,
        'newscategories': newscategories,
        'rssfeeds': rssfeeds,
    }
    return render(request, 'nat/home.html', context)


def var(word, var):
    if var == 0:
        return word
    if var == 1:
        return word + " "
    if var == 2:
        return " " + word
    if var == 3:
        return " " + word + " "


def search(request):
    if 'q' in request.GET and request.GET['q']:
        # what the person types in for searching
        q = request.GET['q']
        q = q.lower()

        # new
        qString = q
        q = q.split()
        articles = []
        # finds all articles with a keyword contained in q

        for keyWord in q:
            tempList = Article.objects.filter(title__icontains=keyWord)
            tempList2 = Article.objects.filter(description__icontains=keyWord)
            articles += tempList
            articles += tempList2

        # filter multiple occurances of articles for different keywords
        for article in articles:
            while articles.count(article) > 1:
                articles.remove(article)

        if len(q) == 1:
            for article in articles:
                article.search_order = 0
                if (var(qString.lower(), 3) in article.title.lower()):
                    article.search_order += 50
                if var(qString.lower(), 3) in article.description.lower():
                    article.search_order += 25
                if len(qString) > 4:
                    if (qString.lower() in article.title.lower()):
                        article.search_order +=50
                    if (qString.lower() in article.title.lower()):
                        article.search_order +=25
        else:
            # find best articles to match higher search order = better
            for article in articles:
                article.search_order = 0
                if qString.lower() in article.title.lower():
                    article.search_order += 100
                if qString.lower() in article.description.lower():
                    article.search_order += 75
                for keyWord in q:
                    if var(keyWord.lower(), 0) in article.title.lower():
                        # print(article.search_order)
                        article.search_order += 20
                    if var(keyWord.lower(), 0) in article.description.lower():
                        article.search_order += 5

        # removing articles that failed to be relevant enough with the search
        articles[:] = [article for article in articles if (article.search_order >= 25)]

        for i in range(len(articles) - 1, 0, -1):
            for j in range(i):
                if articles[j].search_order < articles[j + 1].search_order:
                    temp = articles[j]
                    articles[j] = articles[j + 1]
                    articles[j + 1] = temp

        return render(request, 'nat/search_results.html', {'articles': articles, 'query': qString})
    else:
        return render(request, 'nat/search_results.html', {'error': True})


def about(request):
    return render(request, 'nat/about.html')


def login(request):
    return render(request, 'nat/login.html')


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


'''def show_feed(request, feed_id):
    feed = get_object_or_404(RssFeed, id=feed_id)
    articles = feed.article_set.all()
    context = {
        'articles': articles,
        'feed': feed,
    }
    return render(request, 'nat/feed.html', context)'''
