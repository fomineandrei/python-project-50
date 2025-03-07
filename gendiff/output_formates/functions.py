# Словарь преобразования значений из Python в JSON
PYTHON_TO_JSON = {
    None: "null",
    True: "true",
    False: "false"
}


# Функция преобразует значение из Python в JSON
# в случае отсутствия отличий возвращает само значение
def python_to_json_decoder(value):
    if isinstance(value, bool | None):
        return PYTHON_TO_JSON.get(value)
    return value


# Вложенные списки преобразует в значения списков
def flatten(items):
    plane_items = []
    for item in items:
        if not isinstance(item, list):
            plane_items.append(item)
        else:
            plane_items.extend(item)
    return plane_items


# Проверяет, нужно ли формировать конечный дифф для ключа
def is_diff(*args, key=None):
    is_in_dict = [key in arg for arg in args]
    is_dict = [isinstance(arg.get(key), dict) for arg in args]
    return not all(is_dict + is_in_dict)


# Формирует сортированный список ключей двух словарей
def get_keys(*args):
    keys_set = set()
    for arg in args:
        keys_set = keys_set | set(arg.keys())
    keys = list(keys_set)
    keys.sort()
    return keys


# Декоратор, рекурсивно проверяет словари на различия по ключам
# оборачивает функцию диффа конечного элемента
# принимает четыре обязательные функции-обработчика для каждого формата
def recursive_decorator(depth_default, depth_func, diff_decor, result_decor):
    def inner(func):
        default = depth_default()

        def wrapper(*args, depth=default):
            keys = get_keys(*args)

            def diff_func(*args, key, depth):
                if is_diff(*args, key=key):
                    return func(*args, key, depth)
                return diff_decor(
                    *args,
                    key=key,
                    depth=depth,
                    recursive_func=wrapper)

            result = list(map(lambda key: diff_func(
                *args,
                key=key,
                depth=depth_func(depth, key)),
                keys))
            return result_decor(result, depth)
        return wrapper
    return inner
