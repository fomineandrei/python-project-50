PYTHON_JSON_SPECIALS = {
    None: "null",
    True: "true",
    False: "false"
}


def for_specials_converter(value) -> str:
    """Converts special Python values to json"""
    if isinstance(value, bool | None):
        return PYTHON_JSON_SPECIALS.get(value)
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
