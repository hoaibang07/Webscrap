import io
from bs4 import BeautifulSoup
import urllib2
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main(url):
    
    zenmatePath = "/home/hbc/.mozilla/firefox/yeyuaq0s.default/extensions/firefox@zenmate.com.xpi"
    ffprofile = webdriver.FirefoxProfile()
    ffprofile.add_extension(zenmatePath)
    driver = webdriver.Firefox(ffprofile)

    # driver = webdriver.Firefox()
    driver.get("about:blank")

    print('Nhap vao mot ky tu bat ky de tiep tuc chuong trinh')
    key = raw_input()

    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')

    # Load a page 
    driver.get(url)
    delay = 45 # seconds
    start_time = time.time()
    try:
        wait = WebDriverWait(driver, delay)
        path = '/html/body/center/div[1]/div[2]/div[4]/table/tbody/tr[2]/td[1]/div/div[1]/form[1]/select/option[66]'
        elem = driver.find_element_by_xpath(path)
        wait.until(EC.visibility_of(elem))
        print "Page is ready!"
        content = driver.page_source
        soup = BeautifulSoup(content)
        filename = 'urlsach.txt'
        f = io.open(filename, 'w', encoding = 'utf-8')
        form_tag = soup.find_all('form')[1]
        options_tag = form_tag.find_all('option')
        for tag in options_tag:
            url = tag.get('value')
            print url
            f.write(u'' + url + '\n')
        f.close()
    except TimeoutException:
        print "Loading took too much time!"

        #reload page
        # body = driver.find_element_by_tag_name("body")
        # body.send_keys(Keys.F5)
        driver.refresh()
    endtime = time.time()
    execute_time = endtime - start_time
    print('Time page loading is %f'%execute_time)
    
    # close the tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    driver.close()


if __name__ == '__main__':
    main_url = 'http://www.transcripture.com/english-vietnamese-genesis-1.html'
    main(main_url)
