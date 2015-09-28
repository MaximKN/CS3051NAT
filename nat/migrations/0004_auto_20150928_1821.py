# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nat', '0003_remove_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.CharField(default=datetime.datetime(2015, 9, 28, 18, 21, 38, 396134, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.CharField(default=datetime.datetime(2015, 9, 28, 18, 21, 47, 409182, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
