import twitter
import urllib
import json

WORLD_WOE_ID = 1

US_WOE_ID = 2379574 # Chicago's WOE_ID # used for trends extraction


# Authentication into the twitter's API

CONSUMER_KEY = 'YUE5cGzChlvSmZMHlgEbw' 
CONSUMER_SECRET = 'yeCJoOEWuPd2WVjvAvAYgADBn0BXK52uBM8nbKzA'
OAUTH_TOKEN = '1325576605-VMpYD6O1GVZpm83XhlGO6LRNIswOJz73cr8Ni7h'
OAUTH_TOKEN_SECRET = 'vlAcWQuIZ3tOA7fYoLAzepOxxoyCfYs9bqkg83Enrg3dk'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)


# Checks for the validity of the auth using the 4 properties above
                           
twitter_api = twitter.Twitter(auth=auth)

# world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)

trends = twitter_api.trends.place(_id=US_WOE_ID)
print
print json.dumps(trends, indent=1)

# Writing the given list of trending topics into a txt file, which
# can be used by the WebCrawler
def get_trend_tweets(url, filename):
	url = 'https://api.twitter.com/1.1/trends/place.json'
	con = urllib.urlopen(url)
	content = con.read()
	con.close()
	

f = open("sohaib.txt", 'w')
f.write(json.dumps(trends, indent=1))
f.close()

print "done"  # end of twitter api class 
