print("metadatatransformer.py")


def transform(metadata):
    retval = []
    for the_object in metadata:
        autocomplete = []

        kind = ''
        if the_object["kind"] == 'function':
            kind = 'Method'
        elif the_object["kind"] == 'member':
            kind = 'Member'

        trigger = the_object["name"] + '\t' + 'Eko' + ' ' \
            + the_object["memberof"] + ' ' + kind

        autocomplete.append(trigger)
        autocomplete.append(the_object["name"])
        retval.append(autocomplete)
    return retval
