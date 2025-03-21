from gendiff.output_formates.functions import recursive_decorator
from gendiff.diff_types import make_diff
import json as json_lib


def depth_default_json():
    """JSON default depth for decorator"""
    pass


def depth_func_json(key=None, depth=None):
    """JSON depth function for decorator"""
    pass


def diff_decor_json(*args, key, depth, recursive_func) -> dict:
    """JSON decorate function for diff func"""
    return {key: recursive_func(*[arg.get(key) for arg in args], depth=depth)}


def result_decor(result: list, depth) -> dict:
    """JSON decorate function for recursive decorator result"""
    result_dict = {}
    for el in result:
        result_dict.update(el)
    return result_dict


PROCESSING_FUNCS = [
    depth_default_json,
    depth_func_json,
    diff_decor_json,
    result_decor
]


@recursive_decorator(*PROCESSING_FUNCS)
def json_formate(dict1: dict, dict2: dict, key=None, depth=None) -> dict:
    """Generate dict of differences between two dicts"""
    diff_key = make_diff(dict1, dict2, key)
    value1 = dict1.get(key)
    value2 = dict2.get(key)
    diff_dict = {
        'equal': {f'{key}': value1},
        'added': {f'+ {key}': value2},
        'deleted': {f'- {key}': value1},
        'update': {f'- {key}': value1, f'+ {key}': value2}
    }
    return diff_dict[diff_key]


def json(dict1: dict, dict2: dict) -> str:
    """
    Accepts two Python dicts and return diff between them
    in json formate(string type)
    """
    result = json_formate(dict1, dict2)
    return json_lib.dumps(result, indent=4)
