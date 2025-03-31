from gendiff.node_diff import make_diff, NotFound
from gendiff.output_formates.functions import (
    for_specials_converter,
    is_diff,
    get_keys
)


def python_to_stylish(*args, depth=None) -> list:
    """Converts python values to special stylish formate"""
    return [
        stylish(arg, arg, depth=depth) if isinstance(arg, dict)
        else for_specials_converter(arg)
        for arg in args
    ]


def stylish_diff(dict1: dict, dict2: dict, key=None, depth=None) -> str:
    """
    Accepts two Python dicts and return diff between them
    in stylish formate(string type)
    """
    diff = make_diff(dict1, dict2, key)
    stylish_vals = python_to_stylish(
        *diff, depth=depth
    )
    value1 = stylish_vals[0]
    value2 = stylish_vals[1]
    diff_sign_space = 2
    spaces_quantity = 4 * depth
    indent = ' ' * (spaces_quantity - diff_sign_space)
    deleted = type(value2) is NotFound
    if deleted:
        return f'{indent}- {key}: {value1}'
    added = type(value1) is NotFound
    if added:
        return f'{indent}+ {key}: {value2}'
    equal = value1 == value2
    if equal:
        return f'{indent}  {key}: {value1}'
    update = value1 != value2
    if update:
        return f'{indent}- {key}: {value1}\n{indent}+ {key}: {value2}'


def stylish(*args, depth=0):
    """
    Check for diff every nodes of two dictionaries and
    generate diff between them in stylish formate
    """
    keys = get_keys(*args)
    tab = 4 * ' '

    def diff_func(*args, key, depth):
        if is_diff(*args, key=key):
            return stylish_diff(*args, key, depth)
        indent = tab * depth
        return f'{indent}{key}: ' + \
            stylish(*[arg.get(key) for arg in args], depth=depth)

    result = list(map(
        lambda key: diff_func(*args, key=key, depth=depth + 1),
        keys)
    )
    indent = tab * depth
    return '{\n' + '\n'.join(result) + f'\n{indent}' + '}'
