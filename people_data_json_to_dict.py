import json
from pathlib import Path

# Get the directory of the current script
BASE_DIR = Path(__file__).resolve().parent
json_file_path = BASE_DIR / "people_data.json"

# Load the JSON file into a Python dictionary
try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("Successfully loaded people_data.json!\n")
except FileNotFoundError:
    print(f"Error: Could not find the file at {json_file_path}")
    data = {}

# Example usage:
if data:
    print(f"John's email: {data['John']['email']}")
    print("-" * 30)

    print("All users:")
    for name, info in data.items():
        print(f"- {name} (ID: {info['id']}): Born on {info['dob']}")