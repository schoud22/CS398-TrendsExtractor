import urllib2
import json
import pprint
import facebook
from pprint import pprint

access_token = "CAAIjXC4LbYcBABShOdcFBV3N0Itn5ZAYJGHuloqJ0pZC76ukrwB8R8NhRWza3CcNgtiMn6lRXcHp3fGDjKyWwqCAZAqHcWRZBywcbkMTJyFhEoEiTHN17eefamLJ7I3RDx5nyL2LQfusGEzImICugOsZAtZAP3IZAkDNIfllTVrWTo9NIGhXzb8eNWoanSEnuEhj6VYyPZBGxgZDZD"
url = "https://graph.facebook.com/304916642963315/feed?access_token=" + access_token

g = facebook.GraphAPI(access_token)

data = urllib2.urlopen(url)
j = json.load(data)
posts = j["data"]
	
			
s= g.request('search', { 'q' : '&','type' : 'page', 'limit' : 10 , 'locale' : 'ar_AR' })

f = open("samples.txt", 'w')
f.write(json.dumps(s, indent=1))
f.close()

print "done" 
exit 
