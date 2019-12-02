import os
import re
from dotenv import load_dotenv
from mtranslate import translate
from textblob import TextBlob
from flask import Flask

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


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
