import argparse
from gendiff.logic import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    format_help = 'set format of output'
    parser.add_argument('-f', '--format', default="JSON",
                        help=format_help)
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
