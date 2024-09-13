import chardet


import json
import os


def create_pretraining_set(directory_path, json_file):
    # Initialize a variable to store the combined text of all files
    combined_text = ""
    # Walk through all directories and files in the directory
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Read the contents of the file
            try:
                # First, detect the file encoding
                with open(file_path, 'rb') as raw_file:
                    raw_data = raw_file.read()
                    result = chardet.detect(raw_data)
                    file_encoding = result['encoding']

                # Now read the file with the detected encoding
                with open(file_path, "r", encoding=file_encoding) as file:
                    file_contents = file.read()
                # Append the file contents to the combined text, with a separator
                if combined_text:
                    combined_text += "\n\n---NEW FILE---\n\n"
                combined_text += file_contents
                print(f"Successfully read file: {file_path}")
            except UnicodeDecodeError as e:
                print(f"Error reading file {file_path}: {e}. Skipping.")
                continue  # Skip this file and continue with the next one
            except IOError as e:
                print(f"IOError reading file {file_path}: {e}. Skipping.")
                continue  # Skip this file and continue with the next one

    # Create a dictionary with the combined text
    data = {"text": combined_text}

    try:
        with open(json_file, "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
        print("JSON file saved successfully.")
    except IOError as e:
        print(f"Error saving JSON file: {e}")