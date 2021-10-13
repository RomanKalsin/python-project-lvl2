import json
import yaml


def file_parser(file_path):
    extension = file_path.split('.')[-1]
    if extension == "yaml" or extension == "yml":
        return yaml.load(open(file_path), Loader=yaml.FullLoader)
    elif extension == "json":
        return json.load(open(file_path))
