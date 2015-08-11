import feedparser
page = ['http://feeds.rsc.org/rss/dt', 'http://rss.sciencedirect.com/publication/science/00108545','http://onlinelibrary.wiley.com/rss/journal/10.1002/%28ISSN%291099-0682c', 
'http://feeds.rsc.org/rss/mt', 'http://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=775&channel-name=JBIC+Journal+of+Biological+Inorganic+Chemistry', 
'http://feeds.feedburner.com/acs/achre4', 'http://feeds.feedburner.com/acs/accacs', 'http://feeds.feedburner.com/acs/chreay', 'http://feeds.feedburner.com/acs/cmatex', 'http://feeds.feedburner.com/acs/enfuem', 
'http://feeds.feedburner.com/acs/orgnd7', 'http://feeds.feedburner.com/acs/inocaj']
feeds = []
for url in page:
    feeds.append(feedparser.parse(url))
for feed in feeds:
    for post in feed.entries:
        print post.title, ':', post.link, '\n'
