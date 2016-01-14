from selenium import webdriver
from bs4 import BeautifulSoup
# from pyvirtualdisplay import Display

#hidden firefox
# display = Display(visible=0, size=(800, 600))
# display.start()

# browser = webdriver.Firefox()
browser = webdriver.PhantomJS()

anime47url = 'http://anime47.com/xem-phim-one-piece-dao-hai-tac-ep-003/76750.html'
browser.get(anime47url)

show_hide = browser.find_elements_by_class_name('show_hide')[0]
show_hide.click()

content = browser.page_source

soup = BeautifulSoup(content)
linkDownload = soup.find('div', attrs = {'id' : 'taiphim'})

print linkDownload

browser.quit()

# display.stop()