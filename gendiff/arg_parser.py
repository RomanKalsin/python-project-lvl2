import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    format_help = 'set format of output'
    parser.add_argument('-f', '--format', default="JSON",
                        help=format_help)
    return parser.parse_args()
