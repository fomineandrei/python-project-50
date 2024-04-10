#!/usr/bin/env python3


import argparse

def help_func():
    parser = argparse.ArgumentParser(prog="gendiff", description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return args.first_file, args.second_file


def main():
    help_func()


if __name__ == '__main__':
    main()
