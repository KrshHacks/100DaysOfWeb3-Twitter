from time import sleep
import tweepy
import os
from dotenv import load_dotenv
from tweepy.tweet import Tweet

load_dotenv()

print('info: starting 100DaysOfWeb3 Bot')

client = tweepy.Client(bearer_token=os.getenv('BEARER_TOKEN'), consumer_key=os.getenv('CONSUMER_KEY'), consumer_secret=os.getenv(
    'CONSUMER_SECRET'), access_token=os.getenv('ACCESS_TOKEN'), access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))

api = tweepy.API(tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv(
    'CONSUMER_SECRET')).set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET')))

users = []

for tweet in tweepy.Cursor(api.search, q='#web3community').items(10):
    try:
        if not tweet.user.screen_name in users:
            users.append(tweet.user.screen_name)

            status = api.get_status(tweet.id)
            
            retweeted = status.retweeted 

            if retweeted == False: 
                tweet.retweet()

            print(f'Running {tweet.user.screen_name}\'s retweet job')

            sleep(10)
        else:
            print(
                f'Ignoring {tweet.user.screen_name}, They\'ve already got a retweet')

    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break

sleep(10)

for tweet in tweepy.Cursor(api.search, q='#100DaysOfWeb3').items(50):
    try:
        if not tweet.user.screen_name in users:
            users.append(tweet.user.screen_name)

            status = api.get_status(tweet.id)
            
            retweeted = status.retweeted 

            if retweeted == False: 
                tweet.retweet()

            print(f'info: running {tweet.user.screen_name}\'s retweet job')

            sleep(10)
        else:
            print(
                f'info: ignoring {tweet.user.screen_name}, They\'ve already got a retweet')

    except tweepy.TweepError as error:
        print('\nError: Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break

sleep(10)

for tweet in tweepy.Cursor(api.search, q='#100DaysOfBlockchain').items(100):
    try:
        if not tweet.user.screen_name in users:
            users.append(tweet.user.screen_name)

            status = api.get_status(tweet.id)
            
            retweeted = status.retweeted 

            if retweeted == False: 
                tweet.retweet()

            print(f'Running {tweet.user.screen_name}\'s retweet job')

            sleep(10)
        else:
            print(
                f'Ignoring {tweet.user.screen_name}, They\'ve already got a retweet')

    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
