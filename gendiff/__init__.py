from gendiff.logic import generate
from gendiff.file_parser import file_parser


def generate_diff(source1, source2, name='default'):
    file1 = file_parser(source1)
    file2 = file_parser(source2)
    diff = generate(file1, file2)
    return name(diff)
