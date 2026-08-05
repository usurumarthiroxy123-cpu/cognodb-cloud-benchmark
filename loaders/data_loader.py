import json


def load_dataset(path):

    with open(path, "r") as file:
        return json.load(file)