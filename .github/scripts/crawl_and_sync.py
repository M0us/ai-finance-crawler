import json, logging, feedparser
from datetime import datetime
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def crawl():
    all_items = []
    sources = [
        ('Yahoo Finance', 'https://finance.yahoo.com/news/rssindex', 'yahoo', 4),
        ('CoinDesk', 'https://www.coindesk.com/arc/outboundfeeds/rss/', 'coindesk', 4),
        ('arXiv', 'http://arxiv.org/rss/q-fin', 'arxiv', 4),
        ('Investing.com', 'https://www.investing.com/rss/news.rss', 'investing', 4),
    ]
    for name, url, sid, auth in sources:
        try:
            feed = feedparser.parse(url)
            for e in feed.entries[:5]:
                all_items.append({
                    'title': e.get('title', ''),
                    'link': e.get('link', ''),
                    'source_id': sid,
                    'source_name': name,
                    'authority': auth,
                    'published': datetime.now().isoformat(),
                })
            logger.info(f'{name}: {len(feed.entries[:5])}条')
        except Exception as e:
            logger.error(f'{name}错误: {e}')
    
    with open('crawled_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False)
    return all_items

if __name__ == '__main__':
    crawl()
