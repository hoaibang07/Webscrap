#import
import os.path
from urllib import urlopen
from bs4 import BeautifulSoup
import io


#init file name
filename = '/media/hbc/DLIEU/Output.txt'

#using encoding utf8
f = io.open(filename, 'w', encoding='utf-8')

for num in range(1,3):
	numStr = str(num)
	url = "http://tratu.coviet.vn/hoc-tieng-trung/cap-cau-song-ngu/vietgle-tra-tu/tat-ca/trang-" + numStr + ".html"
	html = urlopen(url)
	bsObj = BeautifulSoup(html)
	for child in bsObj.findAll("ul",{"class":"uccss"}):
	    s1 = child.find("li",{"class":"ctk"}).get_text()
	    s2 = child.find("li",{"class":"p10l"}).get_text()
	    f.write(s1 + '\n')
	    f.write(s2 + '\n')
f.close()