#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import ConfigParser

twitter_api = None
config = ConfigParser.ConfigParser()
config.read('config.ini')
section = 'Twitter'
consumer_key = config.get(section, 'consumer_key')
consumer_secret = config.get(section, 'consumer_secret')
access_token = config.get(section, 'access_token')
access_token_secret = config.get(section, 'access_token_secret')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)
