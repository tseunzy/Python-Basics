# Sets (Unordered, Mutable, No Duplicates)

print('======Creating Sets========')

# Different ways to create sets
empty_set = set()                        # NOT {} - that's a dict!
numbers = {1, 2, 3, 4, 5}
mixed = {1, "Hello", 3.14}

# From list (removes duplicates)
colors = ["red", "green", "blue", "red", "green"]
unique_colors = set(colors)
print(f"Unique colors: {unique_colors}")  # {'blue', 'green', 'red'}


print('======Set Operations========')

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set Operations:")
print(f"A: {A}")
print(f"B: {B}")

# Basic operations
print(f"Union: {A | B}")                # {1, 2, 3, 4, 5, 6, 7, 8}
print(f"Intersection: {A & B}")         # {4, 5}
print(f"Difference (A - B): {A - B}")   # {1, 2, 3}
print(f"Difference (B - A): {B - A}")   # {6, 7, 8}
print(f"Symmetric Difference: {A ^ B}") # {1, 2, 3, 6, 7, 8}

# Set methods
print(f"\nSet Methods:")
A.add(6)
print(f"After add(6): {A}")
A.update([7, 8, 9])
print(f"After update: {A}")
A.remove(9)                             # Raises KeyError if not found
A.discard(10)                           # No error if not found
print(f"After remove/discard: {A}")
popped = A.pop()                        # Removes arbitrary element
print(f"Popped: {popped}")

# Set comparisons
C = {1, 2, 3}
print(f"\nC: {C}")
print(f"C is subset of A: {C.issubset(A)}")
print(f"A is superset of C: {A.issuperset(C)}")
print(f"A and C are disjoint: {A.isdisjoint(C)}")


print('======Set Operations========')

# Set comprehension
squares_set = {x**2 for x in range(10)}
print(f"Squares set: {squares_set}")

# Remove vowels from string
text = "Python Programming"
consonants = {char for char in text.lower() if char not in 'aeiou '}
print(f"Consonants: {consonants}")
