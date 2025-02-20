from gendiff.output_formates.recursive_decorator import recursive_decorator
from gendiff.interface import make_diff
from gendiff.files_formates import JSON_TO_PYTHON_DECODER


def plane_decor(main_func, key, depth):
    main_func = [value for value in main_func if value is not None]
    return '\n'.join(main_func)


def depth_func_plane(key=None, depth=''):
    if key is None:
        return depth
    elif key is not None and depth == '':
        return f'{key}'
    return f'{depth}.{key}'


@recursive_decorator(plane_decor, depth_func_plane)
def plane(node1, node2, key=None, depth=''):
    diff_key = make_diff(node1, node2, key)
    args = [node1, node2]
    for index in range(0, len(args)):
        not_string_val = JSON_TO_PYTHON_DECODER.values()
        if isinstance(args[index], dict | list | tuple):
            args[index] = '[complex value]'
        elif isinstance(args[index], str) and args[index] not in not_string_val:
            args[index] = f"'{args[index]}'"
    diff_dict = {
        'equal': None,
        'added': f"Property '{depth}' was added with value: {args[1]}",
        'deleted': f"Property '{depth}' was removed",
        'update': f"Property '{depth}' was updated. From {args[0]} to {args[1]}"
    }
    return diff_dict[diff_key]
