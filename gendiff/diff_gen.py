from gendiff.files_formates import file_to_dict
from gendiff.cli import parse_func
from gendiff.output_formates import OUTPUT_FORMATES


def flatten(items):
    plane_items = []
    for item in items:
        if not isinstance(item, list):
            plane_items.append(item)
        else:
            plane_items.extend(item)
    return plane_items


def generate_diff(file1, file2, formate='stylish'):
    output_formate_func = OUTPUT_FORMATES[formate]
    dict1 = file_to_dict(file1)
    dict2 = file_to_dict(file2)
    return output_formate_func(dict1, dict2)


def output_func():
    args = parse_func()
    formate = args.FORMAT if args.FORMAT in OUTPUT_FORMATES else {}
    print(generate_diff(args.first_file, args.second_file, **formate))
