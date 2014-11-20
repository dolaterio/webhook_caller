import urllib.parse
import urllib.request
import json
import sys

obj=json.load(sys.stdin)

if not 'url' in obj:
  print("No 'url' found.\n")
  sys.exit(1)

url = obj["url"]

values = {}

if "status" in obj:
  values["status"] = obj["status"]
if "stdout" in obj:
  values["stdout"] = obj["stdout"]
if "stderr" in obj:
  values["stderr"] = obj["stderr"]
if "error" in obj:
  values["error"] = obj["error"]
if "job_id" in obj:
  values["job_id"] = obj["job_id"]
if "image_id" in obj:
  values["image_id"] = obj["image_id"]
if "created_at" in obj:
  values["created_at"] = obj["created_at"]

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
urllib.request.urlopen(req)
