print('=========Variables container==========')

age = 25  # Integer type
temperature = -5
print(f"Age: {age}, Type: {type(age)}")

print('===================')

price = 99.99  # Floating point type
pi = 3.14159
print(f"Price: ${price}, Type: {type(price)}")

print('===================')

name = "Alice"  # String type
greeting = 'Hello, World!'
print(f"Name: {name}, Type: {type(name)}")



print('\n=========Basic Input Prompt==========')

# Getting user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Welcome to the program.")

print('===================')

# Converting input to different data types
age_input = input("Enter your age: ")
age = int(age_input)  # Convert string to integer
height_input = input("Enter your height in meters: ")
height = float(height_input)  # Convert string to float
print(f"In 5 years, you'll be {age + 5} years old") # Concatenate two strings

print('===================')

# Getting multiple values at once
user_data = input("Enter name, age, and city (separated by commas): ")
name, age, city = user_data.split(",")
print(f"Name: {name.strip()}, Age: {age.strip()}, City: {city.strip()}")