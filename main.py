# Read more about setting it up
# https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd

from datetime import timedelta, datetime
from dateutil import parser
from pprint import pprint
from time import sleep
import requests
import feedparser

BOT_TOKEN = '1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI'
CHANNEL_ID = '-1001114081400' # @bot_channel_name
FEED_URL = 'https://malayalam.oneindia.com/rss/malayalam-malappuram-fb.xml' # https://something.com/feeds/rss.xml


def send_message(message):
    requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message}')


def main():
    rss_feed = feedparser.parse(FEED_URL)

    for entry in rss_feed.entries:

        parsed_date = parser.parse(entry.published)
        parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None) # remove timezone offset
        now_date = datetime.utcnow()

        published_20_minutes_ago = now_date - parsed_date < timedelta(minutes=20)
        if published_20_minutes_ago:
            send_message(entry.links[0].href)
            print(entry.links[0].href)


if __name__ == "__main__":
    while(True):
        main()
        sleep(20 * 60)
