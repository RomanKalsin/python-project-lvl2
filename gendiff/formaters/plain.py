#!/usr/bin/env python3


def plain(data, path=''):
    result = ''
    sotr_key = sorted(data)
    for key in sotr_key:
        status = get_status(data, key)
        val = get_value(data, key)
        if status == 'children':
            result += plain(val, path=(path + key + '.'))
            result += "\n"
        elif status == 'value':
            continue
        else:
            result += format_string(val, status, path=(path + key))
    return result[:-1]


def format_string(data, status, path):
    if status == 'added':
        data = "[complex value]" if isinstance(data, dict)\
            else convert_string(data)
        return "Property '{}' was added with value: {}\n".format(path, data)
    elif status == 'deleted':
        return "Property '{}' was removed\n".format(path)
    elif status == 'updated':
        val1 = "[complex value]" if isinstance(data[0], dict)\
            else convert_string(data[0])
        val2 = "[complex value]" if isinstance(data[1], dict)\
            else convert_string(data[1])
        return "Property '{}' was updated. From {} to {}\n".\
            format(path, val1, val2)
    else:
        return ''


def convert_string(val):
    type_str = ['null', 'true', 'false']
    if isinstance(val, str) and val not in type_str:
        return "'{}'".format(val)
    else:
        return val


def get_status(data, key):
    item = data[key]
    return item[0]


def get_value(data, key):
    item = data[key]
    return item[1]
