#!/usr/bin/python2.7 -tt
import io
import urllib2
from bs4 import BeautifulSoup
from sys import argv
import re

script, file_name, url_file = argv
#request to site and get response
def get_response(url):
    #configure proxy for browser
    proxy = urllib2.ProxyHandler({'http':'202.167.248.186'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'
    req = urllib2.Request(url,user_agent)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError:
        print "Bad URL or timeout"
    return response
#parse html from response
def parse_html(url):
    html = BeautifulSoup(get_response(url))
    table_tag = html.find('table')
    table_row = table_tag.find('table').findAll('tr')
    f = io.open(file_name,'w',encoding='utf-8')
    for row in table_row:
        table_data = row
        try:
            vn_line = table_data.findAll('td')[0].get_text()
        except AttributeError as error:
            print 'Not Found ',error
        write_file(vn_line.strip(' '),f)
        try:
            cn_line = table_data.findAll('td')[1].get_text()
        except AttributeError as error:
            print 'Not Found ',error
        write_file(cn_line,f)
    f.close()
#write line to file
def write_file(line,f):
    f.write(line + u'\n')
    f.write(u'----------------------\n')
def read_url_file():
    urls = []
    f = open(url_file,'r')
    for line in f:
        urls.append(line.rstrip('\n'))
    f.close()
    return urls
#main define
def main():
    urls = read_url_file()
    for url in urls:
        parse_html(url)
if __name__ == '__main__':
    main()
