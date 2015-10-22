from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', 'nat.views.home', name='home'),
    url(r'^addFavouriteArticles/(?P<article_id>[0-9]+)/$', 'nat.views.addFavouriteArticles', name='addFavouriteArticles'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'nat.views.show_article', name='article'),
    url(r'^category/([0-9]+)/$', 'nat.views.show_category', name='category'),
    # url(r'^feed/(?P<rssfeed_id>[0-9]+)/$', 'nat.views.show_feed', name='rssfeed')
    url(r'^login', 'nat.views.login', name='login'),
    url(r'^register_user', 'nat.views.register_user', name='register_user'),
    url(r'^search/$', views.search),
    url(r'^register/$', views.register),
    url(r'^logInUser/$', views.logInUser),
    url(r'^favourite_articles', 'nat.views.favouriteArticles', name='favourite_articles'),
]
