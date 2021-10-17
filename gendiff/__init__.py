from gendiff.logic import generate
from gendiff.file_parser import file_parser
from gendiff.arg_parser import choose_formater


def generate_diff(source1, source2, name='default'):
    file1 = file_parser(source1)
    file2 = file_parser(source2)
    diff = generate(file1, file2)
    formater = choose_formater(name)
    return formater(diff)
