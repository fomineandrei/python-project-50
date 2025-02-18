import json
import yaml


FILE_JSON = 'file4.json'
FILE_YAML = 'file4.yaml'


def write_yaml(file_json: str, file_yaml: str):
    with open(file_json, 'r') as fr:
        json_file = json.load(fr)
        with open(file_yaml, 'w') as fw:
            yaml_formate = yaml.dump(json_file)
            fw.write(yaml_formate)


write_yaml(FILE_JSON, FILE_YAML)

        
