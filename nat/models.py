from django.contrib.auth.models import User
from django.db import models

SHORT_LEN_TEXT = 1000


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.IntegerField()
    link = models.CharField(max_length=200)
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
