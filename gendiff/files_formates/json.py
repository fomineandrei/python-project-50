import json


def file_to_dict(file_path):
    file_ = open(file_path, 'r')
    json_dict = json.load(file_)
    file_.close()
    return json_dict
