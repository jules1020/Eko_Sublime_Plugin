print("metadatatransformer.py")


def transform(metadata):
    retval = []
    for the_object in metadata:
        autocomplete = []
        memberof = the_object["memberof"]
        trigger = the_object["name"]
        trigger_final = trigger + '\t' + 'Eko' + ' ' + memberof + ' ' + 'Method'
        autocomplete.append(trigger_final)
        autocomplete.append(the_object["name"])
        retval.append(autocomplete)
    return retval
