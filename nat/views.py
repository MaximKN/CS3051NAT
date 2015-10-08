from django.shortcuts import render, get_object_or_404
from rssparser import *



def home(request):
    parse_rss()
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'nat/home.html', context)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        #what the person types in for searching
        q = request.GET['q']
        q = q.lower()

        #new
        qString = q
        q = q.split()
        articles = []
        #finds all articles with a keyword contained in q
        for keyWord in q:
            tempList = Article.objects.filter(title__icontains=keyWord)
            articles += tempList

        #filter multiple occurances of articles for different keywords
        for article in articles:
            while articles.count(article) > 1:
                articles.remove(article)


        #find best articles to match higher search order = better
        for article in articles:
            article.search_order = 0
            for keyWord in q:
                if keyWord in article.title.lower():
                    print(article.search_order)
                    article.search_order += 1

        for i in range(len(articles)-1,0,-1):
            for j in range(i):
                if articles[j].search_order < articles[j+1].search_order:
                    temp = articles[j]
                    articles[j] = articles[j+1]
                    articles[j+1] = temp

        return render(request, 'nat/search_results.html',
            {'articles': articles, 'query': qString})
    else:
        return render(request, 'nat/search_results.html', {'error': True})


def about(request):
    return render(request, 'nat/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'nat/article.html', {'article': article})
