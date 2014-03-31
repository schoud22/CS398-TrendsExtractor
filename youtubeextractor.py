import urllib
import urllib2
import simplejson as json

trendsurl = 'https://gdata.youtube.com/feeds/api/standardfeeds/on_the_web/?alt=json&prettyprint=false&max-results=10'
result = 10

# Grab trends from the youtube api (no auth required)
def _get_trends_json():
    request = urllib2.Request(trendsurl)
    response = urllib2.urlopen(request)
    s = response.read();
    json_obj = json.loads(s)
    print json.dumps(json_obj, indent=2)


def youtube_stream_get_trends():
    trends_json = _get_trends_json()
    trends = []
    
def _main():
    trends = youtube_stream_get_trends()
    for t in trends:
        print t
    print ''

if __name__ == '__main__':
     exit(_main())
