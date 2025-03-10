import argparse
from gendiff.output_formates import OUTPUT_FORMATES


# Функция, которая парсит ввод из командной строки
# Парсит два адреса файлов и формат вывода(необязателен)
def parse_func():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format",
                        dest="FORMAT", help='set format of output',
                        choices=OUTPUT_FORMATES.keys())
    args = parser.parse_args()
    return args
