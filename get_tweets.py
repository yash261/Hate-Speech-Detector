import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "GRLHh2YtbvTqSMczBlAegW0qp"
# api secret key
api_secret_key = "P23LGvSGvG0nE5umdvPJK06AOkNC8tK30NnaP73taZkhrNV5s2"
# access token
access_token = "854879004649803782-wjXdCephqVq4uVaLHUiK21Eg7TfqjaP"
# access token secret
access_token_secret = "Y9qBA7f2ZRhhidTMmQPm7aFGvLaJZlzJtCdhwKPrU8nr6"


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
