import json
import pandas as pd

# 1. The Core Data: A list of dictionaries (looks just like JSON or rows)
users_data = [
    {
        "id": 1,
        "first_name": "Sam",
        "last_name": "Wilson",
        "email": "sam.wilson@example.com",
        "status": "Active",
    },
    {
        "id": 2,
        "first_name": "Elazar",
        "last_name": "Sanchidrian",
        "email": "elazar.sanchidrian@example.com",
        "status": "Active",
    },
]

print("--- 1. Original Dictionary Data ---")
print(users_data)


# ==========================================
# TRANSFORMATION 1: Convert to a Pandas DataFrame
# ==========================================
df = pd.DataFrame(users_data)
print("\n--- 2. Transformed into a DataFrame ---")
print(df)


# ==========================================
# TRANSFORMATION 2: Export to Excel
# ==========================================
df.to_excel("from_dictionary.xlsx", index=False)
print("\nSuccessfully transformed dictionary into an Excel file!")


# ==========================================
# TRANSFORMATION 3: Export to a JSON file
# ==========================================
# (JSON is widely used for web apps, APIs, and cloud databases)
with open("from_dictionary.json", "w") as json_file:
    json.dump(users_data, json_file, indent=4)

print("Successfully transformed dictionary into a JSON file!")