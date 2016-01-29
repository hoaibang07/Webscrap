#!/usr/bin/python2.7
import urllib2
from bs4 import BeautifulSoup
from sys import argv
import re
"""
@param url: url main website
@param format_link: what format link will be crawler
@param url_file: which is store link in a file
"""
script, url, format_link_start, url_file = argv
def get_response(url_crawl):
    #configure proxy for browser
    proxy = urllib2.ProxyHandler({'http':'202.167.248.186'})
    openner = urllib2.build_opener(proxy)
    urllib2.install_opener(openner)
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'
    req = urllib2.Request(url_crawl,user_agent)
    try:
        response = urllib2.urlopen(req,timeout=5)
    except urllib2.URLError:
        print "Bad URL or timeout"
    return response
def append_link(link,links):
    if link not in links:
        links.append(link)
def get_all_link(url_crawl,crawled,to_crawl):
    html = BeautifulSoup(get_response(url_crawl))
    a_tag = html.findAll('a')
    for tag in a_tag:
        if 'href' in tag.attrs:
            link = tag.attrs['href']
            if re.match(r'^'+format_link_start,link):
                link = re.sub(r' ','%20',link)
                if link not in crawled:
                    append_link(link,to_crawl)
def crawler_web():
    to_crawl = [url]
    crawled = []
    i = 0
    while True:
        print to_crawl
        url_crawl = to_crawl.pop()
        if url_crawl is None:
            break
        get_all_link(url_crawl,crawled,to_crawl)
        crawled.append(url_crawl)
        write_file(crawled)
        i = i + 1
        print i
    return crawled
def write_file(links):
    f = open(url_file,'w')
    for link in links:
        f.write(link + '\n')
    f.close()

def main():
    crawler_web()

if __name__=='__main__':
    main()

