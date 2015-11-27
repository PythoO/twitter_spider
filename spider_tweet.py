#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from models import *
from twitter_api import *


class SpiderTweet():
    def __init__(self):
        print "Call me spider tweet"

    @staticmethod
    def get_accounts():
        return session.query(Account).order_by(Account.name)

    @staticmethod
    def mining_tweets(uid):
        """
        Function to get tweets data.
        :return:
        """
        try:
            print 'Job start ....'
            args = {'id': uid}
            tweet_list = twitter_api.user_timeline(**args)
            for tweet in tweet_list:
                db_tweet = Tweet(tid=tweet.id, uid=uid, favorite_count=tweet.favorite_count,
                                 retweet_count=tweet.retweet_count, text=tweet.text)
                session.add(db_tweet)
                session.commit()
            print 'Job done waiting....'
        except StandardError:
            print "Mining tweets error"

    @staticmethod
    def get_tweets():
        for tweet in session.query(Tweet).order_by(Tweet.tid):
            print "%d | %s | %d | %d : %s" % (tweet.tid, tweet.favorite_count, tweet.retweet_count, tweet.uid, tweet.text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
        spider = SpiderTweet
        spider.get_tweets()
    else:
        while True:
            thread_list = []
            spider = SpiderTweet
            accounts = spider.get_accounts()
            for account in accounts:
                print account.name
                spider.mining_tweets(account.uid)
            print 'sleeping....'
            t = 60 * 30
            time.sleep(t)
