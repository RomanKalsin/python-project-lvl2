#!/usr/bin/env python3


from gendiff.arg_parser import arg_parser
from gendiff.logic import generate_diff
from gendiff.file_parser import file_parser
from gendiff.formaters.stylish import stylish
from gendiff.formaters.stylish2 import format


def main():
    args = arg_parser()
    file1_data = file_parser(args.first_file)
    file2_data = file_parser(args.second_file)
    diff = generate_diff(file1_data, file2_data)
    #print(format(diff))
    print(stylish(diff))
    #print(format(diff))


if __name__ == "__main__":
    main()
