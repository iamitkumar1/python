import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ' )
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = json.loads(data.decode())
print('Count:',len(tree['comments']))

total=0
for result in tree['comments']:
	total=total+int(result['count'])
print('Sum:',total)