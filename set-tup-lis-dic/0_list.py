
print('======Creating Lists========')

# Different ways to create lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# Using list() constructor
list_from_string = list("Python")
list_from_range = list(range(5))

print("List Creation:")
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"list('Python'): {list_from_string}")
print(f"list(range(5)): {list_from_range}")


print('=======List Operations========')

fruits = ["apple", "banana", "cherry"]

# Accessing elements
print("\nList Access:")
print(f"fruits[0]: {fruits[0]}")          # apple
print(f"fruits[-1]: {fruits[-1]}")        # cherry
print(f"fruits[1:3]: {fruits[1:3]}")      # ['banana', 'cherry']

# Modifying lists
fruits[1] = "blueberry"
print(f"After modification: {fruits}")    # ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("orange")                    # Add to end
fruits.insert(1, "mango")                  # Insert at index
fruits.extend(["grape", "kiwi"])           # Add multiple
print(f"After adding: {fruits}")

# Removing elements
removed = fruits.pop()                     # Remove last
print(f"Popped: {removed}")
removed = fruits.pop(2)                    # Remove at index
print(f"Popped at index 2: {removed}")
# fruits.remove("blueberry")                 # Remove by value
print(f"After removal: {fruits}")

# List methods
print(f"\nList Methods:")
print(f"Length: {len(fruits)}")
print(f"Count 'apple': {fruits.count('apple')}")
print(f"Index of 'mango': {fruits.index('mango')}")

# Sorting
numbers = [5, 2, 8, 1, 9]
numbers.sort()                            # In-place sort
print(f"Sorted numbers: {numbers}")
numbers.sort(reverse=True)                # Descending
print(f"Reverse sorted: {numbers}")

# Sorted function (returns new list)
unsorted = [3, 1, 4, 1, 5]
sorted_list = sorted(unsorted)            # Creates new list
print(f"Original: {unsorted}, Sorted: {sorted_list}")


print('======List Comprehensions========')
# Basic list comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Flattening a matrix
flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")


