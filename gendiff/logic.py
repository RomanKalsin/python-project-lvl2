#!/usr/bin/env python3


def generate_diff(file1, file2):
    # for linux /mnt/c/python/code/python-project-lvl2/file/file1.json
    # for windows C:\Python\Code\python-project-lvl2\\file\\file1.json
    result = {}
    ADD, DEL, UPDATE = 'added', 'deleted', 'updated'
    VAL, CHILD = 'value', 'children'
    set_file1 = set(file1.keys())
    set_file2 = set(file2.keys())
    set_crossing = set_file1 & set_file2
    set_only_file1 = set_file1 - set_file2
    set_only_file2 = set_file2 - set_file1
    for key in set_crossing:
        first_item = file1[key]
        second_item = file2[key]
        if first_item == second_item:
            result[key] = (VAL, first_item)
        else:
            if type(first_item) == dict and type(second_item) == dict:
                result[key] = (CHILD, generate_diff(first_item, second_item))
            else:
                result[key] = (UPDATE, (first_item, second_item))
    for key in set_only_file1:
        first_item = file1[key]
        result[key] = (DEL, first_item)
    for key in set_only_file2:
        second_item = file2[key]
        result[key] = (ADD, second_item)
    return result
