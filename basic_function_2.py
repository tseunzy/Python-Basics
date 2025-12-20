
print('========Examples==========')
# Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

def calculator(operation, a, b):  # 
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        return "Invalid operation"

# Using the calculator
print(calculator("add", 10, 5))       # 15
print(calculator("divide", 10, 0))    # Error: Cannot divide by zero

print('========Examples==========')


def reverse_string(text):  # To resverse a string
    return text[::-1]

def count_vowels(text):     # To count number of vowel in a text
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def is_palindrome(text):        # To check if a text is palindrome
    # Remove spaces and convert to lowercase
    return text == text[::-1]

def format_string(text, case='lower'):  # To format text using the keyword function as default
    if case == 'upper':
        return text.upper()
    elif case == 'title':
        return text.title()
    elif case == 'lower':
        return text.lower()
    else:
        return text

# Test string functions
text = "Hello World"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")
print(f"Vowel count: {count_vowels(text)}")
print(f"Is palindrome? {is_palindrome('racecar')}")
print(f"Title case: {format_string(text, 'title')}")


print('========Examples==========')
# A function to check if a number is negative, positive or zzero 

def check_number(num):
    # Early returns for edge cases
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "Negative"

print(check_number(10))   # Positive
print(check_number(0))    # Zero
print(check_number(-5))   # Negative

print('========Examples==========')

#  Maximum of three numbers
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print('========Examples==========')

# HIGHEST NUMBER IN A LIST
def highest_num(number):

    highest = number[0]
    for num in number:
        if num > highest:
            highest = num
    return highest

print('========Examples==========')

#  Calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print('========Examples==========')

#sorting in ascending order
def sort_asc(nums):

    sortLow = [float('inf')] * len(nums)

    for num in nums:
        for i in range(len(nums)):
            if num < sortLow[i]:
                sortLow.insert(i, num)
                sortLow.pop()
                break
    return sortLow

print('========Examples==========')

# Generate multiplication table
def multiplication_table(n, limit=10):
    table = []
    for i in range(1, limit + 1):
        table.append(f"{n} × {i} = {n * i}")
    return table

print('========Examples==========')

#Write a function that removes duplicates from a list4 
def remove_dup(list):
    new = []
    for num in list:
        if num not in new:
            new.append(num)    
    return new  #return list(set(items))


print('========Examples==========')
# Given a dictionary of people and their ages, group them by age range
# Age ranges: Child (0-12), Teen (13-19), Adult (20-64), Senior (65+)

def group_by_age(data):

    result = {}
    for people, age in data.items():
        if age <= 12:
            category = 'Child'
        elif age <= 19:
            category = 'Teen'
        elif age <= 64:
            category = 'Adult'
        else:
            category = 'Senior'

        if category not in result:
            result[category] = []
        result[category].append(people)
    return result


people_ages = {
    'Alice': 25,
    'Bob': 13,
    'Charlie': 8,
    'Diana': 70,
    'Eve': 15,
    'Frank': 45,
    'Grace': 10,
    'Henry': 32
}

result = group_by_age(people_ages)