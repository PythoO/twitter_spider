#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import ConfigParser
import sys
import time


class TwitterSpider():
    """
    The main class to make some data mining in twitter.
    """

    def __init__(self, name):
        """
        Initalize the TwitterRoi class.
        :param name:
        :return:
        """
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
                print "User ID : %s" % user.id
                user_name = user.name
                user_screen_name = user.screen_name
                self.user_id = user.id
        except StandardError:
            print 'Mining account error'

    def mining_tweets(self):
        """
        Function to get tweets data.
        :return:
        """
        try:
            args = {'id': self.user_id}
            tweet_list = self.api.user_timeline(**args)
            for tweet in tweet_list:
                print "#####"
                print tweet.id
        except StandardError:
            print "Mining tweets error"


if __name__ == "__main__":
    name = ''
    for arg in sys.argv:
        name = arg

    while True:
        twitter_roi = TwitterSpider(name)
        twitter_roi.mining_account()
        twitter_roi.mining_tweets()
        time.sleep(10)