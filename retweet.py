# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.

import time
import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.
from keys import *
import os 
from os import environ


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(100), change 100 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!
for tweet in tweepy.Cursor(api.search, q='#100DaysOfCode').items(500):
    try:
        print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')

        
        time.sleep(10)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
