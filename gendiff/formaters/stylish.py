#!/usr/bin/env python3


def stylish(data, deep=0):
    result = '{\n'
    sorted_keys = sorted(data)
    for key in sorted_keys:
        item = data[key]
        status_item = item[0]
        if status_item == 'children':
            spaces_beginning = '    ' * (deep)
            result += '{}    {}: '.format(spaces_beginning, key)
            result += stylish(item[1], deep + 1)
            result += '\n'
        else:
            result += make_string_stylish(status_item, deep, key, item[1])
    result += '    ' * (deep)
    result += '}'
    return result


def make_string_stylish(stat, deep, key, item):
    symb = {'added': "+", 'deleted': "-", 'value': " "}
    result = ''
    spaces = '    ' * deep
    if stat == 'updated':
        value1 = dict_former(item[0], deep + 1)
        value2 = dict_former(item[1], deep + 1)
        result += '{}  {} {}: {}\n'.format(spaces, symb['deleted'], key, value1)
        result += '{}  {} {}: {}\n'.format(spaces, symb['added'], key, value2)
        return result
    else:
        value = dict_former(item, deep + 1)
        result += '{}  {} {}: {}\n'.format(spaces, symb[stat], key, value)
        return result


def dict_former(item, deep):
    if isinstance(item, dict):
        result = '{\n'
        keys = sorted(item.keys())
        for key in keys:
            result += '{}{}: '.format('    ' * (deep + 1), key)
            result += dict_former(item[key], deep + 1) + '\n'
        result += '    ' * deep
        result += '}'
        return result
    else:
        return '{}'.format(item)
