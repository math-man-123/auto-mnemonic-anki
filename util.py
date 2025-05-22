import json


# opens file at given path with UTF-8 encoding
def open_file(path, read_write):
    return open(path, read_write, newline="", encoding="utf-8")


# reads file at given path and returns content as string
def read_file(path):
    with open_file(path, "r") as file:
        return file.read().strip()


# parses JSON file at given path and retruns python dict
def load_file(path):
    with open_file(path, "r") as file:
        return json.load(file)
