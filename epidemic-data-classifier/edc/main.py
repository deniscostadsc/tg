#coding: utf-8

import os
import sys

# This line fix the path, and let GAE see the installed libs
SRC_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(SRC_DIR, 'lib'))

from flask import Flask, render_template
from google.appengine.ext import ndb
import tweepy

from models import Document
from secrets import (
    CONSUMER_KEY, CONSUMER_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


app = Flask(__name__)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter_api = tweepy.API(auth)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task/get-tweets')
def get_tweets():
    disease_terms = [
        'dengue',

        'gripe',
        'gripado',
        'gripada',
        'h1n1',

        'tuberculose',

        u'cólera',
        'colera',

        u'malária',
        'malaria'
    ]

    for term in disease_terms:
        tweets = twitter_api.search(q=term, rpp=100)

        documents = [
            Document(id=tweet.id_str, text=tweet.text) for tweet in tweets
        ]

        ndb.put_multi(documents)


if __name__ == '__main__':
    app.run()
