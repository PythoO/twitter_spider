#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from models import *
from twitter_api import *
import datetime
import argparse
import time


class SpiderAccount:
    """
    Spider use to add new accounts.
    """

    def __init__(self):
        print "Call me spider add."

    @staticmethod
    def mining_account(name):
        """
        Function to get account information and then record it in the DB.
        :param name:
        :return account id:
        """
        try:
            search_result = twitter_api.search_users(name, 1, 1)
            for user in search_result:
                now = datetime.datetime.now()
                account = Account(name=user.name, uid=user.id, description=user.description, tags='', created_at=now,
                                  updated_at=now)
                session.add(account)
                session.commit()

                return user.id

        except StandardError, e:
            print e.message

    @staticmethod
    def update_account_data():
        for account in session.query(Account).order_by(Account.name):
            print account.uid
            user_data = twitter_api.get_user(account.uid)
            now = datetime.datetime.now()
            account_data = AccountData(uid=user_data.id, favourites_count=user_data.favourites_count,
                                       followers_count=user_data.followers_count,
                                       friends_count=user_data.friends_count, listed_count=user_data.listed_count,
                                       statuses_count=user_data.statuses_count, created_at=now,
                                       updated_at=now)
            session.add(account_data)
            session.commit()

    @staticmethod
    def get_accounts():
        for account in session.query(Account).order_by(Account.name):
            print "%s | %s (%s) : %s" % (account.name, account.uid, account.created_at, account.description)

    @staticmethod
    def get_accounts_data():
        for account in session.query(AccountData).order_by(AccountData.uid):
            print "Account id: %s " % account.uid
            print "Favourite : %d :" % account.favourites_count
            print "Followers : %d :" % account.followers_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '-create', nargs='?', help='create help')
    parser.add_argument('-u', '-update', nargs='?', help='update help')
    parser.add_argument('-v', '-view', nargs='?', help='view help')
    args = parser.parse_args()
    spider = SpiderAccount()
    if args.c is not None:
        name = args.c
        spider.mining_account(name)

    if args.u is not None:
        while True:
            spider.update_account_data()
            time.sleep(60 * 10)

    if args.v is not None:
        SpiderAccount.get_accounts()
        SpiderAccount.get_accounts_data()
        sys.exit()
