def is_all_not_dict(*args):
    is_dicts = [isinstance(arg, dict) for arg in args]
    return not all(is_dicts)


def get_keys(*args):
    keys_set = set()
    for arg in args:
        keys_set = keys_set | set(arg.keys())
    keys = list(keys_set)
    keys.sort()
    return keys


def recursive_decorator(decor_func, depth_func):
    def inner(func):
        default = depth_func()

        def wrapper(*args, key=None, depth=default):
            if is_all_not_dict(*args):
                return func(*args, key, depth)
            keys = get_keys(*args)
            result = list(map(
                lambda key: wrapper(
                    *[arg.get(key) for arg in args],
                    key=key,
                    depth=depth_func(key=key, depth=depth)),
                keys
            ))
            return decor_func(result, key, depth)
        return wrapper
    return inner
