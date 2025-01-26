import json
import os


def split_json(fname="", output_dir="./"):
    # Read the JSON data from the file
    with open(fname, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    # Directory to save split JSON files

    os.makedirs(output_dir, exist_ok=True)

    # Loop through the list and create separate JSON files
    file_paths = []
    for data in json_data:
        file_name = f"{data['intermediate_hash']}.json"
        file_path = os.path.join(output_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        file_paths.append(file_path)

    # Provide the list of file paths for download
    file_paths


if __name__ == "__main__":
    split_json(fname="results.json", output_dir="./")
