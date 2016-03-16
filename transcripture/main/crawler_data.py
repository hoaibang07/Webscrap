# -*- encoding: utf-8 -*-
import random
import sys
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
import os.path
from selenium.webdriver.common.by import By


zenmatePath = "/home/hbc/.mozilla/firefox/yeyuaq0s.default/extensions/firefox@zenmate.com.xpi"
ffprofile = webdriver.FirefoxProfile()
# ffprofile.set_preference("javascript.enabled", False)
# ffprofile.set_preference('permissions.default.image', 2)
# ffprofile.set_preference('permissions.default.stylesheet', 2)
# ffprofile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
ffprofile.add_extension(zenmatePath)

ffprofile.add_extension('/home/hbc/Downloads/quickjava-2.0.6-fx.xpi')
# Prevents loading the 'thank you for installing screen'
ffprofile.set_preference("thatoneguydotnet.QuickJava.curVersion", "2.0.6.1")
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.Images", 2)  # Turns images off
# Turns animated images off
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.AnimatedImage", 2)
ffprofile.set_preference(
    "thatoneguydotnet.QuickJava.startupStatus.CSS", 2)  # CSS
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


def _remove_div_vdx(soup):
    for div in soup.find_all('div', class_='vidx'):
        div.extract()
    return soup


def loadpage(urlchuong):
    try:
        # dem thoi gian thuc hien load page
        start_time = time.time()

        # Load a page
        driver.get(urlchuong)
        # delay = 10  # seconds
        # wait = WebDriverWait(driver, delay)
        # path = '/html/body/center/center/div/div[1]/a'
        # elem = driver.find_element_by_xpath(path)
        # wait.until(EC.visibility_of(elem))
        # element = WebDriverWait(driver, delay).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "/html/body/center/center/div/div[1]/a"))
        # )
        print "Page is ready!"
        endtime = time.time()
        execute_time = endtime - start_time
        print('Time page loading is %f' % execute_time)
        return True
    except Exception, e:
        print "Page is not ready!"
        se = str(e)
        print('Error detail: %s' % se)
        return False


def get_data(urlchuong_list, sachi):
    filename = 'urlsach/data/sach' + str(sachi) + '.txt'
    if os.path.isfile(filename):

        # open file in append mode
        ftmp = io.open(filename, 'a', encoding='utf-8')
    else:

        # open file in write mode
        ftmp = io.open(filename, 'w', encoding='utf-8')
    try:
        # hdrs = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #         'Connection': 'keep-alive',
        #         'Cookie': 'ipq_lip=20376774; ipq_set=1453874029; __atuvc=2%7C4; __utma=126044488.676620502.1453787537.1453787537.1453787537.1; __utmz=126044488.1453787537.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=ed3f4874b92a29b6ed036adfa5ad6fb3; ipcountry=us',
        #         'Host': 'www.transcripture.com',
        #         'Referer': 'http://www.transcripture.com/vietnamese-spanish-genesis-1.html',
        #         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'
        #         }

        # tim chuong da get duoc truoc do
        begin = da_get_den_chuong(sachi)

        #_len chinh la tong so chuong
        _len = len(urlchuong_list)

        # bien count dem so lan get chuong
        count = 0

        # x chay tu begin boi vi urlchuong_list bat dau tu 0
        # nen begin se la chuong tiep theo phai get, xem dong 110
        for x in xrange(begin, _len):
            count = count + 1

            # neu so lan get lon hon 100 thi delete tat ca cookie cua trinh
            # duyet
            if count > 50:
                count = 0
                driver.delete_all_cookies()

            timesl = random.uniform(2.0, 3.0)
            print('Time sleep is %f seconds' % timesl)

            # time sleep in 2.5 to 3.3
            time.sleep(timesl)

            urlchuong = urlchuong_list[x]
            print('Dang get chuong %d, sach %d' % (x + 1, sachi))

            # urlchuong = 'http://www.transcripture.com/vietnamese-chinese-revelation-3.html'
            # # create request
            # req = urllib2.Request(urlchuong, headers=hdrs)

            # # get response
            # response = urllib2.urlopen(req)
            # soup = BeautifulSoup(response.read())
            ct = 0
            while True:

                # Neu load page thanh cong
                if(loadpage(urlchuong)):
                    ct = 0
                    break
                else:

                    # dem loi tang len 1
                    ct = ct + 1
                    if(ct == 4):

                        # close file
                        ftmp.close()
                        print('Not load the page. program will exit')
                        driver.close()
                        sys.exit()

            content = driver.page_source
            soup = BeautifulSoup(content)
            soup = _remove_div_vdx(soup)

            # print soup

            table_tag = soup.find_all(
                'table', attrs={'width': '100%', 'cellspacing': '0'})[0]
            tr_tags = table_tag.find_all('tr')
            _len_trtags = len(tr_tags)

            # in first tr tag:
            h2_class = tr_tags[0].find_all('h2', class_='cphd')
            ftmp.write(u'' + h2_class[0].get_text() + '|')
            ftmp.write(u'' + h2_class[1].get_text() + '\n')

            # print table_tag
            for j in xrange(1, _len_trtags):
                data = tr_tags[j].get_text('|')
                ftmp.write(u'' + data + '\n')

        # close file
        ftmp.close()

    except Exception, e:
        print e

        # close file
        ftmp.close()


def bo_sung_data(sachi):
    sach_url = 'urlsach/data/sach' + str(sachi) + '.txt'
    f = open(sach_url, 'r')
    fname = 'urlsach/sach' + str(sachi) + '.txt'
    if :
        pass


def get_num_lines_file(file):
    return sum(1 for line in file)


def da_get_den_chuong(sachi):

    # lay ve so chuong cua sach cung la so dong trong file urlsach
    num_lines = get_num_lines_file(
        open('urlsach/sach' + str(sachi) + '.txt', 'r'))
    fname = 'urlsach/data/sach' + str(sachi) + '.txt'
    data = open(fname).read()

    # kiem tra xem moi dong trong file sach data da co chuong cac so nay chua
    for i in xrange(1, num_lines + 1):
        key = str(i)
        if key not in data:
            return (i - 1)

    # neu nhu tat ca key deu co thi return ve num_lines
    return num_lines


def da_get_den_sach(urlsach_file):
    num_lines = get_num_lines_file(urlsach_file)
    filename = 'urlsach/data/sach'
    for x in xrange(1, num_lines + 1):

        # kiem tra xem da ton tai duong dan data sach nay hay chua
        if not os.path.isfile(filename + str(x) + '.txt'):
            return (x - 1)
    return num_lines


def main():
    urlsach_file = open('urlsach.txt', 'r')
    begin = da_get_den_sach(urlsach_file)

    # kiem tra xem file nay da get day du cac chuong chua, neu du roi thi bat dau tu sach tiep
    # neu chua du thi bat dau tu sach nay
    fname = 'urlsach/sach' + str(begin) + '.txt'
    num_lines = get_num_lines_file(open(fname, 'r'))

    # neu da get tat ca cac chuong thi begin duoc gan bang begin + 1(tuc la
    # bat dau tu sach tiep theo)
    if num_lines == da_get_den_chuong(begin):
        begin = begin + 1
    sosachget = 0
    for x in xrange(begin, num_lines + 1):
        sosachget = sosachget + 1

        # Khoang 7 cuon thi dung lai de doi ip
        if sosachget % 8 == 0:
            driver.get(
                'file:///media/hbc/DLIEU/Users/Hoaibang/My%20Documents/GitHub/Webscrap/transcripture/main/notice.html')
            print('Nhap vao mot ky tu bat ky de tiep tuc chuong trinh')
            key = raw_input()

        # remove all cookie selenium webdriver
        driver.delete_all_cookies()

        print('Dang get data sach %d' % x)
        urlchuong_list = []
        filename = 'urlsach/sach' + str(x) + '.txt'
        urlchuong_file = open(filename, 'r')
        for line in urlchuong_file:
            # print(line)
            urlchuong_list.append(line.rstrip())
        get_data(urlchuong_list, x)
        urlchuong_file.close()

if __name__ == '__main__':
    driver.set_page_load_timeout(15)
    driver.get("about:blank")
    print('Nhap vao mot ky tu bat ky de tiep tuc chuong trinh')
    key = raw_input()
    main()

    # close the tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    driver.close()

    # urlchuong_list = ['http://www.transcripture.com/vietnamese-chinese-exodus-1.html']
    # get_data(urlchuong_list, 2)
