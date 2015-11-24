#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import ConfigParser
import sys
import sqlite3
from datetime import datetime


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
        # Create a Db connection
        self.conn = sqlite3.connect('twitter.db')
        self.curs = self.conn.cursor()
        # Create table.
        # self.conn.execute('''CREATE TABLE twitter_account (user int , name text, screen_name text)''')
        # self.conn.execute(
        #    '''CREATE TABLE twitter_account_data
        #    (user int , data text, followers int, favourite int, friend int, statuses int)''')
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

                self.curs.execute("SELECT user FROM twitter_account where user=:uid", self.user_id)
                data = self.curs.fetchone()
                if data is None:
                    self.curs.execute("INSERT INTO twitter_account VALUES(?, ?, ?)",
                                      (self.user_id, user_name, user_screen_name))

                self.curs.execute("INSERT INTO twitter_account_data VALUES(?,?,?,?,?,?)",
                                  (self.user_id, datetime.today(), user.followers_count, user.favourites_count,
                                   user.friends_count, user.statuses_count))
                self.conn.commit()
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
                print "-----------------------"
                print "\t Tweet created at : %s" % tweet.created_at
                print "\t Tweet favorite count (like) : %d" % tweet.favorite_count
                print "\t Tweet id : %d" % tweet.id
                print "\t Tweet lang %s" % tweet.lang
                print "\t Tweet retweet count : %d" % tweet.retweet_count
                print "\t Tweet text : %s" % tweet.text
        except StandardError:
            print "Mining tweets error"

    def get_data(self):
        data = self.curs.execute('SELECT * FROM twitter_account')
        print data.fetchall()

        data2 = self.curs.execute('SELECT * FROM twitter_account_data')
        print data2.fetchall()


if __name__ == "__main__":
    name = ''
    for arg in sys.argv:
        name = arg
    twitter_roi = TwitterSpider(name)
    twitter_roi.mining_account()
    twitter_roi.mining_tweets()

    twitter_roi.get_data()
