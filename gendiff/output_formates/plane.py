from gendiff.output_formates.functions import (
    recursive_decorator,
    python_to_json_decoder
)
from gendiff.diff_types import make_diff


def flatten(items):
    plane_items = []
    for item in items:
        if not isinstance(item, list):
            plane_items.append(item)
        else:
            plane_items.extend(item)
    return plane_items


def depth_default_plane():
    return ''


def depth_func_plane(depth=None, key=None):
    return f'{depth}.{key}'.lstrip('.')


def diff_decor_plane(*args, key, depth, recursive_func):
    return recursive_func(*[arg.get(key) for arg in args], depth=depth)


def result_decor(result, depth):
    return '\n'.join(flatten([arg for arg in result if arg is not None]))


PROCESSING_FUNCS = [
    depth_default_plane,
    depth_func_plane,
    diff_decor_plane,
    result_decor
]


def python_to_plane(*args):
    plane_values = []
    for arg in args:
        if isinstance(arg, str):
            plane_values.append(f"'{arg}'")
        elif isinstance(arg, dict | list | tuple):
            plane_values.append('[complex value]')
        else:
            plane_values.append(arg)
    return [python_to_json_decoder(val) for val in plane_values]


@recursive_decorator(*PROCESSING_FUNCS)
def plane(node1, node2, key=None, depth=''):
    diff_key = make_diff(node1, node2, key)
    plane_values = python_to_plane(node1.get(key), node2.get(key))
    diff_dict = {
        'equal': None,
        'added': f"Property '{depth}' was added with value: {plane_values[1]}",
        'deleted': f"Property '{depth}' was removed",
        'update': f"Property '{depth}' was updated. "
        f"From {plane_values[0]} to {plane_values[1]}"
    }
    return diff_dict[diff_key]
