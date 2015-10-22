# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nat', '0009_article_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourite_article',
            field=models.ManyToManyField(to='nat.Article'),
        ),
    ]
