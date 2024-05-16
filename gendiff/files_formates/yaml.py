import yaml
from yaml import Loader


def file_to_dict(file_path):
    file_ = open(file_path, 'r')
    yaml_dict = yaml.load(file_, Loader=Loader)
    file_.close()
    return yaml_dict
