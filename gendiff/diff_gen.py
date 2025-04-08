from gendiff.files_formates import file_to_dict
from gendiff.cli import parse_func
from gendiff.output_formates import OUTPUT_FORMATES
from gendiff.exceptions import OutputFormateError
from gendiff.make_diff import make_diff


def generate_diff(first_file: str,
                  second_file: str,
                  format: str = 'stylish') -> str:
    """
    Generate diff between two JSON, YAML or YML files

    Arguments: two paths of files,
               output formate(optional) - 'stylish', 'plain' or 'json'
               default value - 'stylish'

    Return diff between two files in string type
    """
    if format not in OUTPUT_FORMATES:
        raise OutputFormateError(
            f'"{format}". Choose from {list(OUTPUT_FORMATES.keys())}'
        )
    output_formate_func = OUTPUT_FORMATES[format]
    dict1 = file_to_dict(first_file)
    dict2 = file_to_dict(second_file)
    diff = make_diff(dict1, dict2)
    return output_formate_func(diff)


def output_func():
    """Print difference for parsed arguments"""
    kwargs = vars(parse_func())
    print(generate_diff(**kwargs))
