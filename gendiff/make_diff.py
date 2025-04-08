from gendiff.output_formates.functions import get_keys


class NotFound():
    pass


not_found = NotFound()


def make_dict(result: list) -> dict:
    """
    function for generate one dictionary from
    list of dictionaries
    """
    result_dict = {}
    for el in result:
        result_dict.update(el)
    return result_dict


def make_diff(data1_dict: dict, data2_dict: dict) -> dict:
    """Return python dict of differences between two dicts"""
    keys = get_keys(data1_dict, data2_dict)

    def node_diff(data1, data2, key):
        value1 = data1.get(key, not_found)
        value2 = data2.get(key, not_found)
        deleted = type(value2) is NotFound
        if deleted:
            return {'diff': 'deleted', 'result': {key: value1}}
        added = type(value2) is NotFound
        if added:
            return {'diff': 'added', 'result': {key: value2}}
        nested = isinstance(value1, dict) and isinstance(value2, dict)
        if nested:
            return {'diff': 'nested', 'result': {key: make_diff(value1, value2)}}
        equal = value1 == value2
        if equal:
            return {'diff': 'equal', 'result': {key: value1}}
        update = value1 != value2
        if update:
            return {'diff': 'update', 'result': {key: [value1, value2]}}
        
    result = list(map(lambda key: node_diff(data1_dict, data2_dict, key), keys))
    return make_dict(result)

        


    