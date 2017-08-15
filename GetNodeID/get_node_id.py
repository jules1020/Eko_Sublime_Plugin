from pathlib import Path


def search(directory_in_str):
    pathlist = Path(directory_in_str).glob('**/*.')
    for path in pathlist:
        path_in_str = str(path)
        print(path_in_str)
        return path_in_str
