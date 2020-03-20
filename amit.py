import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter Url -')
count=int(input('Enter count: '))
position=int(input('Enter position: '))

for i in range(count):
	html=urllib.request.urlopen(url,context=ctx).read()
	soup=BeautifulSoup(html,'html.parser')
	tags=soup('a')
	for j in range(position):
		url=tags[j].get('href',None)
		name=tags[j].text
print(name)