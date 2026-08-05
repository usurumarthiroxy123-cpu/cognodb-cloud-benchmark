import json


def load_dataset():
    with open("dataset/sample_data.json", "r") as file:
        return json.load(file)