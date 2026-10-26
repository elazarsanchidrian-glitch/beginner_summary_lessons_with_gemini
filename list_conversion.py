names = ["John", "Alice", "Bob", "Eve", "Charlie"]
dates_of_birth = ["1990-01-15", "1985-07-30", "1992-03-22", "1988-11-05", "1995-06-12"]
emails = ["john@example.com", "alice@example.com", "bob@example.com", "eve@example.com", "charlie@example.com"]

# Convert the lists into a dictionary
people_dict = dict(zip(names, dates_of_birth))
print(people_dict)

# Accessing a specific
print(people_dict["Alice"])   # Output: 1985-07-30
print(people_dict["Charlie"])  # Output: 1995-06-12