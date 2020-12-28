

import numpy as np
import pandas as pd

class TweetAnalyzer():
    def tweets_to_data_frame(self, tweets):

        df = pd.DataFrame(columns=['id', 'len', 'date', 'source', 'likes', 'retweets', 'location'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.full_text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets]) #.strftime('%H:%M:%S.%f')
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['location'] = np.array([tweet.user.location for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

        return df
