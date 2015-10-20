# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nat', '0007_auto_20151010_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 12, 47, 24, 748553, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
