# coding=utf-8

import unicodedata
import urllib2
import urllib
from bs4 import BeautifulSoup
import urlparse
import os
import io
import sys
import traceback
import subprocess
from bs4 import SoupStrainer
import time

# Convert URL from unicode to ascii


def fixurl(url):
    # turn string into unicode
    if not isinstance(url, unicode):
        url = url.decode('utf8')

    # parse it
    parsed = urlparse.urlsplit(url)

    # divide the netloc further
    userpass, at, hostport = parsed.netloc.rpartition('@')
    user, colon1, pass_ = userpass.partition(':')
    host, colon2, port = hostport.partition(':')

    # encode each component
    scheme = parsed.scheme.encode('utf8')
    user = urllib.quote(user.encode('utf8'))
    colon1 = colon1.encode('utf8')
    pass_ = urllib.quote(pass_.encode('utf8'))
    at = at.encode('utf8')
    host = host.encode('idna')
    colon2 = colon2.encode('utf8')
    port = port.encode('utf8')
    path = '/'.join(  # could be encoded slashes!
        urllib.quote(urllib.unquote(pce).encode('utf8'), '')
        for pce in parsed.path.split('/')
    )
    query = urllib.quote(urllib.unquote(parsed.query).encode('utf8'), '=&?/')
    fragment = urllib.quote(urllib.unquote(parsed.fragment).encode('utf8'))

    # put it back together
    netloc = ''.join((user, colon1, pass_, at, host, colon2, port))
    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))


def getResponseFromGetMethod(key):
    # f = io.open('response.txt', 'w', encoding = 'utf-8')
    url = "https://www.youtube.com/results?search_query=" + key
    url_encode = fixurl(url);
    # values = {'search_query': key}

    # header of request
    hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Connection': 'keep-alive',
               'Cookie': 'VISITOR_INFO1_LIVE=_-mX7GX7EI0; YSC=g6Tbal56wf8; PREF=f1=50000000&f5=30',
               'Host': 'www.youtube.com',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0'
               }

    # create request
    req = urllib2.Request(url_encode, headers = hdr)
    # get response
    # response = urllib2.urlopen(req)
    #only parse h3 tag
    only_h3_tags = SoupStrainer("h3")
    soup = BeautifulSoup(urllib2.urlopen(req), "html.parser", parse_only = only_h3_tags)
    # return response
    return soup


def main():
    query_list = []
    for line in f2:
        query_list.append(line)
    f2.close()
    len_ = len(query_list)
    print('List nhac co %d bai' %len_)
    url = "https://www.youtube.com/"
    parsed = list(urlparse.urlparse(url))
    j = 0
    try:
        #da get bat dau tu bai 4
        for i in xrange(9153,9586):
            key = query_list[i] + ' KARAOKE FULL BEAT'
            j = i + 1
            begin_t = time.time()
            print('Dang get tu khoa %s, bai thu %d'%(key,j))
            soup = getResponseFromGetMethod(key)
            # soup = BeautifulSoup(response.read())
            h3_tags = soup.find_all('h3', class_ = 'yt-lockup-title ')
            a_tag_1 = h3_tags[0].find('a')
            link1 = a_tag_1.get('href')
            title1 = a_tag_1.get('title')
            title1 = title1.replace(';', ' ')
            parsed[2] = link1
            if link1.startswith("http"):
                pass
            else:
                link1 = urlparse.urlunparse(parsed)
            a_tag_2 = h3_tags[1].find('a')
            link2 = a_tag_2.get('href')
            title2 = a_tag_2.get('title')
            title2 = title2.replace(';', ' ')
            parsed[2] = link2
            if link2.startswith("http"):
                pass
            else:
                link2 = urlparse.urlunparse(parsed)


            line1 = title1 + ";;;" + link1
            # line1 = link1
            f.write(line1 + '\n')
            line2 = title2 + ";;;" + link2
            # line2 = link2
            f.write(line2 + '\n')
            end_t  = time.time()
            exe_t = end_t - begin_t
            print('Thoi gian thuc hien request la: %f'%exe_t)
        # f.write(soup.prettify())
    except Exception, e:
        print(e)
        f.close()
        return

        


if __name__ == '__main__':
    if os.path.isfile('out/youtubelist00005.txt'):
        f = io.open('out/youtubelist00005.txt', 'a', encoding = 'utf-8')
    else:
        f = io.open('out/youtubelist00005.txt', 'w', encoding = 'utf-8')
    f2 = open('kara_list1_1_songName.txt', 'r')
    main()
    f.close()
