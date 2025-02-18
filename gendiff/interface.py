def is_key_in(data):
    return data is not None


def is_values_equal(data1, data2):
    return data1 == data2


def make_diff_dict(data1, data2, key):
    return {
        (True, True, True): {'equal': [key, data1, None]},
        (True, True, False): {'update': [key, data1, data2]},
        (True, False, False): {'deleted': [key, data1, None]},
        (False, True, False): {'added': [key, None, data2]},
    }


def make_diff_key(dict1, dict2, key):
    return (
        is_key_in(dict1),
        is_key_in(dict2),
        is_values_equal(dict1, dict2),
    )


def make_diff(file1_dict, file2_dict, key):
    diff_key = make_diff_key(file1_dict, file2_dict, key)
    diff_dict = make_diff_dict(file1_dict, file2_dict, key)
    return diff_dict[diff_key]
