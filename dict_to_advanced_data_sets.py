import pandas as pd
import sqlite3
import json



names = ["John", "Alice", "Bob", "Eve", "Charlie"]
dates_of_birth = ["1990-01-15", "1985-07-30", "1992-03-22", "1988-11-05", "1995-06-12"]
user_ids = ["1", "2", "3", "4", "5"]  # Changed 'id' to 'user_ids' to avoid built-in conflicts
emails = ["john@example.com", "alice@example.com", "bob@example.com", "eve@example.com", "charlie@example.com"]
phones = ["555-0101", "555-0102", "555-0103", "555-0104", "555-0105"]

# Zip names with a dictionary of their attributes (matching 'user_ids' here)
people_dict = {
    name: {"dob": dob, "email": email, "phone": phone, "id": user_id}
    for name, dob, email, phone, user_id in zip(names, dates_of_birth, emails, phones, user_ids)
}

print(people_dict)
print("-" * 30)

# Accessing specific details
print(people_dict["Alice"]["dob"])   # Output: 1985-07-30
print(people_dict["Charlie"]["email"]) # Output: charlie@example.com
print(people_dict["Bob"]["phone"]) # Output: 555-0103
print(people_dict["John"]["id"]) # Output: 1

print("-" * 30)

# Printing them all nicely
for name, details in people_dict.items():
    print(f"👤 Name: {name}")
    print(f"   📅 DOB:   {details['dob']}")
    print(f"   📧 Email: {details['email']}")
    print(f"   📞 Phone: {details['phone']}")
    print(f"   🔢 ID: {details['id']}")
    print("-" * 30)  # Fixed the divider line



# Convert nested dictionary into a DataFrame (keys become rows)
df = pd.DataFrame.from_dict(people_dict, orient="index")

# Turn the dictionary key ("John", "Alice", etc.) into a regular column
df.index.name = "name"
df.reset_index(inplace=True)

# Reorder columns logically
df = df[["id", "name", "dob", "email", "phone"]]

print(df)

# Save as CSV file
df.to_csv("people_data.csv", index=False)

# Save as Excel file
df.to_excel("people_data.xlsx", index=False)

# Connect to a local SQLite database file (creates it if it doesn't exist)
conn = sqlite3.connect("people.db")

# Save DataFrame as a SQL table named 'users'
df.to_sql("users", conn, if_exists="replace", index=False)

# Test query to verify
cursor = conn.cursor()
cursor.execute("SELECT name, email FROM users WHERE id > 2")
print(cursor.fetchall())  # Output: [('Bob', 'bob@example.com'), ...]

conn.close()


with open("people_data.json", "w") as f:
    json.dump(people_dict, f, indent=4)