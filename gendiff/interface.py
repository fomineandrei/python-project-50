def is_key_in(some_dict, key):
    return key in some_dict


def is_values_equal(dict1, dict2, key):
    return dict1.get(key, 'No key') == dict2.get(key, 'No key')


def make_diff_dict(dict1, dict2, key):
    dict1_str = f'{key}: {dict1.get(key)}'
    dict2_str = f'{key}: {dict2.get(key)}'
    return {
        (True, True, True): f'  {dict1_str}',
        (True, True, False): f'- {dict1_str}\n+ {dict2_str}',
        (True, False, False): f'- {dict1_str}',
        (False, True, False): f'+ {dict2_str}',
    }


def make_diff_key(dict1, dict2, key):
    return (
        is_key_in(dict1, key),
        is_key_in(dict2, key),
        is_values_equal(dict1, dict2, key),
    )


def file_formate_check(file_name):
    key = file_name.split('.')[1]
    return key
