from nat.models import Article, RssFeed, NewsCategory
import feedparser


def parse_rss():
    # Code for using the RssFeed object instead of list of urls
    feeds = RssFeed.objects.all()
    urls = []
    for feed in feeds:
        urls.append(feed.feedUrl)

    rss_urls = ['http://www.theguardian.com/uk/rss', 'http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://www.thetimes.co.uk/tto/news/uk/rss', 'http://www.dailymail.co.uk/home/index.rss',
                'http://www.telegraph.co.uk/news/uknews/rss', 'http://feeds.skynews.com/feeds/rss/uk.xml']
    rss_number = 0  # 0 - Guardian, 1 - BBC, 2 - Times, 3 - Daily Mail, 4 - Telegraph, 5 - Sky
    for rss_url in rss_urls:
        # Later change this to parse urls retrieved from RssFeeds
        feeds = feedparser.parse(rss_url)
        articles = Article.objects.all()
        for entry in feeds.entries:
            if not Article.objects.filter(title=entry.title).exists() or len(articles) == 0:
                a = Article()
                a.set_attributes(entry.title, entry.description, rss_number, entry.link)
                a.save()
                if 'categories' in entry and len(entry.categories) > 0:
                    categoriesindb = NewsCategory.objects.all()
                    for category in entry.categories:
                        for dbcategory in categoriesindb:
                            if dbcategory.title == category:
                                a.categories.add(dbcategory)
                    a.save()

        rss_number += 1
