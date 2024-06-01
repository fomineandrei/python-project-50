import json
import yaml


def json_to_dict(file_path: str):
    file_ = open(file_path, 'r')
    json_dict = json.load(file_)
    file_.close()
    print(json_dict)
    return json_dict


def yaml_to_dict(file_path: str):
    file_ = open(file_path, 'r')
    yaml_dict = yaml.load(file_, Loader=yaml.Loader)
    file_.close()
    print(yaml_dict)
    return yaml_dict


FILES_FORMATES = {
    'json': json_to_dict,
    'yaml': yaml_to_dict,
}


def file_to_dict(file_path: str):
    file_formate = file_path.split('.')[1]
    print(file_formate)
    file_dict = FILES_FORMATES[file_formate](file_path)
    return file_dict
