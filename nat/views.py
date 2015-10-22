from django.shortcuts import render, get_object_or_404
from rssparser import *
from models import *
from nat.rssparser import *
import user_database as udb

region_specifier = 4;
context = None

def home(request):
    articles = Article.objects.all()
    newscategories = NewsCategory.objects.all()
    rssfeeds = RssFeed.objects.all()
    popular = most_popular()
    recent = most_recent()
    user = udb.get_loggedInUser()
    username = ''
    if user is not None:
        username = user.user_name

    global context
    context = {
        'region_specifier': region_specifier,
        'articles': articles,
        'newscategories': newscategories,
        'rssfeeds': rssfeeds,
        'popular' : popular,
        'recent' : recent,
        'loggedInUser': username
    }
    return render(request, 'nat/home.html', context)

def most_popular():
    keyword = find_most_popular_keyword()
    return Article.objects.filter(title__icontains=keyword)[:10]

def most_recent():
    return Article.objects.all().order_by('-id')[:10]

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
            tempList2 = Article.objects.filter(description__icontains=keyWord)
            articles += tempList
            articles += tempList2

        #filter multiple occurances of articles for different keywords
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

        return render(request, 'nat/search_results.html', {'articles': articles, 'query': qString})
    else:
        return render(request, 'nat/search_results.html', {'error': True})

def about(request):
    return render(request, 'nat/about.html')

def login(request):
    return render(request, 'nat/login.html')

def logInUser(request):
    udb.log_in(request.GET['username'], request.GET['password'])
    contextCopy = context.copy()
    contextCopy.update({'loggedInUser': udb.get_loggedInUser().user_name})
    return render(request, 'nat/home.html', contextCopy)

def register_user(request):
    return render(request, 'nat/register_user.html')

def register(request):
    udb.register_user(request.GET['username'], request.GET['password'])
    return logInUser(request)

def favouriteArticles(request):
    articles = udb.getFavouriteArticle()
    return render(request, 'nat/favourite_articles.html', {'favouriteArticles': articles})

def addFavouriteArticles(request, article_id):
    udb.addFavouriteArticle(Article.objects.get(id=article_id))
    return render(request, 'nat/home.html', context)

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'nat/article.html', {'article': article})


def show_category(request, category_specifier):
    articles = Article.objects.filter(country=category_specifier)
    context = {
        'articles': articles
    }
    return render(request, 'nat/category.html', context)


