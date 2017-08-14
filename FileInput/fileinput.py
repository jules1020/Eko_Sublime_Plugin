import json


def transform(metadata):
    retval = []
    with open("autocomplete.json") as file_object:
        metadata = json.load(file_object)
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
