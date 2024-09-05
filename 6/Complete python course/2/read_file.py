def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Contents of {file_path}:")
            print(content)

    except FileNotFoundError as e:
        print(f"Error: {e}")

read_file('source.txt')
