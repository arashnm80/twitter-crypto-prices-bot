from variables import *

import tweepy
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime

def post_tweet(tweet_text):

    client = tweepy.Client(
        bearer_token=TWITTER_BEARER_TOKEN,
        consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

    response = client.create_tweet(
        text = tweet_text
    )

    print(response.data)
    print(f"https://twitter.com/user/status/{response.data['id']}")

def get_tweet_text():
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': ",".join(currencies),
        'convert':fiat
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_TOKEN,
    }

    session = Session()
    session.headers.update(headers)

    try:
        tweet_text = ""

        response = session.get(url, params=parameters)
        json_data = json.loads(response.text)
        # print(json.dumps(json_data, indent=2)) # debug

        # timestamp
        timestamp = json_data["status"]["timestamp"]
        datetime_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        timestamp = datetime_object.strftime("%Y-%m-%d %H:%M:%S UTC")

        tweet_text += timestamp

        for currency in currencies:
            price = json_data["data"][currency][0]["quote"][fiat]["price"]
            price = "{:,.3f}".format(price)
            tweet_text += f"\n#{currency}: ${price}"
        
        return tweet_text
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("error in get_tweet_text")
        print(e)
    