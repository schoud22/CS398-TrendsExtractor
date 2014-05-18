#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2

'''
Created on 21-Aug-2013

@author: Nithin K Anil (itsnka@gmail.com)
'''
class GoogleResult:
    def __init__(self):
        self.name = None
        self.link = None
        self.description = None
        self.thumb = None
        self.cached = None
        self.page = None
        self.index = None

class SearchEngine:
    @staticmethod
    def search(query, pages = 1):
        results = []
        for i in range(pages):
            url = get_search_url(query, i)
            html = get_html(url)
            if html:
                soup = BeautifulSoup(html)
                lis = soup.findAll("li", attrs = { "class" : "sa_wr" })
                j = 0
                for li in lis:
                    #print li
                    res = GoogleResult()
                    res.page = i
                    res.index = j
                    a = li.find("a")
                    res.name = a.text.strip()
                    #print res.name
                    res.link = a["href"]
                    rawurl=res.link
                    url=rawurl.split('&sa')
                    res.link = url[0]
                    if res.link.startswith("/search?"):
                        # this is not an external link, so skip it (advertisements and search suggestions)
                        continue
                    sdiv = li.find("p")
                    #print sdiv
                    if sdiv:
                        res.description = sdiv.text.strip()
                    results.append(res)
                    j = j + 1
        return results
   
def normalize_query(query):
    return query.strip().replace(":", "%3A").replace("+", "%2B").replace("&", "%26").replace(" ", "+")
 
def get_search_url(query, page = 1):
    url="http://www.bing.com/search?q=%s&first=%i" % (normalize_query(query), page * 10)
    #print url
    return url

    
def get_html(url):
    try:
        request = urllib2.Request(url)
        request.add_header("User-Agent", "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101")
        #print request
        html = urllib2.urlopen(request).read()
        #print html
        return html
    except:
        print "Error accessing:%s Check your Internet Connection", url
        return None 
