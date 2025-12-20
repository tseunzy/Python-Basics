
#  Basic functions & parameters

print('======Basic functions & parameters=========')

# Simple function without parameters
def greet():
    print("Hello, World!")

# Calling the function
greet()  

print('=====Function with Parameters==========')
# Function with one parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")   # Hello, Alice!
greet_person("Seun")     #  Hello, Seun!

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)      #  5 + 3 = 8
add_numbers(10, 20)    #  10 + 20 = 30

print('=====Function with Return Value==========')
# Use 'return' to send value back
# Function that returns a value
def multiply(x, y):
    product = x * y
    return product

# Store the returned value
result = multiply(4, 5)
print(f"4 * 5 = {result}")  # 4 * 5 = 20

# Use returned value directly
print(f"6 * 7 = {multiply(6, 7)}")  # 6 * 7 = 42

# Multiple operations
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returns a tuple

area, perimeter = calculate_rectangle(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")
# Area: 15, Perimeter: 16

print('=====Types of Parameters==========')
# Positional Parameters
# Function with positional parameters
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Positional arguments (order matters)
describe_pet("dog", "Buddy")     # I have a dog named Buddy.
describe_pet('cat', "sally")  

print('=====Keyword Arguments==========')

# Using keyword arguments (order doesn't matter)
describe_pet(pet_name="Max", animal_type="hamster")
#  I have a hamster named Max.

# Mixing positional and keyword arguments
def display_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

display_info("Alice", city="New York", age=25)
# Alice is 25 years old and lives in New York


print('=====Default Parameters==========')

# Function with default parameter values
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

greet_person("Alice")  # Hello, Alice!
greet_person()     # Hello, Guest!

# Multiple default parameters
def book_ticket(name, destination="Paris", seats=1):
    print(f"Ticket booked for {name}")
    print(f"Destination: {destination}")
    print(f"Seats: {seats}")

book_ticket("Seun")    # Uses defaults
book_ticket("Alice", "London")     # Overrides destination
book_ticket("Charlie", "Lagos", 3)          # Overrides both defaults

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))  # ['apple']
print(add_item("banana"))  # ['apple', 'banana'] 


print('=====Variable-Length Arguments (*args)==========')

# *args collects all positional arguments into a tuple
def sum_numbers(*args):
    print(f"Args received: {args}")
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))   
print(sum_numbers(10, 20, 30, 40))   # Args receive (10, 20, 30, 40), Result: 100

# Mixing with regular parameters
def make_pizza(size, *toppings):
    print(f"Making a {size} pizza with:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("large", "pepperoni", "mushrooms", "cheese")


print('=====Keyword Variable-Length Arguments (kwargs)**==========')

# **kwargs collects all keyword arguments into a dictionary
def build_profile(**kwargs):
    print("User Profile:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

build_profile(name="Alice", age=25, city="New York")
# name: Alice
# age: 25
# city: New York

# Mixing all parameter types
def create_order(order_id, *items, **details):
    print(f"Order #{order_id}")
    print("Items:", items)
    print("Details:", details)

create_order(101, "book", "pen", "notebook", 
            priority="high", discount=10)


print('=====Function Scope==========')
# Local vs Global Variables

# Global variable
global_var = "I'm global"

def demonstrate_scope():
    # Local variable
    global global_var
    local_var = "I'm local"
    print("Inside function:")
    print(f"Local variable: {local_var}")
    print(f"Global variable: {global_var}")
    
    # Modifying global variable requires global keyword
    
    global_var = "Modified global"

# Before function call
print("Before function:")
print(f"Global variable: {global_var}")

# Call function
demonstrate_scope()

# After function call
print("\nAfter function:")
print(f"Global variable: {global_var}")
# print(local_var) # local_var is not defined outside function

# Variable shadowing
value = 10

def show_value():
    global value
    value = 20  # This creates a new local variable
    print(f"local value: {value}")
    value = 30

show_value()    # local value: 20
print(f"Global value: {value}")  #global value: 10


print('=====Enclosing Scope==========')

def outer_function():
    outer_var = "Outer"
    
    def inner_function():
        inner_var = "Inner"
        # Can access outer_var
        print(f"Inner: {inner_var}")
        print(f"Can see outer: {outer_var}")
    
    inner_function()
    # print(inner_var)  # inner_var is not accessible here

outer_function()

print('=========Lambda Functions==========')

# Simple lambda functions
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Lambda with one parameter
square = lambda x: x ** 2
print(square(4))  # 16

# Lambda with no parameters
greet = lambda: "Hello, World!"
print(greet())    # Hello, World!

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

print('=========ORDER RULES==========')
# PARAMETER ORDER RULES:

def func(a, b, *args, c=10, d=20, **kwargs):
    pass