from pathlib import Path
import os


def search(directory):
    for dirname, subdirlist, filelist in os.walk(directory):
        if dirname == "./src/_eko_/js/auto_generated/nodes":
            for x in os.walk(dirname):
                for file in filelist:
                    node_id = file.rstrip('.js')
                    return node_id

search(Path('.'))
