from gendiff.output_formates.functions import get_keys, is_diff
from gendiff.node_diff import make_diff, NotFound
import json as json_lib


def make_dict(result: list) -> dict:
    """
    function for generate one dictionary from
    list of dictionaries
    """
    result_dict = {}
    for el in result:
        result_dict.update(el)
    return result_dict


def json_diff(dict1: dict, dict2: dict, key=None, depth=None) -> dict:
    """Generate dict of differences between two dicts"""
    diff = make_diff(dict1, dict2, key)
    value1 = diff[0]
    value2 = diff[1]
    deleted = type(value2) is NotFound
    if deleted:
        return {f'- {key}': value1}
    added = type(value1) is NotFound
    if added:
        return {f'+ {key}': value2}
    equal = value1 == value2
    if equal:
        return {f'{key}': value1}
    update = value1 != value2
    if update:
        return {f'- {key}': value1, f'+ {key}': value2}


def json_recursive(*args):
    """
    Check for diff every nodes of two dictionaries and
    generate difference between them in plain formate
    """
    keys = get_keys(*args)

    def diff_func(*args, key):
        if is_diff(*args, key=key):
            return json_diff(*args, key)
        return {key: json_recursive(*[arg.get(key) for arg in args])}

    result = list(map(
        lambda key: diff_func(*args, key=key),
        keys)
    )
    return make_dict(result)


def json(dict1: dict, dict2: dict) -> str:
    """
    Accepts two Python dicts and return diff between them
    in json formate(string type)
    """
    result = json_recursive(dict1, dict2)
    return json_lib.dumps(result, indent=4)
