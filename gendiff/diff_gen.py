from gendiff.files_formates import file_to_dict
from gendiff.cli import parse_func
from gendiff.output_formates import OUTPUT_FORMATES
from gendiff.exceptions import OutputFormateError


def generate_diff(file1_path, file2_path, formate='stylish'):
    """
    Generate diff between two JSON, YAML or YML files

    Arguments: two paths of files,
               output formate(optional) - 'stylish', 'plain' or 'json'
               default value - 'stylish'

    Return diff between two files in string type
    """
    if formate not in OUTPUT_FORMATES:
        raise OutputFormateError(
            f'"{formate}". Choose from {list(OUTPUT_FORMATES.keys())}'
        )
    output_formate_func = OUTPUT_FORMATES[formate]
    dict1 = file_to_dict(file1_path)
    dict2 = file_to_dict(file2_path)
    return output_formate_func(dict1, dict2)


def output_func():
    args = parse_func()
    formate = {'formate': args.FORMAT} if args.FORMAT else {}
    print(generate_diff(args.first_file, args.second_file, **formate))
