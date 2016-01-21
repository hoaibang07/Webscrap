from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.get("about:blank")

wordList = ['class', 'yellow', 'red', 'result', 'picture', 'image', 'folder', 'flower', 'history', 'cat', 'dog']
for word in wordList:
    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')

    url = 'https://translate.google.com/#en/vi/' + word
    print url
    # Load a page 
    driver.get("" + url + "")

    content = driver.page_source

    soup = BeautifulSoup(content)

    result_box = soup.find('span', {'id': 'result_box', 'class': 'short_text'})

    result = result_box.find('span', class_='hps')

    print result

    # close the tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

# time.sleep(3)
driver.close()