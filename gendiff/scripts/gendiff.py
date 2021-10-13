from gendiff.arg_parser import arg_parser
from gendiff.logic import generate_diff


def main():
    args = arg_parser()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
