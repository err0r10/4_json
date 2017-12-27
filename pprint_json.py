import json
import sys


def load_data(filepath):
    try:
        f = open(filepath)
        return f.read()
    except FileNotFoundError:
        print('File not found')


def pretty_print_json(data):
    return json.dumps(json.loads(data), indent=4)


if len(sys.argv) == 2:
    data = load_data(sys.argv[1])
    if data:
        print(pretty_print_json(data))

else:
    print('Run from command line and set one parameter, example: python pprint_json.py 4.json')
    sys.exit(1)


if __name__ == '__main__':
    pass
    #data = load_data('4.json')
    #print(pretty_print_json(data))
