import argparse
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain


def arg_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    format_help = 'set format of output'
    parser.add_argument('-f', '--format', default="stylish",
                        metavar='FORMAT', help=format_help)
    return parser.parse_args()


def choose_formater(name):
    if name == 'plain':
        return plain
    return stylish
