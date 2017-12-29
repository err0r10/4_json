import json
import sys
from os.path import isfile


def read_file(path_file):
    with open(path_file) as file_description:
        return file_description.read()


def check_data(json_data):
    return 1 if len(json_data) else None


def format_data(json_data):
    return json.dumps(json.loads(json_data), indent=4,  ensure_ascii=False)


def print_json(path_file):
    if isfile(path_file):
        _read_data = read_file(path_file)
        if check_data(_read_data):
            print(format_data(_read_data))
        else:
            print('File is empty')
    else:
        print('File not found')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_json(sys.argv[1])
    else:
        print('Run from command line and set one parameter, example: python pprint_json.py test.json')
