# -*- encoding: utf-8 -*-

import io
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2
import urlparse


def _remove_div_vdx(soup):
    for div in soup.find_all('div', class_='vidx'):
        div.extract()
    return soup

def get_data(urlchuong_list, i):
    filename = 'urlsach/data/sach' + str(i) + '.txt'
    ftmp = io.open(filename, 'w', encoding='utf-8')
    try:
        hdrs = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive',
                'Cookie': 'ipq_lip=20376774; ipq_set=1453874029; __atuvc=2%7C4; __utma=126044488.676620502.1453787537.1453787537.1453787537.1; __utmz=126044488.1453787537.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=ed3f4874b92a29b6ed036adfa5ad6fb3; ipcountry=us',
                'Host': 'www.transcripture.com',
                'Referer': 'http://www.transcripture.com/vietnamese-spanish-genesis-1.html',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'
                }

        for urlchuong in urlchuong_list:
            # urlchuong = 'http://www.transcripture.com/vietnamese-chinese-revelation-3.html'
            
            print urlchuong

            # create request
            req = urllib2.Request(urlchuong, headers=hdrs)

            # get response
            response = urllib2.urlopen(req)
            soup = BeautifulSoup(response.read())
            soup = _remove_div_vdx(soup)

            # print soup

            table_tag = soup.find_all('table', attrs={'width':'100%', 'cellspacing':'0'})[0]
            tr_tags = table_tag.find_all('tr')
            _len = len(tr_tags)

            # in first tr tag:
            h2_class = tr_tags[0].find_all('h2', class_='cphd')
            ftmp.write(u'' + h2_class[0].get_text() + '|')
            ftmp.write(u'' + h2_class[1].get_text() + '\n')

            # print table_tag
            for x in xrange(1,_len):
                data = tr_tags[x].get_text('|')
                # print data

                # url_ec = url.encode('unicode','utf-8')
                ftmp.write(u'' + data + '\n')
    except Exception, e:
        print e
        # close file
        ftmp.close()


def main():
    for x in xrange(1,67):
        print('Dang get data sach %d'%x)
        urlchuong_list = []
        filename = 'urlsach/sach' + str(x) + '.txt'
        urlchuong_file = open(filename, 'r')
        for line in urlchuong_file:
            # print(line)
            urlchuong_list.append(line.rstrip())
        get_data(urlchuong_list, x)
        urlchuong_file.close()

if __name__ == '__main__':
    main()
    # urlchuong_list = ['http://www.transcripture.com/vietnamese-chinese-revelation-3.html']
    # get_data(urlchuong_list, 1)