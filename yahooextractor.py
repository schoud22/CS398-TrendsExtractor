import urllib
import urllib2
import sys
# from config.settings import *

def fetch_woeid_details(woeid):
    values = {'appid': 'HTLeNizV34H33bOH5ZSeLMsw1qFcb1POf6aykZqISEr1BDwZ_qsTgNlWCkVO.G2ebcQ5dK8-', 'format': 'json'}
    data = urllib.urlencode(values)

    url = 'http://where.yahooapis.com/v1/place/%s?%s' % (woeid, data)
    requested = urllib2.Request(url)

    try:
        response = urllib2.urlopen(requested)
        page_reader = response.read()

	return page_reader
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
        return None


if __name__ == '__main__':
    import json

    place = 1      # WORLD WOEID
    result = json.loads(fetch_woeid_details(place))
    print json.dumps(result, indent=5)
    
    
