from gendiff.interface import make_diff
from gendiff.output_formates.recursive_decorator import recursive_decorator


def is_any_dict(*args):
    is_dicts = [isinstance(arg, dict) for arg in args]
    return any(is_dicts)


def stylish_decor(main_func_result, key, depth):
    indent = ' ' * depth * 4
    if key is None:
        return '{\n' + '\n'.join(main_func_result) + f'\n{indent}' + '}'
    return f'{indent}{key}: ' + '{\n' + \
        '\n'.join(main_func_result) + f'\n{indent}' + '}'


@recursive_decorator(stylish_decor)
def stylish_dict(node, key=None, depth=0):
    indent = 4 * ' ' * depth
    return f'{indent}{key}: {node}'


@recursive_decorator(stylish_decor)
def stylish(node1, node2, key=None, depth=0):
    diff = make_diff(node1, node2, key)
    diff_key, diff_value = list(diff.items())[0]
    key = diff_value[0]
    value = diff_value[1:]
    for index in range(0, len(value)):
        if isinstance(value[index], dict):
            value[index] = stylish_dict(value[index], depth=depth)
    indent = ' ' * (depth * 4 - 2)
    diff_dict = {
        'equal': f'{indent}  {key}: {value[0]}',
        'update': f'{indent}- {key}: {value[0]}\n{indent}+ {key}: {value[1]}',
        'deleted': f'{indent}- {key}: {value[0]}',
        'added': f'{indent}+ {key}: {value[1]}'
    }
    return diff_dict[diff_key]
