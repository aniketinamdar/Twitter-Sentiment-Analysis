import tweepy

import tweepy

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAIC6lgEAAAAAs2BggKcYHZzIP3Cb394c8COn22E%3DEY0117cBIxmK1FyHfA3y5kX6xRV3c1pDDbweXVGP2Tq5Sxccpy")
api = tweepy.API(auth)

key = 'up0Dy5kd0SncKef7P336TbpMq'
secret = 'GdGqYIKNJAGpth5dRTWkCKKH3Xqgr2y5UKqZHL3IboJWiyClOS'
token = 'AAAAAAAAAAAAAAAAAAAAAIC6lgEAAAAAs2BggKcYHZzIP3Cb394c8COn22E%3DEY0117cBIxmK1FyHfA3y5kX6xRV3c1pDDbweXVGP2Tq5Sxccpy'

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)