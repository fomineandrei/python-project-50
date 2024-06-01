import gendiff.interface as interface
from gendiff.cli import parse_func
from gendiff.files_formates import file_to_dict


def generate_diff(file1_dict, file2_dict):
    print(set(file1_dict.keys()))
    keys = set(file1_dict.keys()) | set(file2_dict.keys())
    print(keys)
    diff_list = []
    for key in sorted(keys):
        diff_dict = interface.make_diff_dict(
            file1_dict, file2_dict, key)
        diff_key = interface.make_diff_key(file1_dict, file2_dict, key)
        diff_list.append(diff_dict[diff_key])
    return '\n'.join(diff_list)


def output_func():
    print(generate_diff(
        file_to_dict(parse_func().first_file),
        file_to_dict(parse_func().second_file)))
