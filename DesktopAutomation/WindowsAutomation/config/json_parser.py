import json

def get_key_from_config(file,key):
    with open(file) as f:
        data = json.load(f)
        return data[key]

# print(get_key("eaton_config.json","email"))