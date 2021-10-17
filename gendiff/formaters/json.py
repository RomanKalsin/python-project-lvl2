import json


def form_json(data):
    return json.dumps(data, sort_keys=True, indent=2)
