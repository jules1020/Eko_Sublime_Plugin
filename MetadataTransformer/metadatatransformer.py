print("metadatatransformer.py")


def transform(metadata):
    retval = []
    for the_object in metadata:
        autocomplete = []

        trigger = the_object["name"] + '\t' + 'Eko' + ' ' \
        + the_object["memberof"] + ' ' + 'Method'

        autocomplete.append(trigger)
        autocomplete.append(the_object["name"])
        retval.append(autocomplete)
    return retval
