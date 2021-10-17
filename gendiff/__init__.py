from gendiff.logic import generate


def generate_diff(source1, source2, name):
    diff = generate(source1, source2)
    return name(diff)
