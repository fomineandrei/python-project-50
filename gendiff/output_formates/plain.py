from gendiff.functions import (
    for_specials_converter,
    flatten,
    get_keys
)
from gendiff.make_diff import get_diff_type, get_diff_value


def python_to_plain(*args) -> list:
    """Converts python values to special plain formate"""
    plain_values = []
    for arg in args:
        if isinstance(arg, str):
            plain_values.append(f"'{arg}'")
        elif isinstance(arg, dict | list | tuple):
            plain_values.append('[complex value]')
        else:
            plain_values.append(arg)
    return [for_specials_converter(val) for val in plain_values]


def plain_diff(diff: dict, key, depth: list = []) -> str:
    """
    Accepts diff and return diff between them
    in plain formate(string type), if diff_type
    is 'nested' call plain func for value
    """
    diff_type = get_diff_type(diff, key)
    diff_val = get_diff_value(diff, key)

    if diff_type == 'nested':
        return plain(diff_val, depth)

    depth_str = '.'.join(depth)
    plain_vals = python_to_plain(
        *diff_val)
    value1 = plain_vals[0]
    value2 = plain_vals[1]

    if diff_type == 'deleted':
        return f"Property '{depth_str}' was removed"
    if diff_type == 'added':
        return f"Property '{depth_str}' was added with value: {value2}"
    if diff_type == 'equal':
        return
    if diff_type == 'update':
        return f"Property '{depth_str}' was updated. From {value1} to {value2}"


def plain(diff: dict, depth: list = []):
    """
    Check for diff every nodes of two dictionaries and
    generate diff between them in plain formate
    """
    keys = get_keys(diff)
    result = list(map(
        lambda key: plain_diff(diff, key=key, depth=depth + [key]),
        keys)
    )
    return '\n'.join(flatten([arg for arg in result if arg is not None]))
