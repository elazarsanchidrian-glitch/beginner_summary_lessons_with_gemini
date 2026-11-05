import json

# Your raw JSON text as a string
raw_json_text = '''
{
    "project": "Random JSON Generator",
    "active": true,
    "max_users": 500
}
'''

# Convert the text string into a Python dict
my_dict = json.loads(raw_json_text)

print(type(my_dict))  # Output: <class 'dict'>
print(my_dict["project"])  # Output: Random JSON Generator