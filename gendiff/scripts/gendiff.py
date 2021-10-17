#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.arg_parser import arg_parser, choose_formater
from gendiff.file_parser import file_parser


def main():
    args = arg_parser()
    file1_data = file_parser(args.first_file)
    file2_data = file_parser(args.second_file)
    formater = choose_formater(args.format)
    print(generate_diff(file1_data, file2_data, formater))


if __name__ == "__main__":
    main()
