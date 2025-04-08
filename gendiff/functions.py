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


def get_keys(*args) -> list:
    """Collects all keys of dicts in sorted list"""
    keys_set = set()
    for arg in args:
        keys_set = keys_set | set(arg.keys())
    keys = list(keys_set)
    keys.sort()
    return keys


def make_dict(result: list) -> dict:
    """
    function for generate one dictionary from
    list of dictionaries
    """
    result_dict = {}
    for el in result:
        result_dict.update(el)
    return result_dict
