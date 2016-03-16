import requests

r = requests.get('http://www.masokaraoke.net/list-karaoke/a/')
for c in r.cookies:
	print(c.name)
	print('het ten')
	print(c.value)