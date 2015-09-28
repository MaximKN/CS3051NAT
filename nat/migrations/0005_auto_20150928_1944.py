# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nat', '0004_auto_20150928_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='source',
            field=models.IntegerField(),
        ),
    ]
