import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "TdP9WM1tZbUyWkbZJiwPTbcd6"
# api secret key
api_secret_key = "ifIbb8lBni9XJpsF59yHgjkDReLpGkSOivBKs7dgY4XdnSAYtF"
# access token
access_token = "854879004649803782-9HctdTt3BmKDOjJDQCGW74Lp5uuICtV"
# access token secret
access_token_secret = "yLqxGw4DNE7qHaFvxcEQ9sTsTqDU9vNcOkcR9GvmQt14x"


authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_user_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)