import tweepy

consumer_key='IJ140FnKRZH0kguFC4NaGpKdj'
consumer_secret='jQnh4jAM6Qunmj7aTXdDkR4uV2Li3e8TYsvfFyTIGqUGngQMpt'
access_token ='1133317456129187840-Ns0FbwLB2p3lELdmXTAffCKlPoVexn'
access_token_secret ='twwrHMjXmv9onJ7wbzR4cZoDNvjn1WIXkGeaGilypX1tp'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
api.update_status(status="First Self-Made Chatbot Tweet")