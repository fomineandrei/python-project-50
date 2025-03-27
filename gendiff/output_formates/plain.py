from gendiff.output_formates.functions import (
    recursive_decorator,
    python_to_json_decoder,
    flatten
)
from gendiff.node_diff import make_diff, NotFound


def depth_default_plain() -> str:
    """plain formate default depth for decorator"""
    return ''


def depth_func_plain(depth=None, key=None) -> str:
    """plain formate depth function for decorator"""
    return f'{depth}.{key}'.lstrip('.')


def diff_decor_plain(*args, key, depth: str, recursive_func):
    """plain formate decorate function for diff func"""
    return recursive_func(*[arg.get(key) for arg in args], depth=depth)


def result_decor(result: list, depth) -> str:
    """plain formate decorate function for recursive decorator result"""
    return '\n'.join(flatten([arg for arg in result if arg is not None]))


PROCESSING_FUNCS = [
    depth_default_plain,
    depth_func_plain,
    diff_decor_plain,
    result_decor
]


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
    return [python_to_json_decoder(val) for val in plain_values]


@recursive_decorator(*PROCESSING_FUNCS)
def plain(node1: dict, node2: dict, key=None, depth='') -> str:
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
