from gendiff.interface import make_diff


def is_all_not_dict(*args):
    is_dicts = [isinstance(arg, dict) for arg in args]
    return not all(is_dicts)


def is_any_dict(*args):
    is_dicts = [isinstance(arg, dict) for arg in args]
    return any(is_dicts)


def recursive_decorator(func):
    def wrapper(*args, key=None, depth=0):
        if is_all_not_dict(*args):
            return func(*args, key, depth)
        indent = ' ' * depth * 4
        keys_set = set()
        for arg in args:
            keys_set = keys_set | set(arg.keys())
        keys = list(keys_set)
        keys.sort()
        result = list(map(
            lambda key: wrapper(
                *[arg.get(key) for arg in args],
                key=key,
                depth=depth + 1),
            keys
        ))
        if key is None:
            return '{\n' + '\n'.join(result) + f'\n{indent}' + '}'
        return f'{indent}{key}: ' + '{\n' + \
            '\n'.join(result) + f'\n{indent}' + '}'
    return wrapper


@recursive_decorator
def stylish_dict(node, key=None, depth=0):
    indent = 4 * ' ' * depth
    return f'{indent}{key}: {node}'


@recursive_decorator
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
