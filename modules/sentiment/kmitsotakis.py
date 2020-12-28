
from modules.TwitterClient import TwitterClient

import re
import numpy as np
import pandas as pd

# Enable these libraries if Greek Spacy is used
import spacy
import operator
from spacy.lang import el

twitter_client = TwitterClient()
api = twitter_client.get_twitter_client_api()

#Note: On screen name place the name of the political leader
#Greek politicians examples :  PrimeministerGR kmitsotakis atsipras FofiGennimata
get_tweets = api.user_timeline(screen_name="kmitsotakis", count=200, tweet_mode='extended')

df = pd.DataFrame(columns=['text', 'sentiment'])
df['text'] = np.array([''.join(re.sub(r"http\S+|@[^\s]+[\s]?|[^ Α-Ωα-ωΆ-Ώα-ωίϊΐόάέύϋΰήώ0-9]|[0-9]", "", tweet.full_text)) for tweet in get_tweets])

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

sentiment_values = []
sentiment_score = []
for row in df['text']:
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
                    ar = child, child.dep_

    try:
        emotions = {-3: anger_score, -2: disgust_score, -1: fear_score, 3: happiness_score, 1: sadness_score, 2: surprise_score}
        emotion = max(emotions.items(), key=operator.itemgetter(1))[0]

        if (emotions[emotion] == 0):
            temp_sent = 0
            sentiment_values.append(temp_sent)
        else:
            temp_sent = emotion
            sentiment_values.append(temp_sent)
            temp_emscore = round(float(emotions[emotion] * 100 / matched_tokens), 1)
            sentiment_score.append(temp_emscore)

    except:
        print('No matched tokens')

sentiment=sentiment_values
sentiment_accuracy=sentiment_score
print("Results for @kmitotakis account")
print("Emotion Values:")
print(sentiment)
print("Emotion Score:")
print(sentiment_accuracy)
