import nat.models
import feedparser
import re
import HTMLParser


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def parse_rss():
    print "Pulling data from rss feeds"
    # Code for using the RssFeed object instead of list of urls
    feeds = nat.models.RssFeed.objects.all()
    urls = []
    for feed in feeds:
        urls.append(feed.feedUrl)

    rss_urls = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://www.thetimes.co.uk/tto/news/uk/rss',
                'http://www.dailymail.co.uk/home/index.rss',
                'http://feeds.skynews.com/feeds/rss/uk.xml']
    rss_number = 0
    for rss_url in rss_urls:
        # Later change this to parse urls retrieved from RssFeeds
        feeds = feedparser.parse(rss_url)
        articles = nat.models.Article.objects.all()
        for entry in feeds.entries:
            if not nat.models.Article.objects.filter(title=entry.title).exists() or len(articles) == 0:
                a = nat.models.Article()
                a.set_attributes(entry.title, HTMLParser.HTMLParser().unescape(striphtml(entry.description)),
                                 rss_number, entry.link, entry.pubDate)
                a.save()
                if 'categories' in entry and len(entry.categories) > 0:
                    categoriesindb = nat.models.NewsCategory.objects.all()
                    for category in entry.categories:
                        for dbcategory in categoriesindb:
                            if dbcategory.title == category:
                                a.categories.add(dbcategory)
                    a.save()

        rss_number += 1
    print "Pulling complete!"


def find_most_popular_keyword():
    articles = nat.models.Article.objects.all()
    list_of_articles = ""
    for article in articles:
        list_of_articles += article.title + " "

    BAD_CHARS = ".!?,\'\""

    words = [word.strip(BAD_CHARS) for word in list_of_articles.strip().split() if len(word) > 6]

    word_freq = {}

    return max(set(words), key=words.count)

