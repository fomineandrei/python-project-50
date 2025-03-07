import json
import yaml
from yaml.loader import SafeLoader


# Читает и преобразует содержимое json файла в словарь
def json_to_dict(file_path: str):
    with open(file_path, 'r') as f:
        json_dict = json.load(f)
    return json_dict


# Читает и преобразует содержимое yaml файла в словарь
def yaml_to_dict(file_path: str):
    with open(file_path, 'r') as f:
        yaml_dict = yaml.load(f, Loader=SafeLoader)
    return yaml_dict


# Возможные форматы для чтения файлов
FILES_FORMATES = {
    'json': json_to_dict,
    'yaml': yaml_to_dict,
    'yml': yaml_to_dict
}


# Универсальная функция преобразования json, yaml, yml файлов в
# словарь Python
def file_to_dict(file_path: str) -> dict:
    file_formate = file_path.split('.')[1]
    file_dict = FILES_FORMATES[file_formate](file_path)
    return file_dict
