import json
import sys


def read_file(filename):
    with open(filename) as target_file:
        return target_file.read()


def prettify(content):
    return json.dumps(
        json.loads(content),
        indent=4,
        ensure_ascii=False
    )


def print_json(filename):
    try:
        source_file = read_file(filename)
        if source_file:
            print(prettify(source_file))
        else:
            print("File '{0}' empty".format(filename))
    except FileNotFoundError as not_found:
        print("File '{0}' not found".format(not_found.filename))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print_json(sys.argv[1])
    else:
        print(
            "Run from command line and set one parameter, "
            "example: python pprint_json.py test.json"
        )