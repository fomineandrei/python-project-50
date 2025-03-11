from gendiff.diff_gen import generate_diff


def test_generate_diff_simple():
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == '\n'.join([
                             '{', '  - follow: false', '    host: hexlet.io',
                             '  - proxy: 123.234.53.22',
                             '  - timeout: 50\n  + timeout: 20',
                             '  + verbose: true', '}'])


def test_generate_diff_stylish():
    with open('tests/fixtures/diff_stylish.txt', 'r') as f:
        assert generate_diff('tests/fixtures/file3.json',
                             'tests/fixtures/file4.yaml') == f.read()


def test_generate_diff_plane():
    with open('tests/fixtures/diff_plane.txt', 'r') as f:
        assert generate_diff('tests/fixtures/file3.json',
                             'tests/fixtures/file4.yaml',
                             formate='plain') == f.read()


def test_generate_diff_json():
    with open('tests/fixtures/diff_json.txt', 'r') as f:
        assert generate_diff('tests/fixtures/file3.json',
                             'tests/fixtures/file4.yaml',
                             formate='json') == f.read()
