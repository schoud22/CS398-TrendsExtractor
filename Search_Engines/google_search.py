#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2


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
                lis = soup.findAll("li", attrs = { "class" : "g" })
                j = 0
                for li in lis:
                    res = GoogleResult()
                    res.page = i
                    res.index = j
                    a = li.find("a")
                    res.name = a.text.strip()
                    res.link = a["href"]
                    rawurl=res.link
                    url=rawurl.split('&sa')
                    res.link = url[0]
                    if res.link.startswith("/search?"):
                        # this is not an external link, so skip it (advertisements and search suggestions)
                        continue
                    sdiv = li.find("div", attrs = { "class" : "s" })
                    if sdiv:
                        res.description = sdiv.text.strip()
                    results.append(res)
                    j = j + 1
        return results
   
def normalize_query(query):
    return query.strip().replace(":", "%3A").replace("+", "%2B").replace("&", "%26").replace(" ", "+")
 
def get_search_url(query, page = 0, per_page = 10):
    return "http://www.google.com/search?hl=en&q=%s&start=%i&num=%i" % (normalize_query(query), page * per_page, per_page)

    
def get_html(url):
    try:
        request = urllib2.Request(url)
        request.add_header("User-Agent", "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101")
        html = urllib2.urlopen(request).read()
        return html
    except:
        print "Error accessing:%s Check your Internet Connection", url
        return None

