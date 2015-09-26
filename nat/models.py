from django.contrib.auth.models import User
from django.db import models

SHORT_LEN_TEXT = 1000

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_LEN_TEXT:
            return self.text[:SHORT_LEN_TEXT]
        else:
            return self.text