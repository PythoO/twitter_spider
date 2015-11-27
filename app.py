#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from models import *

class TwitterSpider:
    """
    The main class to make some data mining in twitter.
    """
    name = None
    api = None

    def __init__(self):
        """
        Initalize the TwitterRoi class.
        :param name:
        :return:
        """

        try:
            self.get_config()
        except StandardError:
            print "Cannot get config"

        try:
            self.get_connection()
        except StandardError:
            print "Cannot get connection"

    def set_name(self, name):
        self.name = name

    def set_api(self, api):
        self.api = api

    def get_config(self):


    def mining_account(self):
        """
        Function to get twitter account data.
        :return:
        """
        try:
            if self.name is not None:
                search_result = self.api.search_users(self.name, 1, 1)
                for user in search_result:
                    account = Account(name=user.name, user_id=user.id)
                    session.add(account)
                    session.commit()
            print "Account : %s added" % self.name
        except StandardError:
            print 'Mining account error'

    @staticmethod
    def get_all_accounts():
        for account in session.query(Account):
            print "%s | %d " % (account.name, account.user_id)

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

    twitter_roi = TwitterSpider()

    if len(sys.argv) > 1:
        name = sys.argv[1]
        twitter_roi.set_name(name)
        twitter_roi.mining_account()
        #sys.exit()

    twitter_roi.get_all_accounts()

    #twitter_roi.mining_tweets()
