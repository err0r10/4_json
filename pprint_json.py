import json
import sys
from os.path import isfile


def read_file(path_file):
    with open(path_file) as desc:
        return desc.read()


def check_data(content):
    return 1 if len(content) else None


def prettify(content):
    return json.dumps(json.loads(content), indent=4,  ensure_ascii=False)


def print_json(path_file):
    if isfile(path_file):
        content_json = read_file(path_file)
        if check_data(content_json):
            return prettify(content_json)
        else:
            return 'File is empty'
    else:
        return 'File not found'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(print_json(sys.argv[1]))
    else:
        print('Run from command line and set one parameter, example: python pprint_json.py test.json')
