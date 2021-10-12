import json

def type_conversion(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    elif val is None:
        return 'null'
    else:
        return val


def generate_diff(file1_path, file2_path):
    # for linux /mnt/c/python/code/python-project-lvl2/file/file1.json
    # for windows C:\Python\Code\python-project-lvl2\\file\\file1.json
    result = "{\n"
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
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