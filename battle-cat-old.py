#
#   welcome, battle cat
#
#       it's been a while since we've seen each other . .
#
#

import tweepy
import random
import time


# important twitter stuff

CONSUMER_KEY = 'KZu5Qodll5MXzEOSKdKKjtU6b'
CONSUMER_SECRET = '1gpshmYgJw2LrytN1CIoSoN5ydKPfZiZtg5dGphlr17jM8SM58'
ACCESS_KEY = '3192628267-cSvbOIEcG7TAHY3pY8GdUKXi3iGzUpfj3y2vLPg'
ACCESS_SECRET = 'btXo8Q3PeZtOq61ErXWlcNik1Rw31iEtKwCyuXoiRuvja'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)



# msg1 : describe the space / what's going on
# msg2 : something else about the place / meow
# msg3 (optional, random) : cat stuff
# msg4 : display hp
#
# status = msg1 + msg2 + msg3 + msg4
#
# goto_schoolyard():
#   if schoolyard.visitCount < 1:
#       msg1 = something
#       msg2 = another thing
#   else:
#       msg1 = something else
#       msg2 = another thing else
#   msg3_gen()
#   msg4_gen()







# make classes for people and places

class Cat:
    def __init__(self):
        self.hp = 4
        self.atk = 2
        self.dfs = 1

class Controller:
    def __init__(self):
        self.msg = ''
        self.kwd = ['','']
    def newkw1(self,kwd):
        self.kwd[0] = kwd
    def newkw2(self,kwd):
        self.kwd[1] = kwd

class Room:
    def __init__(self):
        self.visitCount = 0
    def addCount(self):
        self.visitCount += 1

class Inventory:
    def __init__(self):
        self.talisman = 0



marcy = Cat()
inv = Inventory()
controller = Controller()

meadow = Room()
treehouse = Room()
city = Room()
hills = Room()








# wake up... battle cat...

def go_meadow():

    msg_wakeup = ['you wake up in the grassy meadow. ',
      'the long grass of the meadow brushes your face, and you wake up. ',
      'you yawn. the sun peeks thru the trees as you wake up. '] # 3
    msg_meadow = ['you check your phone ',
      'the gentle breeze catches your spirit and sends it soaring thru the clouds. ',
      'the quiet hum of the cicadas puts your mind at ease. ']
    msg_go_meadow = 'you see the CITY beyond the trees. your cozy TREEHOUSE stands behind you.'

    if meadow.visitCount == 0:
        msg1 = msg_wakeup[random.randint(0,2)]
    else:
        msg1 = ''
    msg2 = msg_meadow[random.randint(0,2)]
    msg3 = meow()
    msg4 = msg_go_meadow
    controller.newkw1('city')
    controller.newkw2('treehouse')
    meadow.addCount()

    msg = str(msg1) + str(msg2) + str(msg3) + '\r\r' + str(msg4)
    return msg

def go_treehouse():
    msg_treehouse = ['ah yes. home sweet tree. ',
        'yawn. the bed looks so cosy. you are filled with warmth from the tree. ']
    msg_talisman = 'you have %d talismans. ' % inv.talisman
    msg_go_treehouse = 'go to the MEADOW or HILLS? '

    if treehouse.visitCount == 0:
        msg1 = msg_treehouse[0]
    else:
        msg1 = msg_treehouse[1]
    msg2 = msg_talisman
    msg3 = meow()
    msg4 = msg_go_treehouse
    controller.newkw1('meadow')
    controller.newkw2('hills')
    treehouse.addCount()

    msg = str(msg1) + str(msg2) + str(msg3) + '\r\r' + str(msg4)
    return msg

def go_hills():
    msg_hills = ['the wind rips thru the hills. the trees whisper loudly. ',
        'we used to come to these to smoke in high school, remember? i miss you. ']
    msg_hills2 = ['whew.. ','you yawn audibly.. ']
    msg_hills3 = ['do you miss me? ', 'you probably hardly remember.. ']
    msg_hills4 = 'go to the MEADOW or TREEHOUSE? '

    if hills.visitCount == 1:
        msg1 = msg_hills[1]
    else:
        msg1 = msg_hills[0]
    msg2 = msg_hills2[random.randint(0,1)]
    msg3 = msg_hills3[random.randint(0,1)]
    msg4 = msg_hills4
    controller.newkw1('meadow')
    controller.newkw2('treehouse')
    hills.addCount()

    msg = str(msg1) + str(msg2) + str(msg3) + '\r\r' + str(msg4)
    return msg

def go_city():
    msg_city = ['you stumble into downtown. ',
        'you meander into the town. ']
    msg_city2 = ['some band is playing at the store. ',
        'you hear her band playing in the shop. ']
    msg_city3 = ['youve been afraid to see a show since i left. ',
        'i bet you dont have the courage to see them like this. ']
    msg_city4 = 'go back to the MEADOW or HILLS? '

    msg1 = msg_city[random.randint(0,1)]
    msg2 = msg_city2[random.randint(0,1)]
    msg3 = msg_city3[random.randint(0,1)]
    msg4 = msg_city4

    controller.newkw1('meadow')
    controller.newkw2('hills')
    city.addCount()

    msg = str(msg1) + str(msg2) + str(msg3) + '\r\r' + str(msg4)
    return msg

def go_sleep():
    msg = 'you doze off in the grass.. we will see each other again soon, battle cat..'
    tweet = api.update_status(status=msg, in_reply_to_status_id=mention.id_str)
    exit()
    return






def process(word):
    if word == 'treehouse':
        msg = go_treehouse()
    elif word == 'hills':
        msg = go_hills()
    elif word == 'city':
        msg = go_city()
    elif word == 'meadow':
        msg = go_meadow()
    elif word == 'sleep':
        msg = go_sleep()
    return msg

def meow():
    butt = ''
    msg_meow = ['mmmeow.. ', 'mew. ', 'meow~   ']
    msg_stuff = ['*licks paw* ', 'you wag your tail. ', 'your cat eyes shimmer.. ']
    if random.randint(0,3) > 1:
        butt = msg_meow[random.randint(0,2)]
        if random.randint(0,2) > 1:
            butt = butt + msg_stuff[random.randint(0,2)]
    else:
        butt = ''
    return butt











msg = go_meadow()

tweet = api.update_status(status=msg)

# while True:
#     time.sleep(10)
#     mentions = api.mentions_timeline(count=1,since_id=tweet.id)
#     for mention in mentions:
#         for word in controller.kwd:
#             if word in mention.text:
#                 msg = process(word)
#                 status = msg + '\r(via @' + mention.user.screen_name + ')'
#                 tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
#
#                 print msg
#                 print controller.kwd[0]
#                 print controller.kwd[1]
#
#                 break
#             else:
#                 break

while True:
    time.sleep(20)
    mentions = api.mentions_timeline(count=1,since_id=tweet.id)
    for mention in mentions:
        if controller.kwd[0] in mention.text.lower():
            word = controller.kwd[0]
            msg = process(word)
            status = msg + '\r(via @' + mention.user.screen_name + ')'
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)

            print msg
            print controller.kwd[0]
            print controller.kwd[1]

            break
        elif controller.kwd[1] in mention.text.lower():
            word = controller.kwd[1]
            msg = process(word)
            status = msg + '\r(via @' + mention.user.screen_name + ')'
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)

            print msg
            print controller.kwd[0]
            print controller.kwd[1]

            break
        else:
            break
