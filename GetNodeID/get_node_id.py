"""Import Path."""
import pathlib
import os


def search(directory):
    """Search for and return node ids."""
    node_id_list = []
    for dirname, subdirlist, filelist in os.walk(directory):
        if dirname == "./src/_eko_/js/auto_generated/nodes":
            for x in os.walk(dirname):
                for file in filelist:
                    node_id = file.rstrip('.js')
                    node_id_list.append(node_id)
    return node_id_list

search(pathlib.Path('.'))
