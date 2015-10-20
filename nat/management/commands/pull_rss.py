from django.core.management.base import BaseCommand
from nat.rssparser import parse_rss
import time


class Command(BaseCommand):
    def handle(self, **options):
        while True:
            parse_rss()
            time.sleep(60)
