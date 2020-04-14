import pandas as pd
from modules.TweetAnalyzer import TweetAnalyzer
from modules.TwitterClient import TwitterClient

twitter_client = TwitterClient()
tweet_analyzer = TweetAnalyzer()

api = twitter_client.get_twitter_client_api()

# Get tweets from accounts of @kmitsotakis, @atsiptas and @FofiGennimata
tweets_leader_1 = api.user_timeline(screen_name="kmitsotakis", count=200, tweet_mode='extended')
tweets_leader_2 = api.user_timeline(screen_name="atsipras", count=200, tweet_mode='extended')
tweets_leader_3 = api.user_timeline(screen_name="fofigennimata", count=200, tweet_mode='extended')

# Get tweets from the presidential accounts
pr_acc = api.user_timeline(screen_name="PrimeministerGR", count=200, tweet_mode='extended')

# Get tweets from Political party accounts
pol_party_1 = api.user_timeline(screen_name="neademokratia", count=200, tweet_mode='extended')
pol_party_2 = api.user_timeline(screen_name="syriza_gr", count=200, tweet_mode='extended')
pol_party_3 = api.user_timeline(screen_name="kinimallagis", count=200, tweet_mode='extended')

# print(api.lists_subscriptions(['kmitsotakis']))

# Process the tweets for political leaders
tw_ld_1_df = tweet_analyzer.tweets_to_data_frame(tweets_leader_1)
tw_ld_2_df = tweet_analyzer.tweets_to_data_frame(tweets_leader_2)
tw_ld_3_df = tweet_analyzer.tweets_to_data_frame(tweets_leader_3)

# Process the tweets for presidential account
tw_pr_acc = tweet_analyzer.tweets_to_data_frame(pr_acc)

# Process the tweets for political parties
tw_pol_party_1 = tweet_analyzer.tweets_to_data_frame(pol_party_1)
tw_pol_party_2 = tweet_analyzer.tweets_to_data_frame(pol_party_2)
tw_pol_party_3 = tweet_analyzer.tweets_to_data_frame(pol_party_3)

# GET THE NUMBER OF TWITTER SUBSCRIBERS BASED ON AN ACCOUNT OF A POLITICAL LEADER
follower_count_leader_1 = api.get_user('kmitsotakis').followers_count
follower_count_leader_2 = api.get_user('atsipras').followers_count
follower_count_leader_3 = api.get_user('fofigennimata').followers_count

# GET THE NUMBER OF TWITTER SUBSCRIBERS BASED ON AN ACCOUNT OF A POLITICAL PARTY
follower_count_ND = api.get_user('neademokratia').followers_count
follower_count_SYRIZA = api.get_user('syriza_gr').followers_count
follower_count_PASOK = api.get_user('pasok').followers_count

# Get tweets based by negative hashtag trends
# Instead count it would be interesting to add since='2019-11-20', until='2020-01-20' search_terms = ('superbowl OR super bowl OR #superbowl')
neg_hashtag_ND_1 = api.search(q='ΝΔ_θελατε', count=200 , tweet_mode='extended',lang="el")
neg_hashtag_ND_2 = api.search(q='ΝΔ_ξεφτιλες', count=200 , tweet_mode='extended',lang="el")
neg_hashtag_ND_3 = api.search(q='ΝΔ_ρομπες', count=200 , tweet_mode='extended',lang="el")

neg_hashtag_SYRIZA_1 = api.search(q="ΣΥΡΙΖΑ_ξεφτιλες", count=200 , tweet_mode='extended',lang="el")
neg_hashtag_SYRIZA_2 = api.search(q="συριζωα", count=200 , tweet_mode='extended',lang="el")
neg_hashtag_SYRIZA_3 = api.search(q="Συριζα_απατεωνες ", count=200 , tweet_mode='extended',lang="el")

neg_hashtag_KINAL_1 = api.search(q="#ΚΙΝΑΛ_ξεφτιλες", count=200 , tweet_mode='extended',lang="el")

# Process the tweets for political parties
neg_hash_ND_1 = tweet_analyzer.tweets_to_data_frame(neg_hashtag_ND_1)
neg_hash_ND_2 = tweet_analyzer.tweets_to_data_frame(neg_hashtag_ND_2)
neg_hash_ND_3 = tweet_analyzer.tweets_to_data_frame(neg_hashtag_ND_3)

neg_hash_SYRIZA_1 = tweet_analyzer.tweets_to_data_frame(neg_hashtag_SYRIZA_1)
neg_hash_SYRIZA_2 = tweet_analyzer.tweets_to_data_frame(neg_hashtag_SYRIZA_2)
neg_hash_SYRIZA_3 = tweet_analyzer.tweets_to_data_frame(neg_hashtag_SYRIZA_3)

neg_hash_KINAL_1 = tweet_analyzer.tweets_to_data_frame(neg_hashtag_KINAL_1)
# Merge data (likes) and display them in a proper way for political leaders
neg_res_1 = pd.Series(data=neg_hash_ND_1['date'].values)
neg_res_2 = pd.Series(data=neg_hash_ND_2['date'].values)
neg_res_3 = pd.Series(data=neg_hash_ND_3['date'].values)

neg_res_4 = pd.Series(data=neg_hash_SYRIZA_1['date'].values)
neg_res_5 = pd.Series(data=neg_hash_SYRIZA_1['date'].values)
neg_res_6 = pd.Series(data=neg_hash_SYRIZA_1['date'].values)

neg_res_7 = pd.Series(data=neg_hash_KINAL_1['date'].values)


# Merge data (likes) and display them in a proper way for political leaders
leader_1_likes = pd.Series(data=tw_ld_1_df['likes'].values, index=tw_ld_1_df['date'])
leader_2_likes = pd.Series(data=tw_ld_2_df['likes'].values, index=tw_ld_2_df['date'])
leader_3_likes = pd.Series(data=tw_ld_3_df['likes'].values, index=tw_ld_3_df['date'])

# Merge data (likes) and display them in a proper way for presidential account
pr_acc_likes = pd.Series(data=tw_pr_acc['likes'].values, index=tw_pr_acc['date'])

# Merge data (likes) and display them in a proper way for political parties
tw_pol_party_1_likes = pd.Series(data=tw_pol_party_1['likes'].values, index=tw_pol_party_1['date'])
tw_pol_party_2_likes = pd.Series(data=tw_pol_party_2['likes'].values, index=tw_pol_party_2['date'])
tw_pol_party_3_likes = pd.Series(data=tw_pol_party_3['likes'].values, index=tw_pol_party_3['date'])

# Merge data (retweets) and display them in a proper way for political leaders
leader_1_retweets = pd.Series(data=tw_ld_1_df['retweets'].values, index=tw_ld_1_df['date'])
leader_2_retweets = pd.Series(data=tw_ld_2_df['retweets'].values, index=tw_ld_2_df['date'])
leader_3_retweets = pd.Series(data=tw_ld_3_df['retweets'].values, index=tw_ld_3_df['date'])

# Merge data (retweets) and display them in a proper way for presidential account
pr_acc_retweets = pd.Series(data=tw_pr_acc['retweets'].values, index=tw_pr_acc['date'])

#Total length of the posted tweet text
text_length_leader_1 = pd.Series(data=tw_ld_1_df['len'].values)
text_length_leader_2 = pd.Series(data=tw_ld_2_df['len'].values)
text_length_leader_3 = pd.Series(data=tw_ld_3_df['len'].values)

# Merge data (retweets) and display them in a proper way for political leaders
tw_pol_party_1_retweets = pd.Series(data=tw_pol_party_1['retweets'].values, index=tw_pol_party_1['date'])
tw_pol_party_2_retweets = pd.Series(data=tw_pol_party_2['retweets'].values, index=tw_pol_party_2['date'])
tw_pol_party_3_retweets = pd.Series(data=tw_pol_party_3['retweets'].values, index=tw_pol_party_3['date'])

total_subscribers = int(follower_count_leader_1 + follower_count_leader_2 + follower_count_leader_3)
percentage_leader_1 = int((follower_count_leader_1 * 100) / total_subscribers)
percentage_leader_2 = int((follower_count_leader_2 * 100) / total_subscribers)
percentage_leader_3 = int((follower_count_leader_3 * 100) / total_subscribers)

compare_subs = [{'values': [percentage_leader_1, percentage_leader_2, percentage_leader_3], 'type': 'pie'}]

text_1 = 'AthPPA (which stands for Athena political popularity analysis tool) is a webpage which communicates with Twitter in order to obtain tweets of the most prominent political leaders in Greek political scene. The aplication gathers any available data from the official Twitter accounts of these political leaders. With the term available data we refer to a sample their recent posted Tweets which reaches the amount of 200. The data can be sepearated into structured and ustructured ones. With the term structured data we refer to the data which Twitter provides us through their API which are the number of likes, retweets, character length per posted tweet as well as the number of subscribers per account. We have also mined the number of tweets that users post and include negative hashtags for the rescpective political parties that these political leaders represent. We have also mined the same stuctured data from the official Twitter account of these additional political paties. Note that these are updated dynamically every hour as the application communicates directly with Twitter. With the term unstructured data we refer to the overall sentiment of the obtained text of each tweet. To obain the sentiment of the text we used a Python Natural Language Processing module called spaCy which includes linguistic features for the Greek language as well as a variety of Natural Language Processing techniques. Furthermore, a sentiment lexicon is used which has been designed specifically for political sentiment analysis and it includes a set of labeled positive/negative words. Sentiment analysis is perfomed on the text of the posted tweets made by those political leaders with a 200 tweet sample and it is updated each month. For more information visit How AthPPA works section of this webpage.'
text_2 = 'The Hellenic Parliament (Greek: Ελληνικό Κοινοβούλιο), in Greek known as Voulí ton Ellínon (Greek: Βουλή των Ελλήνων, literally Parliament of the Hellenes) is the parliament of Greece, located in the Old Royal Palace, overlooking Syntagma Square in Athens. The Parliament is the supreme democratic institution that represents the citizens through an elected body of Members of Parliament (MPs). It is a unicameral legislature of 300 members, elected for a four-year term. During 1844–1863 and 1927–1935, the parliament was bicameral with an upper house, the Senate, and a lower house, the Chamber of Deputies, which retained the name Vouli. Several important Greek statesmen have served as Speakers of the Hellenic Parliament. For more information check the links provided. '
text_3 = "The 2019 Greek legislative election was held on 7 July 2019. All 300 seats in the Hellenic Parliament were contested. Preliminary results showed that the centre-right liberal conservative New Democracy party, led by Kyriakos Mitsotakis, won 158 seats, an outright majority that is more than double the party's previous representation. The party took nearly 40% of the popular vote. This was the first national election in Greece and third election overall since the voting age was lowered to 17, and the number of parliamentary constituencies was increased from 56 to 59. Athens B, the largest constituency with 44 seats before the 2018 reform, was broken up into smaller constituencies, the largest of which has 18 seats. On 26 May 2019, following his defeat in the 2019 European Parliament election in Greece and the concurrent local elections, Prime Minister Alexis Tsipras announced that a snap election would be held as soon as possible following the second round of the 2019 municipal elections"
text_4 = "Kyriakos Mitsotakis (Greek: Κυριάκος Μητσοτάκης; born 4 March 1968) is a Greek politician serving as Prime Minister of Greece since 8 July 2019. A member of New Democracy, he has been its president since 2016. Mitsotakis previously was Leader of the Opposition from 2016 to 2019 and Minister of Administrative Reform from 2013 to 2015. He was first elected to the Hellenic Parliament for the Athens B constituency in 2004. After New Democracy suffered two election defeats in 2015, he was elected the party's leader in January 2016. Three years later, on 7 July 2019, he led his party to a majority in the 2019 election, their first since 2007. He is the son of former Prime Minister Konstantinos Mitsotakis. He is also president of the ruling party namely as New Democracy a conservative liberalist party. He was also been leader of the opposition until the last elections which concluded on 9th of July 2019 where under his leadership the New Democracy party won the elections with strong majority. The following charts depicts data statistics located from his Twitter account from a sample of 200 recent tweets made by him."

text_5 = "The following graph depicts the sentiment analysis results from the 200 recent tweet sample taken from Kyriakos Mitsotakis (@kmitsotakis) account. The indications are based on emotion scores. These emotions scores are Hapiness (value: 3), Surprise (value: 2), Sadness (value: 1), Neutral (value: 0), Fear (value: -1), Disgust (value: -2) and Anger (value: -3). We can think of this as a fine-grained result from very positive to very negative. The graph below depicts a scale of values from -3 (Anger or very negative) to 3 (Hapiness or very positive) based from the table of sentiment values as provided on how AthPPA works section (table 1)."
text_6 = "The following graph depicts the sentiment analysis results from the 200 recent tweet sample taken from Kyriakos Mitsotakis (@PrimeministerGR) account. The indications are based on emotion scores. These emotions scores are Hapiness (value: 3), Surprise (value: 2), Sadness (value: 1), Neutral (value: 0), Fear (value: -1), Disgust (value: -2) and Anger (value: -3). We can think of this as a fine-grained result from very positive to very negative. The graph below depicts a scale of values from -3 (Anger or very negative) to 3 (Hapiness or very positive) based from the table of sentiment values as provided on how AthPPA works section (table 1)."
text_7 = "In the following graphs bellow we have choosen some recent tweets based on negative hashtags for New Democracy party. We choose only the negative ones as we had plenty of data to visualize. Users in social media and especially Twitter tend express mostly a negative opinion regarding to the political context especially in countries with polical or economical crisis. For this reason, we have choosen three famous hashtags which indicate negative expression booth for New Democracy party."

text_8 = "Alexis Tsipras (Greek: Αλέξης Τσίπρας, born 28 July 1974) is a Greek politician serving as leader of the opposition since 2019 as well as head of the SYRIZA radical left party since 2009. He has also served as Prime Minister of Greece from 2015 to 2019. He is the fourth Greek Prime Minister who has governed in the course of the 2010s government-debt crisis. Originally an outspoken critic of the austerity policies implemented during the crisis, his tenure in office has been marked by an intense austerity policy, mostly in the context of the third EU bailout to Greece (2015–2018). The following charts depicts data statistics from his Twitter account from a sample of 200 recent tweets made by him."
text_9 = "The following graph depicts the sentiment analysis results from the 200 recent tweet sample taken from Alexis Tsipras (@atsipras) account. The indications are based on emotion scores. These emotions scores are Hapiness (value: 3), Surprise (value: 2), Sadness (value: 1), Neutral (value: 0), Fear (value: -1), Disgust (value: -2) and Anger (value: -3). We can think of this as a fine-grained result from very positive to very negative. The graph below depicts a scale of values from -3 (Anger or very negative) to 3 (Hapiness or very positive) based from the table of sentiment values as provided on how AthPPA works section (table 1)."
text_10 = "In the following graphs bellow we have choosen some recent tweets based on negative hashtags for SYRIZA party. We choose only the negative ones as we had plenty of data to visualize. As we mentioned previously users in social media and especially Twitter tend express mostly a negative opinion regarding to the political political party. We have choosen three famous hashtags which indicate negative expression for SYRIZA party."

text_11 = "Fofi Gennimata (Greek: Φώφη Γεννηματά, born 17 November 1964) is a Greek politician who has been president of the Panhellenic Socialist Movement (PASOK) since 2015. Since 2017, she serves as the president of the Movement for Change, a coalition of center-left parties formed around PASOK. Gennimata has served in a number of different roles in various governments, serving in the Cabinet of George Papandreou as a Deputy Minister of Health and Welfare and an Alternate Minister of Education, Lifelong Learning and Religious Affairs. The following charts depicts data statistics located from her Twitter account from a sample of 200 recent tweets made by her."
text_12 = "The following graph depicts the sentiment analysis results from the 200 recent tweet sample taken from Fofi Gennimata (@FofiGennimata) account. The indications are based on emotion scores. These emotions scores are Hapiness (value: 3), Surprise (value: 2), Sadness (value: 1), Neutral (value: 0), Fear (value: -1), Disgust (value: -2) and Anger (value: -3). We can think of this as a fine-grained result from very positive to very negative. The graph below depicts a scale of values from -3 (Anger or very negative) to 3 (Hapiness or very positive) based from the table of sentiment values as provided on how AthPPA works section (table 1)."
text_13 = "In the following graph bellow we have choosen some recent tweets based on a negative hashtag for KINAL party. In the case of KINAL party we couldn't find enough negative hashtags due to the low popularity of the party. For this purpose we choose only one negative hashtag that has been latest trend for this party and users tend to use frequently."





aboutapp_text_1 = "Twitter is commonly known as a news platform through which its users are informed about the latest events or trends around the globe. Basically, it as a micro-blogging platform which covers the latest trends and events. Besides the fact that Twitter is the top micro-blogging platform on the web, it is also the most frequent social media platform which politicians and political parties tend to use. Thus, Twitter is suitable for analyzing data “tweets” of politicians, perform an analysis of them and extract a prediction for a positive or a negative sentiment over a political party or an entity. Furthermore, Twitter provides their API to companies and developers. At a high level, with the term API we refer to the way which computing systems communicate with each other which is in the form of request (asking for a service) and response (providing a service). This can be achieved by allowing a software application to call an endpoint which has an IP address. Endpoints can be a home pc (desktop or laptop) which has a network card with a unique IP address and a connection through the web. Although what makes Twitter one of the most popular micro-blogging platforms is the fact that its APIs can be accessed by programmers. This feature allows the development of applications that can be fully integrated with Twitter. Twitter’s data have a unique form which can be shared by additional social platforms due to the reason that it reflects information that users choose to share publicly. The API of Twitter gives an infinite access to all public “tweets” which are uploaded publicly by its users."
aboutapp_text_2 = "Athena political popularity analysis tool uses Tweepy module in order to establish communication with Twitter. To achieve communication with Twitter an additional API has been created using the API creator that Twiter has. Once a Twitter API is created then four (4) keys will be generated representing this unique API. Figure 1 represents a generic example of how Twitter’s API communicates with a Python script."
aboutapp_text_3 = "These four (4) Twitter keys are used by the application and specifically from Tweepy module of Python programming language. For the purposes of our research we have identified the Twitter accounts of the most prominent top three (3) political leaders in Greece. Those accounts that have been identified are @kmitsotakis, @atsipras and @fofigennimata. We have also included the Twitter acount of the Greek Prime Minister (@PrimeministerGR) which is currently Kyriakos Mitsotakis. For each one of these political leaders we are obtaining dynamically, a sample of their recent tweets. This sample reaches the number of 200 tweets per political account (in total 800 tweets sample), the reason for choosing this number is due to limitations of the tweepy module reagrding of how many tweets we can obtain as well as for the efficiency of the average speed of the webserver. From those tweets we've obtained the user likes, retweets as well as text length per tweet. We've also obtained the number of subscirbers that each political leader has as it shows a positive tendency. We've also obtained the likes and retweets per posted tweet from the oficial political party accounts for each of the above menioned political leaders namely as New Democracy (#neademokratia), Coalition of the Radical Left (@syriza_gr) and Movement for Change (@kinimaallagis) with a total sample of 600 tweets. From those tweets we have also obtained the likes and retweets for each posted tweet. We have also identified three negative hashtag trends for the two prominent political parties namely the New Democracy and the Coalition of the Radical Left as well as one negative hashtag for Movement for Change political party. Using these hashtags we gathered a sample of recent tweets posted by users and visualized how frequntly these particular hashtags are used by the users. It is notable to mention that these data are updated dynamically. Furthermore, sentiment analysis is achieved from a sample of tweets that we have collected using spacy module. "
aboutapp_text_4 = "For the sentiment analysis procedure we used the Greek corpus of spacy and we inspired from the emotion analyzer of the NLPbudy project booth made by Giannis Daras for the text classification. The text is labeled based on the greek-sentiment-lexicon lexicon. For this purpose we created a script in order to gather a sample of 200 recent posted tweets from the accounts of the top three Greek polticians. The text is being processed in order to remove hashtags and urls in order to keep the clear text using regular expressions. Afterwards, the script analyzes each word in the current tweet and tries to seek for words in the lexicon and uses the el_core_news_md in order for the processing proceedure. Both modules are available below as well as a table with the labeled values and their addional description."


about_text_1 = "Alexandros Britzolakis was born in 1991, he currently resides in Heraklion, Crete, Greece. He was a Graduate Assistant Researcher at the Computational BioMedicine Laboratory - CBML of FORTH-ICS and at Artificial Intelligence and Systems Engineering Laboratory at the Hellenic Mediterranean University as part of his master academic thesis with subject Design and development of a web-based data visualization software for political tendency identification of Twitter's users using Python Dash framework. He received his B.Sc. from the department of Informatics Engineering, Hellenic Mediterranean University - H.M.U. (or fomerly known as Technological Educational Institute of Crete) as well as his masters degree in Network Engineering and Multimedia from the same department."
about_text_2 = "Dr. Nikolaos Papadakis received his B.Sc. degree from the computer department of the University of Cyprus with degree grade 8.34 (ranking first of his  graduation year). Furthermore, received his masters degree (M.Sc.) from the department of Computer Science at University of Crete on the fields of Information Systems, Software Engineering and in networks as well as his Ph.D. from the same department on the filed of Knowledge Representation and reasoning systems. He was former lecturer at Technical University of Crete from 2004-2008. He has been recruited as an academic staff at the Hellenic Meditteranean University (or formely known as Technological Educational Insitute of Crete) from 2007 until present. Since then he has been appointed as a Research Fellow from 2007 - 2009, applied professor from 2009 - 2013, Emeritus professor from 2013-2017 and associate professor from 2017 until present at the Hellenic Mediterranean University. "
about_text_3 = "Dr. Haridimos Kondylakis is currently a Collaborating Researcher at Computational BioMedicine Laboratory (CBML), Institute of Computer Science, Foundation of Research & Technology-Hellas (FORTH). He holds a Ph.D and an M.Sc. in Computer Science from University of Crete. He is also a visiting lecturer at the Computer Science Department, University of Crete and at the Department of Electric and Computer Engineeringat Hellenic Mediterranean University and at Hellenic Open University, teaching lessons related to data management and semantics. His interests include semantic-based, big data management topics and their application in healthcare. More specifically he has focused on e-Consent through semantic rules, semantically-enabled medical recommendations for patient empowerment, ontology summarization and evolution, efficient infrastructures for collecting, partitioning, indexing, integrating and managing eHealth information and data series data, personal health environments, modular ontologies for healthcare and mappings to the various data sources. He has more than 130 publications in international conferences, books and journals including ACM SIGMOD, VLDB, JWS, KER, EDBT, ISWC, ESWC etc."
about_text_4 = "Dr. Stelios Sfakianakis received his B.Sc. and MSc diplomas from the Department of Informatics and Telecommunications of the University of Athens and his Ph.D. from the School of Electrical and Computer Engineering of the Technical University of Crete. Since 2000 he has been with the Computational BioMedicine Laboratory of FORTH, working on integrating systems in the field of biomedicine, semantic interoperability, and building tools and services for intelligent data analysis. He has participated as work packages leader in numerous European research projects, focusing on the development of innovative ICT solutions to support large-scale transcription research on cancer, the discovery of biological cancer markers, transcription medicine, and the design and implementation of computational infrastructures for the integration of data and services. His research interests include biomedical computing, web-based cloud-based software architectures, and data mining and analysis with modern computing tools. He has published more than 60 articles in international journals and conference proceedings related to his areas of expertise."




#Add the values taken from spacy script for kmitsotakis account
sentiment_leader_1=[0,3,3,0,0,0,0,0,3,3,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,3,0,1,0,0,0,0,3,0,0,0,0,0,3,0,3,-3,2,0,-3,0,0,2,0,3,-3,3,0,0,0,2,0,3,0,-3,0,0,-2,0,2,0,-3,0,0,0,3,0,0,0,0,0,0,3,0,0,3,0,-3,-2,3,0,0,0,0,0,-3,0,0,0,0,1,0,0,0,0,3,0,0,3,0,0,0,3,0,2,3,0,0,3,0,0,0,0,3,0,-3,0,0,3,0,0,0,0,3,1,3,-2,0,0,0,3,3,3,3,-3,3,3,-3,0,3,0,3,-1,0,0,2,3,0,0,3,0,3,3,3,0,0,0,3,0,0,0,0,3,0,0,0,0,3,0,2,0,3,3,0,0,0,3,0,3,3,0,0,0,3,0,3,0,0,-3,0,0,3,-2]
sent_leader_1_score=[0,60,25,0,0,0,0,0,80,50,0,0,0,0,0,0,27,0,0,0,0,0,0,0,0,0,0,28,0,100,0,0,0,0,32,0,0,0,0,0,35,0,80,10,70,0,40,0,0,20,0,60,40,20,0,0,0,60,0,80,0,27,0,0,33,0,30,0,40,0,0,0,40,0,0,0,0,0,0,100,0,0,20,0,16,13,11,0,0,0,0,0,40,0,0,0,0,80,0,0,0,0,40,0,0,27,0,0,0,30,0,52,40,0,0,47,0,0,0,0,80,0,80,0,0,20,0,0,0,0,80,80,50,60,0,0,0,70,20,80,40,16,27,67,27,0,40,0,50,80,0,0,53,60,0,0,53,0,30,40,40,0,0,0,50,0,0,0,0,20,0,0,0,0,20,0,60,0,40,40,0,0,0,50,0,40,20,0,0,0,90,0,100,0,0,25,0,0,100,80]
#Initiate the lists that potitive, negative and neutral numbers will be stored
pos_count_leader1, neg_count_leader1, neu_count_leader1 = 0, 0, 0

# Iterate the list sentiment_leader_1 and calculate the positive negative and neutral numbers
for num in sentiment_leader_1:
    if num > 0:
        pos_count_leader1 += 1
    elif num < 0:
        neg_count_leader1 += 1
    else:
        neu_count_leader1 += 1

#Calculate the total number of tweets gathered
total_tweets_leader1 = int(pos_count_leader1 + neu_count_leader1 + neg_count_leader1)
#Calculate the percentage of positive tweets
percentage_pos_ld1 = int((pos_count_leader1 * 100) / total_tweets_leader1)
#Calculate the percentage of neutral tweets
percentage_neu_ld1 = int((neu_count_leader1 * 100) / total_tweets_leader1)
#Calculate the percentage of negative tweets
percentage_neg_ld1 = int((neg_count_leader1 * 100) / total_tweets_leader1)



#Add the values taken from spacy script for kmitsotakis account
sentiment_PrAcc=[3,3,3,3,0,0,0,3,2,2,-3,3,3,0,0,0,2,3,0,0,3,0,3,3,0,-3,0,3,3,2,3,0,0,3,0,3,0,-1,-3,0,0,0,3,3,0,3,0,0,3,3,3,3,0,3,2,3,-3,3,0,0,0,3,3,0,0,0,-3,0,-3,3,-3,0,3,0,-3,-3,3,0,-3,0,-3,2,0,3,2,3,0,3,-2,3,3,3,3,2,3,-3,-3,3,0,-3,0,-3,2,2,-3,-3,-2,3,0,0,0,0,-3,3,3,-1,0,0,0,0,0,0,-3,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,3,0,0,-3,0,3,0,3,0,0,3,0,0,3,0,0,1,0,-3,0,0,0,0,0,0,0,0,3,3,0,0,0,3,0,0,1,0,0,2,2,0,0,1,-1,3,0,0,0,3,0,0,0,0,3,3,0,0,-2,0,-2]

#Initiate the lists that potitive, negative and neutral numbers will be stored
pos_count_PrAcc, neg_count_PrAcc, neu_count_PrAcc = 0, 0, 0

# Iterate the list sentiment_leader_1 and calculate the positive negative and neutral numbers
for num in sentiment_PrAcc:
    if num > 0:
        pos_count_PrAcc += 1
    elif num < 0:
        neg_count_PrAcc += 1
    else:
        neu_count_PrAcc += 1

#Calculate the total number of tweets gathered
total_tweets_PrAcc = int(pos_count_PrAcc + neu_count_PrAcc + neg_count_PrAcc)
#Calculate the percentage of positive tweets
percentage_pos_PrAcc = int((pos_count_PrAcc * 100) / total_tweets_PrAcc)
#Calculate the percentage of neutral tweets
percentage_neu_PrAcc = int((neu_count_PrAcc * 100) / total_tweets_PrAcc)
#Calculate the percentage of negative tweets
percentage_neg_PrAcc = int((neg_count_PrAcc * 100) / total_tweets_PrAcc)




#Add the values taken from spacy script for atsipras account
sentiment_leader_2=[0,-2,3,-3,-3,0,0,0,0,0,0,3,-3,0,0,0,-2,-2,2,0,-3,-3,-3,0,0,3,-3,2,0,0,2,0,0,0,0,0,-3,0,0,0,0,0,-3,-2,-3,-3,-3,-2,0,0,0,-3,2,3,0,-3,-3,-3,3,0,-3,-3,3,2,3,2,0,3,3,0,-3,3,3,3,0,0,3,0,0,0,0,-3,3,2,2,3,0,3,-3,-3,0,0,-3,-3,2,-2,0,0,3,3,3,0,-2,-3,3,-3,3,3,0,0,0,0,0,-3,3,0,0,0,0,0,0,-1,3,0,0,-1,-3,0,0,2,3,3,0,-3,0,0,0,0,0,-1,3,0,3,0,0,0,3,-2,0,3,-2,2,0,3,0,0,-2,-3,0,0,2,0,0,0,0,3,0,2,3,3,0,0,0,-2,0,0,2,0,3,-3,0,0,0,0,3,0,0,0,0,0,0,-3,0,0,0,0,0,0,0,0]

#Initiate the lists that potitive, negative and neutral numbers will be stored
pos_count_leader2, neg_count_leader2, neu_count_leader2 = 0, 0, 0

# Iterate the list sentiment_leader_1 and calculate the positive negative and neutral numbers
for num in sentiment_leader_2:
    if num > 0:
        pos_count_leader2 += 1
    elif num < 0:
        neg_count_leader2 += 1
    else:
        neu_count_leader2 += 1

#Calculate the total number of tweets gathered
total_tweets_leader2 = int(pos_count_leader2 + neu_count_leader2 + neg_count_leader2)
#Calculate the percentage of positive tweets
percentage_pos_ld2 = int((pos_count_leader2 * 100) / total_tweets_leader2)
#Calculate the percentage of neutral tweets
percentage_neu_ld2 = int((neu_count_leader2 * 100) / total_tweets_leader2)
#Calculate the percentage of negative tweets
percentage_neg_ld2 = int((neg_count_leader2 * 100) / total_tweets_leader2)




#Add the values taken from spacy script for fofigennimata account
sentiment_leader_3=[0,-3,0,0,0,3,0,0,0,0,0,0,3,-2,0,0,0,-2,0,0,-3,0,0,3,-1,0,-3,-3,0,-3,0,0,0,0,0,0,0,0,0,-3,0,0,0,0,-3,0,3,0,-3,0,0,0,0,0,3,-3,3,-2,0,0,0,0,0,0,0,2,0,0,0,-1,-3,0,0,-3,-3,2,0,0,0,-3,0,0,0,3,0,3,0,3,3,0,0,3,3,0,0,3,3,-3,0,0,-3,0,2,-3,0,2,-3,3,0,0,-3,0,0,0,0,3,0,3,3,-2,-3,0,0,0,2,-3,-3,3,3,3,0,0,0,0,-3,0,0,0,3,0,0,3,2,0,3,0,3,0,3,-3,3,3,0,0,0,0,0,0,0,0,0,0,0,3,1,-2,0,-2,0,1,3,0,0,1,3,3,-3,0,-3,-2,0,0,0,0,0,0,-1,0,0,3,0,0,0,0,0,0,0,0,-3,0]

#Initiate the lists that potitive, negative and neutral numbers will be stored
pos_count_leader3, neg_count_leader3, neu_count_leader3 = 0, 0, 0

# Iterate the list sentiment_leader_1 and calculate the positive negative and neutral numbers
for num in sentiment_leader_3:
    if num > 0:
        pos_count_leader3 += 1
    elif num < 0:
        neg_count_leader3 += 1
    else:
        neu_count_leader3 += 1

#Calculate the total number of tweets gathered
total_tweets_leader3 = int(pos_count_leader3 + neu_count_leader3 + neg_count_leader3)
#Calculate the percentage of positive tweets
percentage_pos_ld3 = int((pos_count_leader3 * 100) / total_tweets_leader3)
#Calculate the percentage of neutral tweets
percentage_neu_ld3 = int((neu_count_leader3 * 100) / total_tweets_leader3)
#Calculate the percentage of negative tweets
percentage_neg_ld3 = int((neg_count_leader3 * 100) / total_tweets_leader3)
