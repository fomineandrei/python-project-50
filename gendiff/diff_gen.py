import gendiff.interface as interface
from gendiff.cli import parse_func
from gendiff.files_formates import json, yaml


FILES_FORMATES = {
    'json': json,
    'yaml': yaml,
}


def file_dict(file_path):
    file_formate = file_path.split('.')[1]
    return FILES_FORMATES[file_formate].file_to_dict(file_path)


def generate_diff(file1_path, file2_path):
    file1_dict = file_dict(file1_path)
    file2_dict = file_dict(file2_path)
    keys = set(file1_dict.keys()) | set(file2_dict.keys())
    diff_list = []
    for key in sorted(keys):
        diff_dict = interface.make_diff_dict(
            file1_dict, file2_dict, key)
        diff_key = interface.make_diff_key(file1_dict, file2_dict, key)
        diff_list.append(diff_dict[diff_key])
    return '\n'.join(diff_list)


def output_func():
    print(generate_diff(
        parse_func().first_file,
        parse_func().second_file))
