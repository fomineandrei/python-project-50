from gendiff.make_diff import get_diff_type, get_diff_value
from gendiff.functions import for_specials_converter, get_keys


def dict_to_stylish(data: dict, depth: int) -> str:
    """Accept python dict and return dict in stylish formate"""
    keys = get_keys(data)
    tab = ' ' * 4

    def check_func(arg, depth, key):
        indent = tab * depth
        val = arg[key]
        if not isinstance(val, dict):
            return f'{indent}{key}: {val}'
        return f'{indent}{key}: ' + dict_to_stylish(val, depth)

    result = list(map(
        lambda key: check_func(data, depth=depth + 1, key=key),
        keys))
    indent = tab * depth
    return '{\n' + '\n'.join(result) + f'\n{indent}' + '}'


def python_to_stylish(*args, depth=None) -> list:
    """Converts python values to special stylish formate"""
    return [
        dict_to_stylish(arg, depth=depth) if isinstance(arg, dict)
        else for_specials_converter(arg)
        for arg in args
    ]


def stylish_diff(diff: dict, key, depth=None) -> str:
    """
    Accepts diff and return diff between them
    in stylish formate(string type), if diff_type
    is 'nested' call stylish func for value
    """
    diff_sign_space = 2
    spaces_quantity = 4 * depth
    indent = ' ' * (spaces_quantity - diff_sign_space)
    diff_type = get_diff_type(diff, key)
    diff_val = get_diff_value(diff, key)

    if diff_type == 'nested':
        return f'{indent}  {key}: ' + stylish(diff_val, depth)

    stylish_vals = python_to_stylish(
        *diff_val, depth=depth)
    value1 = stylish_vals[0]
    value2 = stylish_vals[1]

    if diff_type == 'deleted':
        return f'{indent}- {key}: {value1}'
    if diff_type == 'added':
        return f'{indent}+ {key}: {value2}'
    if diff_type == 'equal':
        return f'{indent}  {key}: {value1}'
    if diff_type == 'update':
        return f'{indent}- {key}: {value1}\n{indent}+ {key}: {value2}'


def stylish(diff: dict, depth: int = 0):
    """
    Check for diff every nodes of two dictionaries and
    generate diff between them in stylish formate
    """
    keys = get_keys(diff)
    tab = 4 * ' '

    result = list(map(
        lambda key: stylish_diff(diff, key=key, depth=depth + 1),
        keys)
    )
    indent = tab * depth
    return '{\n' + '\n'.join(result) + f'\n{indent}' + '}'
