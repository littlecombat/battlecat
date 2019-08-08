#
#   welcome, battle cat
#
#       it's been a while since we've seen each other . .
#
#

import tweepy
import random
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


# starting messages
msg_start1 = ['yawn... you wake up in the tall grass of the meadow. ']
msg_start2 = ['the wind brushes your cheeks. ', 'the clouds drift slowly above. ', 'your cat nose itches. ']
msg_start3 = ['do you want to EAT or NAP?']

# combine all 3 to make one single message
msg = 'DO YA WANNA EAT OR NAP ?????'

# keywords
kwd = ['eat', 'nap']

# start the first tweet
tweet = api.update_status(status=msg)

# scan for a reply
while True:
    time.sleep(20)
    mentions = api.mentions_timeline(count=1,since_id=tweet.id)
    for mention in mentions:
        if kwd[0] in mention.text.lower():
            status = 'NOM NOM NOM !!!!!!'
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        elif kwd[1] in mention.text.lower():
            status = 'ok im gonna sleep'
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        else:
            break
