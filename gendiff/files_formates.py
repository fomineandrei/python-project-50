import json
import yaml
from yaml.loader import SafeLoader
from gendiff.exceptions import FileFormateError


def json_to_dict(file_path: str) -> dict:
    """Read the json file and convers data to python dict"""
    with open(file_path, 'r') as f:
        json_dict = json.load(f)
    return json_dict


def yaml_to_dict(file_path: str) -> dict:
    """Read the yml or yaml file and convers data to python dict"""
    with open(file_path, 'r') as f:
        yaml_dict = yaml.load(f, Loader=SafeLoader)
    return yaml_dict


FILES_FORMATES = {
    'json': json_to_dict,
    'yaml': yaml_to_dict,
    'yml': yaml_to_dict
}


def file_to_dict(file_path: str) -> dict:
    """
    Read data from file and converts to Python dict type
    Only JSON, YAML or YML formates
    """
    file_formate = file_path.split('.')[1]
    if file_formate not in FILES_FORMATES:
        raise FileFormateError(
            f'"{file_formate}". Use only {list(FILES_FORMATES.keys())} files'
        )
    file_dict = FILES_FORMATES[file_formate](file_path)
    return file_dict
