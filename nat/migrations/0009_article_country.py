# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nat', '0008_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='country',
            field=models.IntegerField(default=0),
        ),
    ]
