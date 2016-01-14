# import pickle
# import selenium.webdriver 

# driver = selenium.webdriver.Firefox()
# driver.get("www.yellowbridge.com")
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


# import pickle
# import selenium.webdriver 

# driver = selenium.webdriver.Firefox()
# driver.get("www.yellowbridge.com")
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)


from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.yellowbridge.com/chinese/dictionary.php')

cookie = {'PHPSESSID':'59acipjr77t15lhsh1ekcq7rr6'}
print(driver.get_cookies())