DIFF_DICT = {
    (True, True, True): 'equal',
    (True, True, False): 'update',
    (True, False, False): 'deleted',
    (False, True, False): 'added',
}


def is_key_in(dict_data, key):
    return key in dict_data


def is_values_equal(data1_value, data2_value):
    return data1_value == data2_value


def make_diff_key(dict1, dict2, key):
    return (
        is_key_in(dict1, key),
        is_key_in(dict2, key),
        is_values_equal(dict1.get(key), dict2.get(key)),
    )


def make_diff(data1_dict, data2_dict, key):
    diff_key = make_diff_key(data1_dict, data2_dict, key)
    return DIFF_DICT[diff_key]
