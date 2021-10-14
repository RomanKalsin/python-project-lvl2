#!/usr/bin/env python3


def stylish(data, nested_level=0):
    result = '{\n'
    spaces_beginning = '    ' * nested_level
    spaces_beginning += "  "
    sorted_keys = sorted(data)
    for key in sorted_keys:
        item = data[key]
        status_item = item[0]
        if status_item == 'children':
            result += '{}  {}: '.format(spaces_beginning, key)
            result += stylish(item[1], nested_level + 1)
            result += '\n'
        else:
            result += make_string_stylish(status_item, spaces_beginning, key, item[1])            
    result += spaces_beginning
    result += '}\n'
    return result


def make_string_stylish(status_item, spaces_beginning, key, item):
    symbol = {'added': "+", 'deleted': "-", 'value': " "}
    result = ''
    if status_item == 'updated':
        result += '{}{} {}: {}\n'.format(spaces_beginning, symbol['deleted'], key, item[0])
        result += '{}{} {}: {}\n'.format(spaces_beginning, symbol['added'], key, item[1])
        return result
    else:
        result += '{}{} {}: {}\n'.format(spaces_beginning, symbol[status_item], key, item)
        return result