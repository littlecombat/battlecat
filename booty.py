import tweepy
import time



# IMPORTANT TWITTER STUFF
CONSUMER_KEY = 'KDAOu7NwKFspEjTSwfnb42Gwb'
CONSUMER_SECRET = 'BHLLhL0mPxiNfDuJTrMd4LZHzV2uZiMuP0ocmsJXzokpKO7HHO'
ACCESS_KEY = '971792535575150592-KLWEoyWibQo77QO7KHusk4DVRHJaABw'
ACCESS_SECRET = 'eUN4VNGyKnta2YrbU6urdCaF46kmEIsh96HMRv0OYkWSe'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
# OK THAT'S IT



word = 'booty'

api.update_status(status=word)
print word
