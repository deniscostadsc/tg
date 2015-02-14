#!/usr/bin/env python
# coding: utf-8
import sqlite3

import tweepy
from secrets import (
    CONSUMER_KEY, CONSUMER_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

diseases = [
    'dengue',

    'gripe',
    'gripado',
    'gripada',

    'tuberculose',

    u'cólera',
    'colera',

    u'malária',
    'malaria'
]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def get_tweets(terms, cursor):
    for term in terms:
        tweets = api.search(q=term, rpp=100)
        for tweet in tweets:
            cursor.execute('INSERT OR IGNORE INTO tweets VALUES (?)', (tweet.text,))


if __name__ == '__main__':
    conn = sqlite3.connect('tg.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tweets (text text UNIQUE)')
    cursor.execute('PRAGMA encoding = "UTF-8"')
    get_tweets(diseases, cursor)
    cursor.close()
    conn.close()
