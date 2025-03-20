from gendiff.diff_types import make_diff
from gendiff.output_formates.functions import (
    recursive_decorator,
    python_to_json_decoder
)


def depth_default_stylish() -> int:
    """stylish formate default depth for decorator"""
    return 0


def depth_func_stylish(depth: int, key) -> int:
    """stylish formate depth function for decorator"""
    return depth + 1


def diff_decor_stylish(*args, key, depth: int, recursive_func) -> str:
    """stylish formate decorate function for diff func"""
    tab = 4 * ' '
    indent = tab * depth
    return f'{indent}{key}: ' + \
        recursive_func(*[arg.get(key) for arg in args], depth=depth)


def result_decor(result: list, depth: int) -> str:
    """stylish formate decorate function for recursive decorator result"""
    tab = 4 * ' '
    indent = tab * depth
    return '{\n' + '\n'.join(result) + f'\n{indent}' + '}'


PROCESSING_FUNCS = [
    depth_default_stylish,
    depth_func_stylish,
    diff_decor_stylish,
    result_decor
]


@recursive_decorator(*PROCESSING_FUNCS)
def stylish_dict(value: dict, key, depth: int) -> str:
    """Converts python dict to stylish formate(str type)"""
    json_value = python_to_json_decoder(value.get(key))
    tab = 4 * ' '
    indent = tab * depth
    return f'{indent}{key}: {json_value}'


def python_to_stylish(*args, depth=None) -> list:
    """Converts python values to special stylish formate"""
    return [
        stylish_dict(arg, depth=depth) if isinstance(arg, dict)
        else python_to_json_decoder(arg)
        for arg in args
    ]


@recursive_decorator(*PROCESSING_FUNCS)
def stylish(dict1: dict, dict2: dict, key=None, depth=None) -> str:
    """
    Accepts two Python dicts and return diff between them
    in stylish formate(string type)
    """
    diff_key = make_diff(dict1, dict2, key)
    stylish_vals = python_to_stylish(
        dict1.get(key), dict2.get(key), depth=depth
    )
    diff_sign_space = 2
    spaces_quantity = 4 * depth
    indent = ' ' * (spaces_quantity - diff_sign_space)
    diff_dict = {
        'equal': f'{indent}  {key}: {stylish_vals[0]}',
        'update': f'{indent}- {key}: {stylish_vals[0]}'
        f'\n{indent}+ {key}: {stylish_vals[1]}',
        'deleted': f'{indent}- {key}: {stylish_vals[0]}',
        'added': f'{indent}+ {key}: {stylish_vals[1]}'
    }
    return diff_dict[diff_key]
