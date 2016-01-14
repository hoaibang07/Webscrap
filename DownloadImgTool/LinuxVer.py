# coding=utf-8
__author__ = "Pham Hoai Bang"
__copyright__ = "Copyright 2015, HBC"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pham Hoai Bang"
__email__ = "hoainp@viegrid.com"

import unicodedata
from urllib2 import urlopen
import urllib
from bs4 import BeautifulSoup as bs
import urlparse
import os
import sys
import traceback
import subprocess

def main(url="http://path/to/site", output_folder="output_folder"):
    """Downloads all the images at 'http://path/to/site' to /output_folder"""

    try:
        soup = bs(urlopen(url))
        parsed = list(urlparse.urlparse(url))
        imgCount = 0

        #find all img tag
        for image in soup.findAll("img"):
            sourceImg = image["src"];

            # Don't save gif file
            if sourceImg.find('.gif') == -1:
                imgCount += 1
                print "Downloading Image %(src)s"% (image)
                filename = sourceImg.split("/")[-1]
                parsed[2] = sourceImg

                #out put file name
                outpath = os.path.join(output_folder, removeAccents(u"" + filename))
                if sourceImg.startswith("http"):
                    urllib.urlretrieve(fixurl(sourceImg), outpath)
                else:
                    urllib.urlretrieve(fixurl(urlparse.urlunparse(parsed)), outpath)

        if imgCount == 0:
            print "No image found!"
            sys.exit(-1)
        if imgCount == 1:
            print "Completed! Downloaded %d image" %imgCount
        else:
            print "Completed! Downloaded %d images" %imgCount

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)

# Convert URL from unicode to ascii
def fixurl(url):
    # turn string into unicode
    if not isinstance(url,unicode):
        url = url.decode('utf8')

    # parse it
    parsed = urlparse.urlsplit(url)

    # divide the netloc further
    userpass,at,hostport = parsed.netloc.rpartition('@')
    user,colon1,pass_ = userpass.partition(':')
    host,colon2,port = hostport.partition(':')

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
        urllib.quote(urllib.unquote(pce).encode('utf8'),'')
        for pce in parsed.path.split('/')
    )
    query = urllib.quote(urllib.unquote(parsed.query).encode('utf8'),'=&?/')
    fragment = urllib.quote(urllib.unquote(parsed.fragment).encode('utf8'))

    # put it back together
    netloc = ''.join((user,colon1,pass_,at,host,colon2,port))
    return urlparse.urlunsplit((scheme,netloc,path,query,fragment))

# removeAccents of string - support Vietnamese
def removeAccents(s):
    stemp = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    # stemp = stemp.replace(u"Đ","D")
    # stemp = stemp.replace(u"Ư","U")
    # stemp = stemp.replace(u"Ơ","O")
    # stemp = stemp.replace(u"đ","d")
    # stemp = stemp.replace(u"ư","u")
    # stemp = stemp.replace(u"ơ","o")

    stemp2 = list(stemp)
    for x in stemp2:
    	if x == u'Đ':
    		x = 'D'
    	if x == u'Ư':
    		x = 'U'
    	if x == u'Ơ':
    		x = 'O'
    	if x == u'đ':
    		x = 'd'
    	if x == u'ư':
    		x = 'u'
    	if x == u'ơ':
    		x = 'o'
    return ''.join(stemp2)

    
# show message to user enter correct format
def _usage():
    print 'Please usage: python DownloadImgsFromUrl.py \"http://example.com\" \"output_folder_path\"'
    sys.exit(-1)

if __name__ == "__main__":
    url = ""
    output_folder = ""
    try:
        if sys.argv[-2].startswith("http"):
            url = sys.argv[-2]
            output_folder = sys.argv[-1]
        else:
            _usage()
    except Exception, e:
        _usage()
    main(url, output_folder)