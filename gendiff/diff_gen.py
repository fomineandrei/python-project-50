import gendiff.interface as interface
import gendiff as gd


def generate_diff(file1_dict, file2_dict):
    keys = set(file1_dict.keys()) | set(file2_dict.keys())
    diff_list = []
    for key in sorted(keys):
        diff_dict = interface.make_diff_dict(
            file1_dict, file2_dict, key)
        diff_key = interface.make_diff_key(file1_dict, file2_dict, key)
        diff_list.append(diff_dict[diff_key])
    return "{\n  " + '\n  '.join(diff_list) + "\n}"


def output_func():
    print(gd.generate_diff(
        gd.file_to_dict(gd.parse_func().first_file),
        gd.file_to_dict(gd.parse_func().second_file))
    )
