import json
import os


def file_is_empty(path):
    if file_exists(path):
        return os.stat(path).st_size != 0


def file_exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True


def is_accessible(path, mode="r"):
    try:
        file = open(path, mode)
        file.close()
    except:
        return False
    return True

def read_file(path):
    if file_exists(path):
        with open(path) as file:
            return json.load(file)