import json
import yaml
from yaml.loader import BaseLoader


# From Python to JSON decoder dictionary(bool and None data formate)
JSON_TO_PYTHON_DECODER = {
    None: 'null',
    True: 'true',
    False: 'false'
}


def decode_func(dict_):
    for key, value in dict_.items():
        if not isinstance(value, bool | None):
            continue
        else:
            dict_[key] = JSON_TO_PYTHON_DECODER[value]
    return dict_


def json_to_dict(file_path: str):
    with open(file_path, 'r') as f:
        json_dict = json.load(f, object_hook=decode_func)
    return json_dict


def yaml_to_dict(file_path: str):
    with open(file_path, 'r') as f:
        yaml_dict = yaml.load(f, Loader=BaseLoader)
    return yaml_dict


FILES_FORMATES = {
    'json': json_to_dict,
    'yaml': yaml_to_dict,
    'yml': yaml_to_dict
}


def file_to_dict(file_path: str) -> dict:
    file_formate = file_path.split('.')[1]
    file_dict = FILES_FORMATES[file_formate](file_path)
    return file_dict
