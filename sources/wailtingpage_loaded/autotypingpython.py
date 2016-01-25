from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get("about:blank")

body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

# Load a page 
driver.get('https://translate.google.com/#en/vi')
delay = 4 # seconds
try:
    wait = WebDriverWait(driver, delay);
    elem = driver.find_elements_by_tag_name("textarea")[0];
    wait.until(EC.visibility_of(elem))
    print "Page is ready!"

    # Select elements by tag name:
    inputElement = driver.find_elements_by_tag_name("textarea")[0]
    inputElement.send_keys('wall')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('class')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('yellow')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('song')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('green')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('january')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('fail')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('christmas')

    # Now you can simulate hitting ENTER:
    inputElement.send_keys(Keys.ENTER)
    inputElement.send_keys('mail')

    # or if it is a form you can submit:
    # inputElement.submit()

    # wait.until(EC.visibilityOf(elem));
except TimeoutException:
    print "Loading took too much time!"

    #reload page
    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.F5)

# content = driver.page_source

# soup = BeautifulSoup(content)

# result_box = soup.find('span', {'id': 'result_box', 'class': 'short_text'})

# result = result_box.find('span', class_='hps')

# print result

time.sleep(5)

# close the tab
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
driver.close()