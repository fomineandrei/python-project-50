import argparse
from gendiff.output_formates import OUTPUT_FORMATES


def parse_func() -> object:
    """
    Parse the entered command and return parsed arguments
    as Namespace object
    """
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format",
                        help='set format of output',
                        choices=OUTPUT_FORMATES.keys(),
                        default='stylish')
    args = parser.parse_args()
    return args
