#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import ConfigParser
import sys
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

engine = sqla.create_engine('sqlite:///tutorial.db', echo=False)
connection = engine.connect()
Base = declarative_base()
Session = sessionmaker()


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)

    def __repr__(self):
        return "<Accounts(name= '%s', user_id='%d')>" % (self.name, self.user_id)

#Base.metadata.create_all(engine)
Session.configure(bind=engine)
session = Session()


class TwitterSpider:
    """
    The main class to make some data mining in twitter.
    """

    def __init__(self, name):
        """
        Initalize the TwitterRoi class.
        :param name:
        :return:
        """
        self.api = None
        self.engine = None
        self.name = name
        self.user_id = None
        self.session = None
        try:
            self.get_config()
        except StandardError:
            print "Cannot get config"

        try:
            self.get_connection()
        except StandardError:
            print "Cannot get connection"

    def get_config(self):
        self.api = None
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
            for account in session.query(Account):
                print "%s | %d " % (account.name, account.user_id)

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
    name = None
    if len(sys.argv) > 1:
        name = sys.argv[1]

    #while True:
    twitter_roi = TwitterSpider(name)
    twitter_roi.mining_account()
    #twitter_roi.mining_tweets()
