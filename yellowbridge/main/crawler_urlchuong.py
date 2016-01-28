# -*- encoding: utf-8 -*-

import io
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2
import urlparse


def geturl_chuong(urlsach, i):
    filename = 'urlsach/sach' + str(i) + '.txt'
    ftmp = io.open(filename, 'w', encoding='utf-8')
    print('Dang get url sach %d'%i)
    try:
        hdrs = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive',
                'Cookie': 'ipq_lip=20376774; ipq_set=1453874029; __atuvc=2%7C4; __utma=126044488.676620502.1453787537.1453787537.1453787537.1; __utmz=126044488.1453787537.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=ed3f4874b92a29b6ed036adfa5ad6fb3; ipcountry=us',
                'Host': 'www.transcripture.com',
                'Referer': 'http://www.transcripture.com/vietnamese-spanish-genesis-1.html',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'
                }

        # create request
        req = urllib2.Request(urlsach, headers=hdrs)

        # get response
        response = urllib2.urlopen(req)

        soup = BeautifulSoup(response.read())
        # print soup
        div_tag = soup.find_all('div', attrs={'style':'width:150px; padding:5px 10px 5px 10px; line-height:135%'})[0]
        # print div_tag
        for link in div_tag.find_all('a'):
            url = link.get('href')
            # print url
            # url_ec = url.encode('unicode','utf-8')
            ftmp.write(u'' + url + '\n')
        
        # close file
        ftmp.close()
    except:
        print('bi nhay vao except')
        # close file
        ftmp.close()

def main():
    urlsach_list = []

    urlsach_file = open('urlsach.txt', 'r')
    for line in urlsach_file:
        # print(line)
        urlsach_list.append(line.rstrip())
    i = 1
    for url in urlsach_list:
        geturl_chuong(url, i)
        i = i + 1
        # break
    urlsach_file.close()

if __name__ == '__main__':
    main()
