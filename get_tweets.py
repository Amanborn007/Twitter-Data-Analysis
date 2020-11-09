import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)


api_key = "5sYR7I0ypvIq8XYsm3xlgEyUQ"
# api secret key
api_secret_key = "DAAGrVOaWgXOaFPHc7RRAaUQ1FZaSk8vtCkUThodvIaUf02XM2"
# access token
access_token = "834773618785652737-bLvsrDHgagRZjDhGDQzZLiEDYY8Tn5B"
# access token secret
access_token_secret = "uRZhh7suTiNehiU3meU4GfQ6IN2RCSsuheIRPy8qv2ooI"

authentication = tweepy.OAuthHandler(api_key,api_secret_key)
authentication.set_access_token(access_token,access_token_secret)

api= tweepy.API(authentication , wait_on_rate_limit=True)


def get_related_tweets(text_query):
    tweets_list = []
    count = 50

    try:
        for tweets in api.search(q=text_query, count=count):
            print(tweets.text)
            tweets_list.append({'tweet_text': tweets.text})
        return  pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


