import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter Url -')
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

data =soup("span")
print(data)
reObj=re.compile('\d+')
mo=reObj.findall(data)
n=[]
for i in mo:n.append(int(i))
print(sum(n))