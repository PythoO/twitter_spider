import tweepy
import ConfigParser
import sys

config = ConfigParser.ConfigParser()
config.read('config.ini')
section = 'Twitter'

consumer_key = config.get(section, 'consumer_key')
consumer_secret = config.get(section, 'consumer_secret')
access_token = config.get(section, 'access_token')
access_token_secret = config.get(section, 'access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for arg in sys.argv:
  name = arg

search_result = api.search_users(name, 1, 1)
for user in search_result:
  print "User: %s " % user.screen_name
  print "User ID : %s" % user.id
  print "Follower count : %d" % user.followers_count
  if hasattr(user, 'favorite_count'):
    print "Favorite count : %d" % user.favorite_count
  print "Friend count : %d" % user.friends_count
#print search_result
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#      print tweet.text

