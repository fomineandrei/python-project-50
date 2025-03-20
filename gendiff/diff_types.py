def make_diff(data1_dict, data2_dict, key):
    key_in_data1 = key in data1_dict
    key_in_data2 = key in data2_dict
    is_equal = data1_dict.get(key) == data2_dict.get(key)
    if key_in_data1 and not key_in_data2:
        return 'deleted'
    elif not key_in_data1 and key_in_data2:
        return 'added'
    elif key_in_data1 and key_in_data2 and is_equal:
        return 'equal'
    elif key_in_data1 and key_in_data2 and not is_equal:
        return 'update'
