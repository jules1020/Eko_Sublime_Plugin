def transform_nodeid(node_id_array):
    retval = []
    for node_id in node_id_array:
        query_completion = []
        trigger = node_id + "\tProject Node"
        completion = node_id
        query_completion.append(trigger)
        query_completion.append(completion)
        retval.append(query_completion)
    return retval
