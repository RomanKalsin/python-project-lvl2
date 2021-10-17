#!/usr/bin/env python3
"""Tests."""
from gendiff.scripts.gendiff import generate_diff
from gendiff.file_parser import file_parser
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain


def extract_exp_value(path):
    """Extract expected value which is store in txt file.
    Args:
        path (str): The path to file where expected value is store.
    Returns:
        (str): Expected value.
    """
    with open(path) as expected_txt_diff:
        return expected_txt_diff.read()


def test_json_diff():
    first_path = file_parser('tests/fixtures/json/file1.json')
    second_path = file_parser('tests/fixtures/json/file2.json')
    ansver = extract_exp_value('tests/fixtures/ansvers/exp_json_diff.txt')
    diff = generate_diff(first_path, second_path)
    assert stylish(diff) == ansver


def test_yaml_diff():
    first_path = file_parser('tests/fixtures/yaml/file1.yaml')
    second_path = file_parser('tests/fixtures/yaml/file2.yml')
    ansver = extract_exp_value('tests/fixtures/ansvers/exp_json_diff.txt')
    diff = generate_diff(first_path, second_path)
    assert stylish(diff) == ansver


def test_json_diff_nested():
    first_path = file_parser('tests/fixtures/json/file3.json')
    second_path = file_parser('tests/fixtures/json/file4.json')
    ansver = extract_exp_value('tests/fixtures/ansvers/exp_json_diff_nested.txt')
    diff = generate_diff(first_path, second_path)
    assert stylish(diff) == ansver


def test_yaml_diff_nested():
    first_path = file_parser('tests/fixtures/yaml/file3.yaml')
    second_path = file_parser('tests/fixtures/yaml/file4.yaml')
    ansver = extract_exp_value('tests/fixtures/ansvers/exp_json_diff_nested.txt')
    diff = generate_diff(first_path, second_path)
    assert stylish(diff) == ansver


def test_diff_plain():
    first_path = file_parser('tests/fixtures/json/file3.json')
    second_path = file_parser('tests/fixtures/json/file4.json')
    ansver = extract_exp_value('tests/fixtures/ansvers/exp_plain_diff.txt')
    diff = generate_diff(first_path, second_path)
    assert plain(diff) == ansver
