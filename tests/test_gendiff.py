#!/usr/bin/env python3
"""Tests."""
from gendiff.scripts.gendiff import generate_diff


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
    first_path = 'tests/fixtures/json/file1.json'
    second_path = 'tests/fixtures/json/file2.json'
    ansver = extract_exp_value('tests/fixtures/ansvers/exp_json_diff.txt')
    assert generate_diff(first_path, second_path) == ansver
    #assert generate_diff('tests/fixtures/json/file4.json', 'tests/fixtures/json/file4.json') == "{\n}"


def test_yaml_diff():
    first_path = 'tests/fixtures/yaml/file1.yaml'
    second_path = 'tests/fixtures/yaml/file2.yml'
    ansver = extract_exp_value('tests/fixtures/ansvers/exp_json_diff.txt')
    assert generate_diff(first_path, second_path) == ansver
    #assert generate_diff('tests/fixtures/yaml/file4.yml', 'tests/fixtures/yaml/file4.yml') == "{\n}"