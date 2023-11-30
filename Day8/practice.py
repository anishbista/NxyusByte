def parse_file_to_dict(file_name):
    data_dict = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                # Split each line by space and extract key-value pairs
                pairs = line.strip().split()
                print(type(pairs))
                print((pairs))
                # Extracting key-value pairs assuming the format: key:value key:value ...
                pairs_dict = dict(pair.split(":") for pair in pairs)
                print(pairs_dict)
                print(type(pairs_dict))
                # Update the data_dict with extracted pairs
                data_dict.update(pairs_dict)
        return data_dict
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None


file_name = "data.txt"  # Replace 'data.txt' with your file name

file_content_dict = parse_file_to_dict(file_name)
if file_content_dict is not None:
    print("File content as dictionary:")
    print(file_content_dict)
