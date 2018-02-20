# Dependencies
import tweepy
from textblob import TextBlob

# remember install dependency: pip install <package>

# From twitter API setup
consumer_key = '7NlpZiODaZ8L0RfckoCZMWpdQ'
consumer_secret = 'vf5s6q6k3PmAJsytNSfT91ZrKGDb8k1vnaLrtyzIasDNo5v6KO'

acces_token = '837651924392546304-QLpnJj3fEjGRTEvy7iswSa41E2xVIin'
acces_token_secret = 'DVNg9OnjbzflrKL0bWP6gYSjDpMZnlxoNDZlE4zxhjwgT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

#Twitter API
api = tweepy.API(auth)

public_tweets = api.search('Mitsubishi')

# print number of comments
for tweet in public_tweets:
	 print('')
	 print('')
	 print(tweet.text)
	 analysis = TextBlob(tweet.text)
	 print('Sentiment:')
	 print(analysis.sentiment)
	 print('')
	 print('')