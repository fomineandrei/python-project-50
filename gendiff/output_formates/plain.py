from gendiff.output_formates.functions import (
    recursive_decorator,
    python_to_json_decoder,
    flatten
)
from gendiff.diff_types import make_diff


# =================Функции обработчики=======================
# Глубина по умолчанию
def depth_default_plain():
    return ''


# Расчет глубины следующего шага
def depth_func_plain(depth=None, key=None):
    return f'{depth}.{key}'.lstrip('.')


# оборачивает дифф для ключа при неконечном узле
def diff_decor_plain(*args, key, depth, recursive_func):
    return recursive_func(*[arg.get(key) for arg in args], depth=depth)


# Формирует дифф для ключей двух словарей
def result_decor(result, depth):
    return '\n'.join(flatten([arg for arg in result if arg is not None]))


# Список функций обработчиков для передачи в декоратор
PROCESSING_FUNCS = [
    depth_default_plain,
    depth_func_plain,
    diff_decor_plain,
    result_decor
]
# ===========================================================


# Переводит значения из формата Python в формат plane
def python_to_plain(*args):
    plain_values = []
    for arg in args:
        if isinstance(arg, str):
            plain_values.append(f"'{arg}'")
        elif isinstance(arg, dict | list | tuple):
            plain_values.append('[complex value]')
        else:
            plain_values.append(arg)
    return [python_to_json_decoder(val) for val in plain_values]


# Формирует дифф в формате plane
@recursive_decorator(*PROCESSING_FUNCS)
def plain(node1, node2, key=None, depth=''):
    diff_key = make_diff(node1, node2, key)
    plain_values = python_to_plain(node1.get(key), node2.get(key))
    diff_dict = {
        'equal': None,
        'added': f"Property '{depth}' was added with value: {plain_values[1]}",
        'deleted': f"Property '{depth}' was removed",
        'update': f"Property '{depth}' was updated. "
        f"From {plain_values[0]} to {plain_values[1]}"
    }
    return diff_dict[diff_key]
