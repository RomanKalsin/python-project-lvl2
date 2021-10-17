#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.arg_parser import arg_parser


def main():
    args = arg_parser()
    file1_path = args.first_file
    file2_path = args.second_file
    formater = args.format
    print(generate_diff(file1_path, file2_path, formater))


if __name__ == "__main__":
    main()
