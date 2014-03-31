import urllib
import urllib2
import json
import pprint
import facebook
from pprint import pprint

access_token = 'CAAIjXC4LbYcBAFjAm5ogj1oCVEOcQWPripEVbHEgfnIDIGALYu1t2AC4eNufnv0mPM283Cl5tIoVRgKgGkftbQbCfkGol7xCT7wMp6VqRJvA5RiIKqffooJJE2mGZBTZCorg1PUpZBWuXaOBGxBWOXldQwoGzC7rPxU4TEusMJww4rgrMqUwG1htB7GBqV6qdmQj6qowgZDZD'
url = "https://graph.facebook.com/304916642963315/feed?access_token=" + access_token

g = facebook.GraphAPI(access_token)

data = urllib.urlopen(url)
j = json.load(data)
			
search_trend = g.request('search', { 'q' : '&','type' : 'page', 'limit' : 10 , 'locale' : 'ar_AR' })

f = open("samples.txt", 'w')
f.write(json.dumps(search_trend, indent=1))
f.close()

print "done" 
exit 
