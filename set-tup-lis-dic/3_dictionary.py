
# Dictionaries (Key-Value Pairs, Unordered, Mutable, Unique Keys)

print('======Creating Dictionaries========')
# Different ways to create dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
mixed = {1: "one", "two": 2, 3.0: "three"}

# Using dict() constructor
dict_from_list = dict([("a", 1), ("b", 2), ("c", 3)])
dict_from_kwargs = dict(name="Bob", age=25, city="LA")

print("Dictionary Creation:")
print(f"person: {person}")
print(f"dict_from_list: {dict_from_list}")
print(f"dict_from_kwargs: {dict_from_kwargs}")


print('======Dictionary Operations========')
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Physics"],
    "grades": {"Math": 90, "Physics": 85}
}

# Accessing elements
print("Dictionary Access:")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"Grade (default if not found): {student.get('grade', 'Not availa')}")

# Modifying dictionaries
student["age"] = 21                          # Update existing
student["email"] = "john@example.com"        # Add new key
student.update({"age": 22, "phone": "123-456"})  # Update multiple
print(f"\nAfter updates: {student}")

# Removing elements
email = student.pop("email")                  # Remove and return
print(f"Removed email: {email}")

# Dictionary methods
print(f"\nDictionary Methods:")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")
print(f"Length: {len(student)}")

# Checking existence
print(f"'name' in student: {'name' in student}")
print(f"'email' not in student: {'email' not in student}")


print('======Dictionary Comprehensions========')

# Basic dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(f"Swapped: {swapped}")

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2                      
print(f"Merged: {merged}")                  # {'a': 1, 'b': 3, 'c': 4}

