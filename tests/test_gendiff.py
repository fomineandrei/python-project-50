from gendiff.diff_gen import generate_diff
from gendiff.cli import parse_func


def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == '\n'.join([
        '- follow: False', '  host: hexlet.io', '- proxy: 123.234.53.22',
        '- timeout: 50\n+ timeout: 20', '+ verbose: True',
        ])
