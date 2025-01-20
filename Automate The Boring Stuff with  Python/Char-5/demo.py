# Python Dictionary Manipulation Examples

# 1. Creating a Dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 2. Accessing Values
print(data["name"])  # Output: Alice

# 3. Adding or Updating Key-Value Pairs
data["age"] = 26  # Update age
data["profession"] = "Engineer"  # Add new key-value pair
print(data)

# 4. Removing Key-Value Pairs
del data["city"]  # Remove the key 'city'
removed_value = data.pop("age")  # Remove 'age' and get its value
print(data)
print("Removed age:", removed_value)

# 5. Iterating Through a Dictionary
for key, value in data.items():
    print(f"{key}: {value}")

# 6. Checking if a Key Exists
if "name" in data:
    print("Name exists in the dictionary")

# 7. Merging Dictionaries
data2 = {"country": "USA", "hobby": "Reading"}
data.update(data2)
print(data)

# 8. Dictionary Comprehension
squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)

# 9. Clearing a Dictionary
data.clear()
print(data)  # Output: {}

# 10. Nested Dictionaries
nested_data = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_data["person1"]["name"])  # Output: Alice
