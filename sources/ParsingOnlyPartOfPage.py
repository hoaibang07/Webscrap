from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from urllib import urlopen

#only parse ur tag
only_ul_tags = SoupStrainer("ul")

url = "http://tratu.coviet.vn/hoc-tieng-trung/cap-cau-song-ngu/vietgle-tra-tu/tat-ca/trang-1.html"

soup = BeautifulSoup(urlopen(url), "html.parser", parse_only = only_ul_tags)
print (soup.prettify())