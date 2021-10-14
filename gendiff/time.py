
from gendiff.file_parser import file_parser


def generate_diff(file1_path, file2_path):
    # for linux /mnt/c/python/code/python-project-lvl2/file/file1.json
    # for windows C:\Python\Code\python-project-lvl2\\file\\file1.json
    result = "{\n"
    file1 = file_parser(file1_path)
    file2 = file_parser(file2_path)
    set_file1 = set(file1.keys())
    set_file2 = set(file2.keys())
    set_crossing = set_file1 & set_file2
    set_only_file1 = set_file1 - set_file2
    set_only_file2 = set_file2 - set_file1
    final_key_order = sorted(set_file1 | set_file2)
    for key in final_key_order:
        if key in set_crossing:
            if file1[key] == file2[key]:
                file1[key] = type_conversion(file1[key])
                result += '    {}: {}\n'.format(key, file1[key])
            else:
                file1[key] = type_conversion(file1[key])
                file2[key] = type_conversion(file2[key])
                result += '  - {}: {}\n'.format(key, file1[key])
                result += '  + {}: {}\n'.format(key, file2[key])
        elif key in set_only_file1:
            file1[key] = type_conversion(file1[key])
            result += '  - {}: {}\n'.format(key, file1[key])
        elif key in set_only_file2:
            file2[key] = type_conversion(file2[key])
            result += '  + {}: {}\n'.format(key, file2[key])
    result += '}'
    return result


def type_conversion(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    elif val is None:
        return 'null'
    else:
        return val



            result += '{}  {}: {}\n'.format(spaces_beginning ,key, item[1])
        elif status_item == 'added':
            result += '{}+ {}: {}\n'.format(spaces_beginning, key, item[1])
        elif status_item == 'deleted':
            result += '{}- {}: {}\n'.format(spaces_beginning, key, item[1])
        elif status_item == 'updated':
            result += '{}- {}: {}\n'.format(spaces_beginning, key, item[1][0])
            result += '{}+ {}: {}\n'.format(spaces_beginning, key, item[1][1])



def stylish(data, nested_level=0):
    result = '{'
    spaces_beginning = '    ' * nested_level
    spaces_beginning += "  "
    sorted_keys = sorted(data)
    for key in sorted_keys:
        item = data[key]
        status_item = item[0]
        if status_item == 'children':
            result += '{}  {}: '.format(spaces_beginning, key)
            result += stylish(item[1], nested_level + 1)
            result += ''
        else:
            result += make_string_stylish(status_item, spaces_beginning, key, item[1])            
    result += spaces_beginning
    result += '}'
    return result


def make_string_stylish(status_item, spaces_beginning, key, item):
    symbol = {'added': "+", 'deleted': "-", 'value': " "}
    result = ''
    if status_item == 'updated':
        result += '{}{} {}: {}'.format(spaces_beginning, symbol['deleted'], key, item[0])
        result += '{}{} {}: {}'.format(spaces_beginning, symbol['added'], key, item[1])
        return result
    else:
        result += '{}{} {}: {}'.format(spaces_beginning, symbol[status_item], key, item)
        return result