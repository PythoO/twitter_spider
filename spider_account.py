#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from models import *
from twitter_api import *


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
                account = Account(name=user.name, uid=user.id)
                session.add(account)
                session.commit()
                return user.id
        except StandardError, e:
            print e.message

    @staticmethod
    def get_accounts():
        for account in session.query(Account).order_by(Account.name):
            print "%s \t| %s" % (account.name, account.user_id)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
        spider = SpiderAccount()
        spider.mining_account(name)
    else:
        SpiderAccount.get_accounts()
        sys.exit()
