from HTMLParser import HTMLParser
#from urllib.parse import urlparse  #this is for python 3.x
from urlparse import urljoin     #this is for python 2.x

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        HTMLParser.__init__(self)  # call the parent's init method
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

