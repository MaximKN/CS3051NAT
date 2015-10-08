from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'nat.views.home', name='home'),
    url(r'^about$', 'nat.views.about', name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'nat.views.show_article', name='article'),
    url(r'^newscategory/(?P<newscategory_title>)/$', 'nat.views.show_category', name='newscategory'),
    url(r'^feed/(?P<rssfeed_id>[0-9]+)/$', 'nat.views.show_feed', name='rssfeed')
]
