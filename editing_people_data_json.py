import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
json_file_path = BASE_DIR / "people_data.json"

# 1. Load the existing data into memory
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 2. Edit or add a new person in memory
# Let's add a new person named "Sarah"
data["Sarah"] = {
    "dob": "1998-04-20",
    "email": "sarah@example.com",
    "phone": "555-0106",
    "id": "6",
}

# 3. Save (write) the updated dictionary BACK to the JSON file!
with open(json_file_path, "w", encoding="utf-8") as file:
    # indent=4 makes the JSON look neat and readable instead of squished together
    json.dump(data, file, indent=4)

print("Successfully added Sarah and updated people_data.json!")

# 4. Convert the dictionary back to a pretty JSON string and print it!
updated_json_string = json.dumps(data, indent=4)
print("Newly updated JSON:")
print(updated_json_string)