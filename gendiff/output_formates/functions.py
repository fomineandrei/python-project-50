PYTHON_TO_JSON = {
    None: "null",
    True: "true",
    False: "false"
}


def python_to_json_decoder(value) -> str:
    """Converts special Python values to json"""
    if isinstance(value, bool | None):
        return PYTHON_TO_JSON.get(value)
    return value


def flatten(items: list) -> list:
    """Converts nested list to plain list"""
    plane_items = []
    for item in items:
        if not isinstance(item, list):
            plane_items.append(item)
        else:
            plane_items.extend(item)
    return plane_items


def is_diff(*args, key=None) -> bool:
    """Check args for differences: True or False"""
    is_in_dict = [key in arg for arg in args]
    is_dict = [isinstance(arg.get(key), dict) for arg in args]
    return not all(is_dict + is_in_dict)


def get_keys(*args) -> list:
    """Collects all keys of dicts in sorted list"""
    keys_set = set()
    for arg in args:
        keys_set = keys_set | set(arg.keys())
    keys = list(keys_set)
    keys.sort()
    return keys


def recursive_decorator(depth_default, depth_func, diff_decor, result_decor):
    """
    Decorator for diff functions
    Accepts diff function and proccessing functions
    Check every node of dicts for difference and generate diff
    for them with diff function
    """
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
