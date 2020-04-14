
from modules.TwitterClient import TwitterClient

import re
import numpy as np
import pandas as pd

# Enable these libraries if Greek Spacy is used
import spacy
import operator
from spacy.lang import el

class TweetAnalyzer():
    def tweets_to_data_frame(self, tweets):

        df = pd.DataFrame(columns=['text'])

        df['text'] = np.array([
            ''.join(re.sub(r"http\S+|@[^\s]+[\s]?|[^ Α-Ωα-ωΆ-Ώα-ωίϊΐόάέύϋΰήώ0-9]|[0-9]", "", tweet.full_text))
            for tweet in tweets])

        # BEGIN OF SENTIMENT ANALYZER
        # Sentiment analyzer for calculating positive or negative tweets. The calculation is performed using the
        # the Greek spacy libary of Giannis Daras available at Github: https://github.com/eellak/gsoc2018-spacy
        # Enable this only in a localhost environment as it consumes resources when loading el_core_news_md
        # corpus.

        nlp = spacy.load('el_core_news_md')
        indexes = {}
        lexicon = ('gr_lexicon.tsv')
        lexicon_read = pd.read_csv(lexicon, sep='\t')
        lexicon_read = lexicon_read.fillna('N/A')

        for index, row in lexicon_read.iterrows():
            lexicon_read.at[index, "Term"] = row["Term"].split(' ')[0]
            indexes[lexicon_read.at[index, "Term"]] = index

        subj_scores = {'OBJ': 0, 'SUBJ-': 0.5, 'SUBJ+': 1}
        emotion_scores = {'N/A': 0, '1.0': 0.2, '2.0': 0.4, '3.0': 0.6, '4.0': 0.8, '5.0': 1}
        polarity_scores = {'N/A': 0, 'BOTH': 0, 'NEG': -1, 'POS': 1}

        for row in df['text']:
            #doc=nlp(row)
            anger_score = 0
            disgust_score = 0
            fear_score = 0
            happiness_score = 0
            sadness_score = 0
            surprise_score = 0
            matched_tokens = 0

            for token in nlp(row):
                lemmatized_token = token.lemma_
                if (lemmatized_token in indexes):
                    indx = indexes[lemmatized_token]
                    pos_flag = False
                    for col in ["POS1", "POS2", "POS3", "POS4"]:
                        if (token.pos_ == lexicon_read.at[indx, col]):
                            pos_flag = True
                            break

                    if (pos_flag == True):
                        match_col_index = [int(s) for s in col if s.isdigit()][0]
                        anger_score += emotion_scores[str(lexicon_read.at[indx, 'Anger' + str(match_col_index)])]
                        disgust_score += emotion_scores[str(lexicon_read.at[indx, 'Disgust' + str(match_col_index)])]
                        fear_score += emotion_scores[str(lexicon_read.at[indx, 'Fear' + str(match_col_index)])]
                        happiness_score += emotion_scores[str(lexicon_read.at[indx, 'Happiness' + str(match_col_index)])]
                        sadness_score += emotion_scores[str(lexicon_read.at[indx, 'Sadness' + str(match_col_index)])]
                        surprise_score += emotion_scores[str(lexicon_read.at[indx, 'Surprise' + str(match_col_index)])]
                        matched_tokens += 1

                        for child in token.children:
                            ar=child, child.dep_


        #   Modification made by Alexandros Britzolakis store in every value
            try:
                emotions = {-3: anger_score,
                            -2: disgust_score,
                            -1: fear_score,
                             3: happiness_score,
                             1: sadness_score,
                             2: surprise_score}

                emotion = max(emotions.items(), key=operator.itemgetter(1))[0]

                #If no emotion is identified then assign 0 value which means Neutral
                if (emotions[emotion] == 0):
                     sentiment=0
                # If emotion is identified then assign the value
                # -3 = Anger | -2 = Disgust | -1 = Fear | 1 = Sadness | 2 = Surprise | 3 = Happiness
                else:
                     sentiment=emotion
                     # Uncomment this to print the sentiment score
                     # print(emotions[emotion] * 100 / matched_tokens, end =',')

            #If something goes wrong throw exception
            except:
                sentiment= 'No matched tokens'

            #Print sentiment
            print(sentiment, end =',')

            #Uncomment this to print the additional tweet text that the value was given with
            #print(row)

        return df


if __name__ == '__main__':
    # Enable the following lines of code and add any other code above in comments
    # when using spacy in a localhost environment.
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()

    #Note: On screen name place the name of the political leader
    #Greek politicians examples :  PrimeministerGR kmitsotakis atsipras FofiGennimata
    get_tweets = api.user_timeline(screen_name="place the name of leader here", count=200, tweet_mode='extended')

    generate_res = tweet_analyzer.tweets_to_data_frame(get_tweets)