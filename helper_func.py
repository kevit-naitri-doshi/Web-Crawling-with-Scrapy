import os
import json

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Directory "+directory)
        os.makedirs(directory)

def write_file(path,data):
    with open(path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

