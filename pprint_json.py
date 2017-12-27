import json
import sys


def load_data(filepath):
    try:
        file_discriprion = open(filepath)
        return file_discriprion.read()
    except FileNotFoundError:
        print('File not found')


def pretty_print_json(data_json):
    return json.dumps(json.loads(data_json), indent=4)


if len(sys.argv) == 2:
    data_json = load_data(sys.argv[1])
    if data:
        print(pretty_print_json(data_json))

else:
    print('Run from command line and set one parameter, example: python pprint_json.py 4.json')
    sys.exit(1)


if __name__ == '__main__':
    pass
