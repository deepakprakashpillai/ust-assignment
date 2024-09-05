def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()

        with open(destination, 'w') as dest_file:
            dest_file.write(content)

        print(f"File copied successfully from {source} to {destination}.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

copy_file('source.txt', 'destination.txt')
