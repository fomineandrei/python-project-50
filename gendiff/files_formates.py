import json
import yaml
from yaml.loader import SafeLoader


def json_to_dict(file_path: str):
    file_ = open(file_path, 'r')
    json_dict = json.load(file_)
    file_.close()
    return json_dict


def yaml_to_dict(file_path: str):
    file_ = open(file_path, 'r')
    yaml_dict = yaml.load(file_, Loader=SafeLoader)
    file_.close()
    return yaml_dict


FILES_FORMATES = {
    'json': json_to_dict,
    'yaml': yaml_to_dict,
}


def file_to_dict(file_path: str) -> dict:
    file_formate = file_path.split('.')[1]
    file_dict = FILES_FORMATES[file_formate](file_path)
    return file_dict
