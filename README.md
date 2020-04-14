# AthPPA
A Python tool for identifying political popularity through Twitter

Description:

AthPPA (which stands for Athena political popularity analysis tool) is a web application which communicates with Twitter in order to obtain tweets of the most prominent political leaders in Greek political scene. The aplication gathers any available data from the official Twitter accounts of these political leaders. With the term available data we refer to a sample their recent posted Tweets which reaches the amount of 200. The data can be sepearated into structured and ustructured ones. With the term structured data we refer to the data which Twitter provides us through their API which are the number of likes, retweets, character length per posted tweet as well as the number of subscribers per account. We have also mined the number of tweets that users post and include negative hashtags for the rescpective political parties that these political leaders represent. We have also mined the same stuctured data from the official Twitter account of these additional political paties. Note that these are updated dynamically every hour as the application communicates directly with Twitter. With the term unstructured data we refer to the overall sentiment of the obtained text of each tweet. To obain the sentiment of the text we used a Python Natural Language Processing module called spaCy which includes linguistic features for the Greek language as well as a variety of Natural Language Processing techniques. Furthermore, a sentiment lexicon is used which has been designed specifically for political sentiment analysis and it includes a set of labeled positive/negative words. Sentiment analysis is perfomed on the text of the posted tweets made by those political leaders with a 200 tweet sample and it is updated each month.

Prerequisites:
1. Python (3.8 version)
2. tweepy (pip install tweepy)
3. spacy-nightly (pip install spacy-nightly)
4. Download Spacy Greek libraries (spacy download el_core_news_md)

Live preview: https://athppa.cs.hmu.gr/ 
