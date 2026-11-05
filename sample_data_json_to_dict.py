import json

# Read the JSON file and load it into a Python dictionary
with open("sample_data.json", "r") as f:
    data = json.load(f)

# Now 'data' is an exact Python dict copy!
print(type(data))  # <class 'dict'>

# Access specific values using keys and indexes:
print("Project:", data["project"])
print("Theme:", data["settings"]["theme"])
print("First Tag:", data["tags"][0])