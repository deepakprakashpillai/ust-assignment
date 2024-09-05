import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
            print(f"Data loaded from {file_path}: {data}")
            return data

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error: {e}")

def save_json(file_path, data):
    try:
        with open(file_path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
            print(f"Data saved to {file_path}")

    except IOError as e:
        print(f"Error: {e}")

data = load_json('sample.json')
data['new_key'] = 'new_value' 
save_json('data_modified.json', data)
