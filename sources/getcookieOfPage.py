import requests

r = requests.get('https://translate.google.com/#en/vi/yellow')
for c in r.cookies:
	print(c.name)
	print('het ten')
	print(c.value)