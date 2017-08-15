import json
import urllib.request


def url_to_json(metadata):
    with urllib.request.urlopen(metadata) as url:
        data = json.loads(url.read().decode())
        print(data)
        return (data)
url_to_json("https://developer.helloeko.com/api/autocomplete.json")