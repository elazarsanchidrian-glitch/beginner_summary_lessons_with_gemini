from datetime import datetime
import os
import pandas as pd

file_name = "my_database.xlsx"

# 1. Load existing file or create a new one
if os.path.exists(file_name):
    df = pd.read_excel(file_name)
    print("Loaded existing database file.")
else:
    columns = ["id", "first_name", "last_name", "email", "status", "created_at"]
    df = pd.DataFrame(columns=columns)
    print("Created a brand new database file.")

# 2. Ask you to type a name in the PyCharm console at the bottom
print("\n--- Add a New Person ---")
first = input("Enter First Name: ")
last = input("Enter Last Name: ")

# 3. Create the new record using what you typed
new_record = {
    "id": len(df) + 1,
    "first_name": first,
    "last_name": last,
    "email": f"{first.lower()}.{last.lower()}@example.com",
    "status": "Active",
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

# 4. Add and save
df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
df.to_excel(file_name, index=False)

print(f"\nSuccessfully added {first} {last} to '{file_name}'!")
print(df)