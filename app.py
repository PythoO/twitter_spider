#!/usr/bin/python

import tweepy
import ConfigParser
import sys


class TwitterRoi():
    """
    The main class to make some data mining in twitter.
    """

    def __init__(self, name):
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        section = 'Twitter'

        consumer_key = config.get(section, 'consumer_key')
        consumer_secret = config.get(section, 'consumer_secret')
        access_token = config.get(section, 'access_token')
        access_token_secret = config.get(section, 'access_token_secret')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)
        self.name = name
        self.user_id = int

    def mining_account(self):
        """
        Function to get twitter account data.
        :return:
        """
        try:
            search_result = self.api.search_users(name, 1, 1)
            for user in search_result:
                print "User: %s " % user.screen_name
                print "User ID : %s" % user.id
                self.user_id = user.id
                print "Follower count : %d" % user.followers_count
                if hasattr(user, 'favourites_count'):
                    print "Favorite count : %d" % user.favourites_count
                print "Friend count : %d" % user.friends_count
                print "Statuses count : %d" % user.statuses_count
        except StandardError:
            print 'Mining account error'

    def mining_tweets(self):
        """
        Function to get tweets data.
        :return:
        """
        try:
            args = {'id': self.user_id }
            tweet_list = self.api.user_timeline(**args)
            for tweet in tweet_list:
                print "-----------------------"
                print "\t Tweet created at : %s" % tweet.created_at
                print "\t Tweet favorite count (like) : %d" % tweet.favorite_count
                print "\t Tweet id : %d" % tweet.id
                print "\t Tweet lang %s" % tweet.lang
                print "\t Tweet retweet count : %d" % tweet.retweet_count
                print "\t Tweet text : %s" % tweet.text
        except StandardError:
            print "Mining tweets error"


if __name__ == "__main__":
    for arg in sys.argv:
        name = arg
    twitter_roi = TwitterRoi(name)
    twitter_roi.mining_account()
    twitter_roi.mining_tweets()