from gendiff.diff_gen import generate_diff
from gendiff.cli import parse_func
from gendiff.files_formates import json_to_dict, yaml_to_dict


def test_generate_diff_():
    json_file_to_dict = json_to_dict('tests/fixtures/file1.json')
    yaml_file_to_dict = yaml_to_dict('tests/fixtures/file2.yaml')
    assert generate_diff(json_file_to_dict, yaml_file_to_dict) == '\n'.join([
        '- follow: False', '  host: hexlet.io', '- proxy: 123.234.53.22',
        '- timeout: 50\n+ timeout: 20', '+ verbose: True',
        ])
