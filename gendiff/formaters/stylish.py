#!/usr/bin/env python3


def stylish(data, nested_level=0):
    result = '{\n'
    sorted_keys = sorted(data)
    for key in sorted_keys:
        item = data[key]
        status_item = item[0]
        if status_item == 'children':
            spaces_beginning = '    ' * (nested_level)
            result += '{}    {}: '.format(spaces_beginning, key)
            result += stylish(item[1], nested_level + 1)
            result += '\n'
        else:
            result += make_string_stylish(status_item, nested_level, key, item[1])         
    result += '    ' * (nested_level)
    result += '}'
    return result


def make_string_stylish(status_item, nested_level, key, item):
    symbol = {'added': "+", 'deleted': "-", 'value': " "}
    result = ''
    spaces_beginning = '    ' * nested_level
    if status_item == 'updated':
        result += '{}  {} {}: {}\n'.format(spaces_beginning, symbol['deleted'], key, dict_former(item[0], nested_level + 1))
        result += '{}  {} {}: {}\n'.format(spaces_beginning, symbol['added'], key, dict_former(item[1], nested_level + 1))
        return result
    else:
        result += '{}  {} {}: {}\n'.format(spaces_beginning, symbol[status_item], key, dict_former(item, nested_level + 1))
        return result


def dict_former(item, nested_level):
    if isinstance(item, dict):
        result = '{\n'
        keys = sorted(item.keys())
        for key in keys:
            result += '{}{}: '.format('    ' * (nested_level + 1), key)
            result += dict_former(item[key], nested_level + 1) + '\n'
        result += '    ' * nested_level
        result += '}'
        return result
    else:
        return '{}'.format(item)



