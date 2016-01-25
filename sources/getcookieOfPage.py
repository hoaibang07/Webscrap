import requests

r = requests.get('http://www.anhvietsongngu.com/alice-o-xu-than-tien-1a/')
for c in r.cookies:
	print(c.name)
	print('het ten')
	print(c.value)