#!/usr/bin/env python3


import argparse
import json


def help_func():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", dest="FORMAT")
    args = parser.parse_args()
    return args


def generate_diff(file1_path, file2_path):
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    keys = set(file1.keys()) | set(file2.keys())
    diff_list = []
    for key in sorted(list(keys)):
        if key in file1 and key in file2 and file1[key] == file2[key]:
            diff_list.append(f'  {key}: {file1[key]}')
        elif key in file1 and key in file2 and file1[key] != file2[key]:
            diff_list.append(f'- {key}: {file1[key]}')
            diff_list.append(f'+ {key}: {file2[key]}')
        elif key in file1 and key not in file2:
            diff_list.append(f'- {key}: {file1[key]}')
        elif key not in file1 and key in file2:
            diff_list.append(f'+ {key}: {file2[key]}')
    return diff_list


def output_func(diff_data):
    for element in diff_data:
        print(element)


def main():
    output_func(generate_diff(help_func().first_file, help_func().second_file))


if __name__ == '__main__':
    main()
