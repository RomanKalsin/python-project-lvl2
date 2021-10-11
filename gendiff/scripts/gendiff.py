import argparse
import json    


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default="JSON", help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
    print(__file__)
    


def generate_diff(file1_path, file2_path):
    #/mnt/c/python/code/python-project-lvl2/file/file1.json
    #C:\Python\Code\python-project-lvl2\\file\\file1.json
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
                result += '    {}: {}\n'.format(key, file1[key])
            else:
                result += '  - {}: {}\n'.format(key, file1[key])
                result += '  + {}: {}\n'.format(key, file2[key])
        elif key in set_only_file1:
            result += '  - {}: {}\n'.format(key, file1[key])
        elif key in set_only_file2:
            result += '  + {}: {}\n'.format(key, file2[key])
    result += '}'
    return result


if __name__ == "__main__":
    main()
