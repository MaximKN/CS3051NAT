#!/usr/bin/env python
import os
import sys
from nat.rssparser import parse_rss
from datetime import timedelta


if __name__ == "__main__":
    CELERYBEAT_SCHEDULE = {
        'add-every-60-seconds': {
            'task': parse_rss(),
            'schedule': timedelta(seconds=60),
            'args': (16, 16)
        },
    }
    CELERY_TIMEZONE = 'UTC'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CS3051NAT.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
