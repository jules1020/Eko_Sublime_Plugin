print("metadatatransformer.py")


def transform(metadata):
    retval = []
    for the_object in metadata:
        autocomplete = []
        trigger = the_object["name"]
        autocomplete.append(the_object["name"])
        autocomplete.append(trigger)
        retval.append(autocomplete)
    return retval
