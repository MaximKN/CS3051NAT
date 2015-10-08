from django.contrib import admin
from nat.models import Article
from nat.models import NewsCategory
from nat.models import RssFeed

admin.site.register(Article)
admin.site.register(NewsCategory)
admin.site.register(RssFeed)
