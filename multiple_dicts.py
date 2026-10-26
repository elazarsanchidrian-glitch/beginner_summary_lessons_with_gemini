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