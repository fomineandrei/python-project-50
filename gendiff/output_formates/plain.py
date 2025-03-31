from gendiff.output_formates.functions import (
    for_specials_converter,
    flatten,
    get_keys,
    is_diff
)
from gendiff.node_diff import make_diff, NotFound


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


def plain_diff(node1: dict, node2: dict, key=None, depth='') -> str:
    """
    Accepts two Python dicts and return diff between them
    in plain formate(string type)
    """
    diff = make_diff(node1, node2, key)
    plain_values = python_to_plain(*diff)
    value1 = plain_values[0]
    value2 = plain_values[1]
    deleted = type(value2) is NotFound
    if deleted:
        return f"Property '{depth}' was removed"
    added = type(value1) is NotFound
    if added:
        return f"Property '{depth}' was added with value: {value2}"
    equal = value1 == value2
    if equal:
        return
    update = value1 != value2
    if update:
        return f"Property '{depth}' was updated. From {value1} to {value2}"


def plain(*args, depth=''):
    """
    Check for diff every nodes of two dictionaries and
    generate difference between them in plain formate
    """
    keys = get_keys(*args)

    def diff_func(*args, key, depth=''):
        depth = f'{depth}.{key}'.lstrip('.')
        if is_diff(*args, key=key):
            return plain_diff(*args, key, depth)
        return plain(*[arg.get(key) for arg in args], depth=depth)

    result = list(map(
        lambda key: diff_func(*args, key=key, depth=depth),
        keys)
    )
    return '\n'.join(flatten([arg for arg in result if arg is not None]))
