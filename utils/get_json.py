"""JSON and Urllib Modules."""
import json
import urllib.request


def url_to_json(metadata):
    """Load the JSON file from a URL."""
    with urllib.request.urlopen(metadata) as url:
        data = json.loads(url.read().decode())
        return (data)
