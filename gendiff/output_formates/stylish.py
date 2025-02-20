from gendiff.interface import make_diff
from gendiff.output_formates.recursive_decorator import recursive_decorator


def is_any_dict(*args):
    is_dicts = [isinstance(arg, dict) for arg in args]
    return any(is_dicts)


def stylish_decor(func, key, depth):
    indent = ' ' * depth * 4
    if key is None:
        return '{\n' + '\n'.join(func) + f'\n{indent}' + '}'
    return f'{indent}{key}: ' + '{\n' + \
        '\n'.join(func) + f'\n{indent}' + '}'


def depth_func_stylish(key=None, depth=0):
    if key is None:
        return 0
    return depth + 1


@recursive_decorator(stylish_decor, depth_func_stylish)
def stylish_dict(node, key=None, depth=0):
    indent = 4 * ' ' * depth
    return f'{indent}{key}: {node}'


@recursive_decorator(stylish_decor, depth_func_stylish)
def stylish(node1, node2, key, depth):
    diff_key = make_diff(node1, node2, key)
    args = [node1, node2]
    for index in range(0, len(args)):
        if isinstance(args[index], dict):
            args[index] = stylish_dict(args[index], depth=depth)
    indent = ' ' * (depth * 4 - 2)
    diff_dict = {
        'equal': f'{indent}  {key}: {args[0]}',
        'update': f'{indent}- {key}: {args[0]}\n{indent}+ {key}: {args[1]}',
        'deleted': f'{indent}- {key}: {args[0]}',
        'added': f'{indent}+ {key}: {args[1]}'
    }
    return diff_dict[diff_key]
