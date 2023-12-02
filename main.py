from functions import *

if __name__ == "__main__":
    print(COINMARKETCAP_TOKEN)
    tweet_text = get_tweet_text()
    print(tweet_text)
    if len(tweet_text) > 280:
        print("tweet text more than 280 characters")
    else:
        post_tweet(tweet_text)