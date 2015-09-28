from nat.models import Article
import feedparser


def parse_rss():
    rss_urls = ['http://www.theguardian.com/uk/rss', 'http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://www.thetimes.co.uk/tto/news/uk/rss', 'http://www.dailymail.co.uk/home/index.rss',
                'http://www.telegraph.co.uk/news/uknews/rss', 'http://feeds.skynews.com/feeds/rss/uk.xml']
    rss_number = 0  # 0 - Guardian, 1 - BBC, 2 - Times, 3 - Daily Mail, 4 - Telegraph, 5 - Sky
    for rss_url in rss_urls:
        feeds = feedparser.parse(rss_url)
        articles = Article.objects.all()
        for entry in feeds.entries:
            if not Article.objects.filter(title=entry.title).exists() or len(articles) == 0:
                a = Article()
                a.set_attributes(entry.title, entry.description, rss_number, entry.link)
                a.save()
        rss_number += 1
