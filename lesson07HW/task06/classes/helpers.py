import json


def save_data_to_json(filename, data):
    with open(filename, "w") as file_dig:
        json.dump(data, file_dig, ensure_ascii=False)


def get_data_from_json(filename):
    with open(filename, "r") as file_dig:
        return json.load(file_dig)
