import json
import sys


def read_file(filename):
    with open(filename) as json_file:
        return json_file.read()


def prettify_json(content):
    return json.dumps(
        json.loads(content),
        indent=4,
        ensure_ascii=False
    )


def get_prettify_json(filename):
    return prettify_json(read_file(filename))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            source_file = read_file(filename)
            if source_file:
                print(prettify_json(source_file))
            else:
                print("File '{0}' empty".format(filename))
        except FileNotFoundError as not_found:
            print("File '{0}' not found".format(not_found.filename))
    else:
        print(
            "Run from command line and set one parameter"
        )