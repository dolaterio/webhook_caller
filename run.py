import urllib.parse
import urllib.request
import json
import sys

obj=json.load(sys.stdin)

if not 'url' in obj:
  print("No 'url' found.\n")
  sys.exit(1)

url = obj["url"]
values = obj["values"]

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
urllib.request.urlopen(req)
