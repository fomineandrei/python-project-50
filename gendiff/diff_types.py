def make_diff(data1_dict: dict, data2_dict: dict, key) -> str:
    """Define type of difference for key in two dicts"""
    key_in_data1 = key in data1_dict
    key_in_data2 = key in data2_dict
    is_equal = data1_dict.get(key) == data2_dict.get(key)
    match (key_in_data1, key_in_data2, is_equal):
        case (True, True, True):
            return 'equal'
        case (True, True, False):
            return 'update'
        case (True, False, _):
            return 'deleted'
        case (False, True, _):
            return 'added'
