from gendiff.files_formates import file_to_dict
from gendiff.cli import parse_func
from gendiff.output_formates import OUTPUT_FORMATES
from gendiff.exceptions import OutputFormateError


def generate_diff(first_file, second_file, FORMAT='stylish'):
    """
    Generate diff between two JSON, YAML or YML files

    Arguments: two paths of files,
               output formate(optional) - 'stylish', 'plain' or 'json'
               default value - 'stylish'

    Return diff between two files in string type
    """
    if FORMAT not in OUTPUT_FORMATES:
        raise OutputFormateError(
            f'"{FORMAT}". Choose from {list(OUTPUT_FORMATES.keys())}'
        )
    output_formate_func = OUTPUT_FORMATES[FORMAT]
    dict1 = file_to_dict(first_file)
    dict2 = file_to_dict(second_file)
    return output_formate_func(dict1, dict2)


def output_func():
    kwargs = vars(parse_func())
    print(generate_diff(**kwargs))
