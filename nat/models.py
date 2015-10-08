from django.contrib.auth.models import User
from django.db import models

SHORT_LEN_TEXT = 1000


class NewsCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def set_attributes(self, title):
        self.title = title

    @property
    def __unicode__(self):
        return self.title


class RssFeed(models.Model):
    title = models.CharField(max_length=100, unique=True)
    feedUrl = models.CharField(max_length=300)

    def set_attributes(self, title, url):
        self.title = title
        self.feedUrl = url

    @property
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ("title",)


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.IntegerField()
    link = models.CharField(max_length=200)
    categories = models.ManyToManyField(NewsCategory)
    feed = models.ForeignKey(RssFeed, null=True)
    search_order = models.IntegerField(default=0)

    def set_attributes(self, title, description, source, link):
        self.title = title
        self.description = description
        self.source = source
        self.link = link

    def __unicode__(self):
        return self.title
'''
    def get_short_text(self):
        if len(self.description) > SHORT_LEN_TEXT:
            return escape(self.description[:SHORT_LEN_TEXT])
        else:
            return escape(self.description)
'''

'''
Used to store user data
'''
class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return "Username: " + self.user_name +  " Password: " + self.password
