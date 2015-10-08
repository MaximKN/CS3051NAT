from django.contrib import admin
from nat.models import Article, User, NewsCategory, RssFeed

admin.site.register(Article)
admin.site.register(User)
admin.site.register(NewsCategory)
admin.site.register(RssFeed)
