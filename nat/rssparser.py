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
    # rss_urls = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
    #             'http://www.thetimes.co.uk/tto/news/uk/rss',
    #             'http://www.dailymail.co.uk/home/index.rss',
    #             'http://feeds.skynews.com/feeds/rss/uk.xml',
    #             'http://www.tanea.gr/rss']

    rss_all_urls = [['http://feeds.bbci.co.uk/news/rss.xml?edition=int', 'http://feeds.skynews.com/feeds/rss/world.xml', 'http://rss.upi.com/news/tn_int.rss', 'http://feeds.foxnews.com/foxnews/latest?format=xml'],
                ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk', 'http://www.dailymail.co.uk/home/index.rss', 'http://feeds.skynews.com/feeds/rss/uk.xml', 'http://www.thetimes.co.uk/tto/news/uk/rss'],
                ['http://www.dailymail.co.uk/ushome/index.rss', 'http://www.usnews.com/rss/news', 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'],
                ['http://www.france24.com/fr/france/rss', 'http://www.lemonde.fr/m-actu/rss_full.xml','http://www.lexpress.fr/rss/alaune.xml'],
                ['http://wsrss.bbc.co.uk/russian/index.xml', 'http://www.pravda.ru/export-news.xml', 'https://russian.rt.com/rss/'],
                ['http://www.dailymail.co.uk/auhome/index.rss', 'http://www.abc.net.au/news/feed/46182/rss.xml', 'http://www.smh.com.au/rssheadlines/top.xml'],
                ['http://rss.in.gr/feed/news/greece/', 'http://ellinikanea.gr/feed/','http://www.tanea.gr/rss'],
                ['http://feeds.foxnews.com/foxnews/science?format=xml','http://www.thetimes.co.uk/tto/science/rss','http://www.dailymail.co.uk/sciencetech/index.rss'],
                ['http://feeds.foxnews.com/foxnews/sports?format=xml', 'http://www.dailymail.co.uk/sport/index.rss'],
                ['http://feeds.skynews.com/feeds/rss/politics.xml', 'http://feeds.foxnews.com/foxnews/politics?format=xml'],
                ['http://feeds.foxnews.com/foxnews/health?format=xml', 'http://www.dailymail.co.uk/health/index.rss'],
                ['http://feeds.foxnews.com/foxnews/entertainment?format=xml', 'http://feeds.skynews.com/feeds/rss/entertainment.xml', 'http://www.dailymail.co.uk/tvshowbiz/index.rss']]
    rss_number = 0
    category_specifier = 0
    for rss_country_urls in rss_all_urls:
        for rss_url in rss_country_urls:
            print(rss_url)
            # Later change this to parse urls retrieved from RssFeeds
            feeds = feedparser.parse(rss_url)
            articles = nat.models.Article.objects.all()
            for entry in feeds.entries:
                if not nat.models.Article.objects.filter(title=entry.title).exists() or len(articles) == 0:
                    a = nat.models.Article()
                    if 'pubDate' in entry:
                        a.set_attributes(entry.title, HTMLParser.HTMLParser().unescape(striphtml(entry.description)),
                                         rss_number, entry.link, entry.pubDate, category_specifier)
                    else:
                         a.set_attributes(entry.title, HTMLParser.HTMLParser().unescape(striphtml(entry.description)),
                                          rss_number, entry.link, category_specifier)
                    a.save()

            rss_number += 1
        category_specifier += 1
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
