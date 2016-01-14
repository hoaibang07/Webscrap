    # destination page exploit
    url = 'http://www.yellowbridge.com/chinese/dictionary.php'

    # user_agent get from http://www.useragentstring.com/
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'

    # value is param send in post method
    # values = {'searchMode' : 'E',
    #           'word' : 'hello'
    #          }
    values = {'searchMode': searchMode,
              'word': word
              }

    # PHPSESSID is different for each session
    cookies = 'PHPSESSID=' + phpsessionid

    # header of request
    headers = {'User-Agent': user_agent, 'Cookie': cookies}

    # encode url(values)
    data = urllib.urlencode(values)

    # create request
    req = urllib2.Request(url, data, headers)

    # get response
    response = urllib2.urlopen(req)