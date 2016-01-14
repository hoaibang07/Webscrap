import requests
import io

for x in xrange(1,10):
	r = requests.get('http://www.yellowbridge.com/chinese/sentsearch.php?word=%E7%94%B5%E8%84%91')
	filename = 'phpsessionid.txt'
	f = io.open(filename, 'w', encoding='utf-8')
	for c in r.cookies:
	    print(c.value)
	    f.write(c.value)