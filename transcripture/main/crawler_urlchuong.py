# -*- encoding: utf-8 -*-

import io
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2
import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


zenmatePath = "/home/hbc/.mozilla/firefox/yeyuaq0s.default/extensions/firefox@zenmate.com.xpi"
ffprofile = webdriver.FirefoxProfile()
# ffprofile.set_preference("javascript.enabled", False)
# ffprofile.set_preference('permissions.default.image', 2)
# ffprofile.set_preference('permissions.default.stylesheet', 2)
# ffprofile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
ffprofile.add_extension(zenmatePath)

ffprofile.add_extension('/home/hbc/Downloads/quickjava-2.0.6-fx.xpi')
ffprofile.set_preference("thatoneguydotnet.QuickJava.curVersion", "2.0.6.1") ## Prevents loading the 'thank you for installing screen'
ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Images", 2)  ## Turns images off
ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.AnimatedImage", 2)  ## Turns animated images off
ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.CSS", 2)  ## CSS
# ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Cookies", 2)  ## Cookies
ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Flash", 2)  ## Flash
ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Java", 2)  ## Java
# ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.JavaScript", 2)  ## JavaScript
ffprofile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Silverlight", 2)  ## Silverlight

driver = webdriver.Firefox(ffprofile)


def geturl_chuong(urlsach, i):
    filename = 'urlsach/sach' + str(i) + '.txt'
    ftmp = io.open(filename, 'w', encoding='utf-8')
    print('Dang get url sach %d'%i)
    try:
        # hdrs = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #         'Connection': 'keep-alive',
        #         'Cookie': 'ipq_lip=20376774; ipq_set=1453874029; __atuvc=2%7C4; __utma=126044488.676620502.1453787537.1453787537.1453787537.1; __utmz=126044488.1453787537.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=ed3f4874b92a29b6ed036adfa5ad6fb3; ipcountry=us',
        #         'Host': 'www.transcripture.com',
        #         'Referer': 'http://www.transcripture.com/vietnamese-spanish-genesis-1.html',
        #         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'
        #         }

        # # create request
        # req = urllib2.Request(urlsach, headers=hdrs)

        # # get response
        # response = urllib2.urlopen(req)
        # soup = BeautifulSoup(response.read())

        driver.get(urlsach)
            # delay = 40 # seconds

            # try:
            #     wait = WebDriverWait(driver, delay)
            #     path = '/html/body/center/div[1]/div[2]/div[4]/table/tbody/tr[2]/td[1]/div/div[1]/form[1]/select/option[66]'
            #     elem = driver.find_element_by_xpath(path)
            #     wait.until(EC.visibility_of(elem))
            #     print "Page is ready!"
                
            # except TimeoutException:
            #     print "Loading took too much time!"

            #     #reload page
            #     body = driver.find_element_by_tag_name("body")
            #     body.send_keys(Keys.ESCAPE)
            #     body.send_keys(Keys.F5)

        content = driver.page_source
        soup = BeautifulSoup(content)

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
    except Exception, e:
        print('bi nhay vao except')
        raise e
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

    # driver = webdriver.Firefox()
    driver.get("about:blank")
    
    # open new tab
    # body = driver.find_element_by_tag_name("body")
    # body.send_keys(Keys.CONTROL + 't')
    
    # time.sleep(15)
    print('Nhap vao mot ky tu bat ky de tiep tuc chuong trinh')
    key = raw_input()
    main()
    
    # close the tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    driver.close()


