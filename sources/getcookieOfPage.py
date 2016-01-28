import requests

r = requests.get('http://www.transcripture.com/vietnamese-chinese-genesis-1.html')
for c in r.cookies:
	print(c.name)
	print('het ten')
	print(c.value)