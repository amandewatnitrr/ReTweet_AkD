import tweepy

consumer_key='Your Consumer Key'
consumer_secret='Your Secret Consumer Key'
access_token ='Your Access token Key'
access_token_secret ='Your Access token Secret Key'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
api.update_status(status="First Self-Made Chatbot Tweet")