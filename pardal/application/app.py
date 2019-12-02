import os
import re
import tweepy
import preprocessor
from dotenv import load_dotenv
from mtranslate import translate
from textblob import TextBlob
from flask import Flask, render_template, send_from_directory

load_dotenv()
app = Flask(__name__)


class TwitterClient():
    def __init__(self):
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

        try:
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print('Error: Authentication Failed')

    def translate_tweet(self, tweet):
        t_tweet = translate(tweet, 'en', 'auto')

        return t_tweet

    def clean_tweet(self, tweet):
        c_tweet = preprocessor.clean(tweet)
        c_tweet = re.sub(r'(\:)', '', c_tweet)
        c_tweet = re.sub(r'(\")', '', c_tweet)
        c_tweet = re.sub(r'(\')', '', c_tweet)
        c_tweet = c_tweet.strip()

        return c_tweet

    def get_sentiment(self, tweet):
        c_tweet = self.clean_tweet(tweet)
        t_tweet = self.translate_tweet(c_tweet)
        analysis = TextBlob(t_tweet)

        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, word, count):
        tweets = []

        try:
            fetched_tweets = self.api.search(q=word, count=count)

            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_sentiment(tweet.text)

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets
        except tweepy.TweepError as error:
            print('Error: {}'.format(error))


def get_amount(tweets):
    positive, neutral, negative = 0, 0, 0

    for tweet in tweets:
        if tweet['sentiment'] == 'positive':
            positive += 1
        elif tweet['sentiment'] == 'neutral':
            neutral += 1
        else:
            negative += 1

    positive = 100 * positive / len(tweets)
    neutral = 100 * neutral / len(tweets)
    negative = 100 * negative / len(tweets)

    return positive, neutral, negative


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)
