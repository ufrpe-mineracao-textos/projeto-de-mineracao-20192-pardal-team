import pandas as pd
import preprocessor as p

tweets = pd.read_csv('../scraping/datasets/politics/tweets.csv')['tweet']
result = pd.Series([p.clean(tweet) for tweet in tweets])
result = result.drop_duplicates()

result.to_csv('preprocessed_datasets/politics/tweets.csv', header=['tweet'])
