from gendiff.functions import get_keys, make_dict
from gendiff.make_diff import get_diff_type, get_diff_value
import json as json_lib


def json_diff(diff: dict, key) -> dict:
    """
    Accepts diff and return diff between them
    in json formate(string type), if diff_type
    is 'nested' call json_recursive func for value
    """
    diff_type = get_diff_type(diff, key)
    diff_val = get_diff_value(diff, key)

    if diff_type == 'nested':
        return {key: json_recursive(diff_val)}

    value1 = diff_val[0]
    value2 = diff_val[1]

    if diff_type == 'deleted':
        return {f'- {key}': value1}
    if diff_type == 'added':
        return {f'+ {key}': value2}
    if diff_type == 'equal':
        return {f'{key}': value1}
    if diff_type == 'update':
        return {f'- {key}': value1, f'+ {key}': value2}


def json_recursive(diff: dict) -> dict:
    """
    Check for diff every nodes of two dictionaries and
    generate diff between them in python dict formate
    """
    keys = get_keys(diff)
    result = list(map(
        lambda key: json_diff(diff, key=key),
        keys)
    )
    return make_dict(result)


def json(diff: dict) -> str:
    """
    Accepts two Python dicts and return diff between them
    in json formate(string type)
    """
    result = json_recursive(diff)
    return json_lib.dumps(result, indent=4)
