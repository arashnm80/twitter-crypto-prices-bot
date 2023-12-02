import os

# twitter tokens
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET =os.environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# coinmarketcap token
COINMARKETCAP_TOKEN = os.environ.get("COINMARKETCAP_TOKEN")

# settings
currencies = ["BTC", "ETH", "BNB", "XRP", "SOL", "ADA", "TRX", "TON", "DOGE"]
fiat = "USD"
