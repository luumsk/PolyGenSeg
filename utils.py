import os
import json

def load_json(path):
    data = None
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def check_path(path):
    if not os.path.isfile(path):
        raise ValueError(f'File does not exist: {path}')