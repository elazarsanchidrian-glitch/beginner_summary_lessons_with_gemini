import json
import pprint

with open("sample_data.json", "r") as f:
    data = json.load(f)

# This formats it nicely with indented lines
pprint.pprint(data)