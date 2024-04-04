import json
import sys
import os

def read_and_sort_data(file_path):
    if not os.path.exists(file_path):
        sys.exit(1)  # Exit with code 1 if file not found

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == "":  # Ignore empty lines
                continue
            try:
                score, record = line.split(': ', 1)
                score = int(score)
                record_dict = json.loads(record)
                if 'id' in record_dict:
                    data.append((score, record_dict))
            except (ValueError, json.JSONDecodeError):
                sys.exit(2)  # Exit with code 2 if invalid input
    # Sort the data by score in descending order
    data.sort(key=lambda x: x[0], reverse=True)
    return data

def get_top_n_records(data, n):
    return [record for _, record in data[:n]]

def main():
    if len(sys.argv) != 3:
        print("Usage: python highest.py <file_path> <number_of_records>")
        sys.exit(1)

    file_path = sys.argv[1]
    n = int(sys.argv[2])

    data = read_and_sort_data(file_path)
    top_n_records = get_top_n_records(data, n)

    # Output the top N records to stdout as well-formed JSON
    print(json.dumps(top_n_records, indent=4))

    sys.exit(0)  # Exit with code 0 upon successful running

if __name__ == "__main__":
    main()
