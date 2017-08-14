import json
import urllib.request


def transform(metadata):
    retval = []
    with urllib.request.urlopen(
            "https://developer.helloeko.com/api/autocomplete.json")\
            as url:
            metadata = json.loads(url.read().decode())
    for the_object in metadata:
        autocomplete = []

        kind = ""
        for value in the_object:
            if the_object["memberof"] != "urls":
                memberof = the_object["memberof"].capitalize()
        if the_object["kind"] == "function":
            kind = "Method"
        elif the_object["kind"] == "member":
            kind = "Member"

        trigger = the_object["name"] + "\t" + "Eko" + " " \
            + memberof + " " + kind

        autocomplete.append(trigger)
        autocomplete.append(the_object["name"])
        retval.append(autocomplete)
    return retval
