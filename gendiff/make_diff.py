from gendiff.functions import get_keys, make_dict


class NotFound():
    pass


not_found = NotFound()


def node_diff(data1: dict, data2: dict, key) -> dict:
    """
    Return diff of node(key)
    formate of diff: {'diff': type, 'result': (val1, val2)}
    For type='nested' 'result' value is diff.
    Valid values for 'diff' key:
    'deleted', 'added', 'equal', 'update' or 'nested'.
    """
    value1 = data1.get(key, not_found)
    value2 = data2.get(key, not_found)
    nested = isinstance(value1, dict) and isinstance(value2, dict)
    if nested:
        return {key: {'diff': 'nested', 'result': make_diff(value1, value2)}}
    deleted = type(value2) is NotFound
    added = type(value1) is NotFound
    equal = value1 == value2
    update = value1 != value2
    if deleted:
        diff_type = 'deleted'
    elif added:
        diff_type = 'added'
    elif equal:
        diff_type = 'equal'
    elif update:
        diff_type = 'update'
    return {key: {'diff': diff_type, 'result': (value1, value2)}}


def make_diff(data1_dict: dict, data2_dict: dict) -> dict:
    """Return python dict of differences between two dicts"""
    keys = get_keys(data1_dict, data2_dict)
    result = list(map(lambda key: node_diff(data1_dict, data2_dict, key), keys))
    return make_dict(result)


def get_diff_type(diff_node: dict, key) -> str:
    """Return diff type from diff(result of make_diff func)"""
    return diff_node[key]['diff']


def get_diff_value(diff_node: dict, key):
    """Return diff value from diff(result of make_diff func)"""
    return diff_node[key]['result']
