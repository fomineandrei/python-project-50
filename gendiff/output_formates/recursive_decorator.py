def is_all_not_dict(*args):
    is_dicts = [isinstance(arg, dict) for arg in args]
    return not all(is_dicts)


def recursive_decorator(decor_func):
    def inner(func):
        def wrapper(*args, key=None, depth=0):
            if is_all_not_dict(*args):
                return func(*args, key, depth)
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
            return decor_func(result, key, depth)
        return wrapper
    return inner