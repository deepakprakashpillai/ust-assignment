import csv

def read_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

def write_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
            print(f"Data written successfully to {file_path}.")

    except IOError as e:
        print(f"Error: {e}")

read_csv('sample.csv')

data_to_write = [['Name', 'Age'], ['Alice', '30'], ['Bob', '25']]
write_csv('modified_data.csv', data_to_write)
