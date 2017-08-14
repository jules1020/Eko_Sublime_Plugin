import json
import urllib.request

with urllib.request.urlopen(
    "https://developer.helloeko.com/api/autocomplete.json") \
        as url:
    data = json.loads(url.read().decode())
    print(data)
