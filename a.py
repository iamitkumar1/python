import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter Location:' )
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall('.//count')
print('Count:',len(results))
total=0
for result in results:
	total=total+int(result.text)
print('Sum:',total)