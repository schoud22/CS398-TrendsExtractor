import sys
import twitter
import urllib
import json
import urllib2
import pprint
import facebook
import logging
import re
import subprocess
import simplejson as json
from pprint import pprint


sys.stdout = open('results.txt', 'w')   #-- Used to save output in a .txt file

class twitter:
	woeid = 1 

	# Authentication into the twitter's API

	key = 'YUE5cGzChlvSmZMHlgEbw' 
	secret = 'yeCJoOEWuPd2WVjvAvAYgADBn0BXK52uBM8nbKzA'
	authtoken = '1325576605-VMpYD6O1GVZpm83XhlGO6LRNIswOJz73cr8Ni7h'
	authsecret = 'vlAcWQuIZ3tOA7fYoLAzepOxxoyCfYs9bqkg83Enrg3dk'

	auth = twitter.oauth.OAuth(authtoken, authsecret,
							   key, secret)

	url = 'https://api.twitter.com/1.1/trends/place.json'							   
	twit_api = twitter.Twitter(auth=auth)

	# world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
	trends = twit_api.trends.place(_id=woeid, exclude='hashtags')

	names = [trend['name'] for trend in trends[0]['trends']]
	print 
	for name in names:
		print name
		 
	def get_trend_tweets(url, filename):
		url = 'https://api.twitter.com/1.1/trends/place.json'
		con = urllib.urlopen(url)
		x = con.read()
		con.close()
		
class facebook:
		#Authentication for Facebook's API
	access_token = '601828769885575|fSYx5sCM1s7s_LbEg_xJoVRoheI'
	url = 'https://graph.facebook.com/304916642963315/feed?access_token=' + access_token

	#Searching for trending topics from facebooks trend API
	search = facebook.GraphAPI(access_token)

	data = urllib.urlopen(url)
	j = json.load(data)
	search_trend = search.request('search', { 'q' : '&','type' : 'page', 'limit' : 10 , 'locale' : 'ar_AR' })
	#print out the keywords only--
	trends = [name['name'] for name in search_trend['data']]	
	
	print json.dumps(trends, indent=1)
	
class google:
	resulturl = ''

	def __init__(self,resulturl):
			self.resulturl = resulturl

	def get(self,formats):

			import urllib2
			html = urllib2.urlopen(self.resulturl).read(1000000)
		
			import re
			links = re.findall('<a href="([^"]+)">(.+)</a></span></li>', html)
			#json object returned as result
			if formats is "json":
				import json
				result = json.dumps(links)
				return result
			else:
				return links
				
#creating instance of the class

#trending topics hourly updated through google's API 
gtrend = google('http://www.google.com/trends/hottrends/atom/hourly')
trend = gtrend.get('');
for t in trend: 	#output trending "keywords" only
		print t[1]

