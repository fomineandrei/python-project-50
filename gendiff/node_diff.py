class NotFound():
    pass


not_found = NotFound()


def make_diff(data1_dict: dict, data2_dict: dict, key) -> list:
    """Return values for key in two dicts"""
    return [
        data1_dict.get(key, not_found),
        data2_dict.get(key, not_found)
    ]
