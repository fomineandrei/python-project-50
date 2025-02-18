from gendiff.diff_gen import generate_diff
from gendiff.cli import parse_func
from gendiff.files_formates import file_to_dict
from gendiff.output_formates.stylish import stylish


__all__ = (
    'generate_diff',
    'parse_func',
    'file_to_dict',
    'stylish'
)
