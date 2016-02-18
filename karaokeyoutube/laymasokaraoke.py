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
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os.path
from selenium.webdriver.common.by import By


# Crawler http://www.masokaraoke.net
# Band ip after 30 time request


# zenmatePath = "/home/hbc/.mozilla/firefox/yeyuaq0s.default/extensions/firefox@zenmate.com.xpi"
ffprofile = webdriver.FirefoxProfile()
# ffprofile.set_preference("javascript.enabled", False)
# ffprofile.set_preference('permissions.default.image', 2)
# ffprofile.set_preference('permissions.default.stylesheet', 2)
# ffprofile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# ffprofile.add_extension(zenmatePath)

# add Toggle JS to firefox
ffprofile.add_extension('/home/hbc/Downloads/toggle_js-0.8-fx.xpi')


ffprofile.add_extension('/home/hbc/Downloads/quickjava-2.0.6-fx.xpi')
# Prevents loading the 'thank you for installing screen'
ffprofile.set_preference("thatoneguydotnet.QuickJava.curVersion", "2.0.6.1")
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.Images", 2)  # Turns images off
# Turns animated images off
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.AnimatedImage", 2)
# ffprofile.set_preference(
#     "thatoneguydotnet.QuickJava.startupStatus.CSS", 2)  # CSS
# ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Cookies",
# 2)  ## Cookies
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.Flash", 2)  # Flash
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.Java", 2)  # Java
# ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.JavaScript",
# 2)  ## JavaScript
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.Silverlight", 2)  # Silverlight

driver = webdriver.Firefox(ffprofile)


# remove karaoke vol version, eg: vol 29, 58, etc
def _remove_not_need_tag(soup):
    for span_tag in soup.find_all('span', attrs={'style': 'font-size: 14px!important;text-transform: uppercase!important;'}):
        span_tag.extract()
    for div_tag in soup.find_all('div', attrs = {'style':'margin-top:-5px;'}):
        div_tag.extract()
    return soup


def getResponseFromGetMethod(page_older):
    url = "http://www.masokaraoke.net/list-karaoke//?page=" + str(page_older)

    # header of request
    hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': 'PHPSESSID=5fuh1fj7fehs141ju2jpv68ek2',
           'Host': 'www.masokaraoke.net',
           'Referer': 'http://www.masokaraoke.net',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0'
           }

    # create request
    req = urllib2.Request(url, headers = hdr)

    # get response
    response = urllib2.urlopen(req)
    
    # return soup
    return response


# def loadpage(url):
#     try:
#         # dem thoi gian thuc hien load page
#         start_time = time.time()

#         # Load a page
#         driver.get(urlchuong)
#         print "Page is ready!"
#         endtime = time.time()
#         execute_time = endtime - start_time
#         print('Time page loading is %f' % execute_time)
#         return True
#     except Exception, e:
#         print "Page is not ready!"
#         se = str(e)
#         print('Error detail: %s' % se)
#         return False
    

def extract_data(soup):
    result = soup.find_all('div', attrs = {'id':'resultSong', 'style':'width:476px;'})[0]
    result = _remove_not_need_tag(result)
    try:
        for song in result.find_all('div', class_='song'):
            songID_t = song.find('p', class_ = 'songID')
            songName_t = song.find('h1', class_ = 'songName')
            songLyric_t = song.find('h2', class_ = 'SongLyric')
            author_t = song.find('h3', class_ = 'author')
            songID = ''
            songName = ''
            songLyric = ''
            author = ''
            if songID_t.string != None:
                songID = songID_t.string.strip()
            if songName_t.string != None:
                songName = songName_t.string.strip()
            if songLyric_t.string == None:
                pass
            else:
                songLyric = songLyric_t.string.strip()
            if author_t.string != None:
                author = author_t.string.strip()
            

            #upper songName
            songName = songName.upper()
            line  = (u'' + songID +'|'  + songName + '|' + songLyric + '|' + author)

            #nomalize string
            pat = re.compile(r'\s+')
            line = pat.sub(' ', line)
            # line = re.sub('[\s+]', ' ', line)
            f.write(line + '\n')
    except Exception, e:
        er = str(e)
        print('Xay ra loi khi extract data, chi tiet %s'%er)
        return


def main():

    try:
        
        for x in xrange(0,511):
            print('Dang get trang %d'%x)
            url = "http://www.masokaraoke.net/list-karaoke//?page=" + str(x)
            driver.get(url)
            # response = getResponseFromGetMethod(x)
            # soup = BeautifulSoup(response.read())
            
            content = driver.page_source
            soup = BeautifulSoup(content)
            title = soup.find('title').get_text()
            if title == unicode('Tra mã số karaoke VOL 1-57 Arirang, Califonia, Việt KTV, MusicCore', 'utf-8'):
                print('Hay bat lai javascript cho trinh duyet, cam on!')
                print('Nhap vao mot ky tu bat ky de tiep tuc chuong trinh')
                key = raw_input()
                # time.sleep(1)
                # ele = driver.find_elements_by_xpath('//*[@id="target"]')[0]
                # ele.click()
                # time.sleep(2)
                print('Dang get lai trang %d'%x)
                driver.get(url)
                content = driver.page_source
                soup = BeautifulSoup(content)
            extract_data(soup)
    except Exception, e:
        print('Loi khi dang get trang %d'%x)
        print(e)
        f.close()
        return

if __name__ == '__main__':

    #output file
    if os.path.isfile('kara_list1_1_demo.txt'):
        f = io.open('kara_list1_1_demo.txt', 'a', encoding='utf-8')
    else:
        f = io.open('kara_list1_1_demo.txt', 'w', encoding='utf-8')

        #output format each line: songID|songName|songLyric|Author
        f.write(u'songID|songName|songLyric|Author' + '\n')
    driver.set_page_load_timeout(10)
    driver.get("about:blank")
    print('Nhap vao mot ky tu bat ky de tiep tuc chuong trinh')
    key = raw_input()
    main()

    # close the tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    driver.close()
    f.close()
