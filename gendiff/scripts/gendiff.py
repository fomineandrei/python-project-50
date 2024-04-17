#!/usr/bin/env python3


import argparse
import json
from gendiff import interface


def parse_func():
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
    for key in sorted(keys):
        diff_dict = interface.make_diff_dict(
            file1, file2, key)
        diff_key = interface.make_diff_key(file1, file2, key)
        diff_list.append(diff_dict[diff_key])
    return diff_list


def output_func(diff_data):
    for element in diff_data:
        print(element)


def main():
    output_func(generate_diff(
        parse_func().first_file, parse_func().second_file)
    )


if __name__ == '__main__':
    main()
