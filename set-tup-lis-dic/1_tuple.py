
# Tuples (Ordered, Immutable, Allows Duplicates)

print('======Creating Tuples========')
# Different ways to create tuples
empty_tuple = ()
single_item = (42,)                      # Note the comma!
coordinates = (10, 20)
mixed = (1, "Hello", 3.14, True)
nested = ((1, 2), (3, 4))

# Without parentheses (tuple packing)
point = 10, 20, 30
print(f"Tuple packing: {point}")

# Tuple unpacking
x, y, z = point
print(f"Unpacked: x={x}, y={y}, z={z}")

# Swapping variables
a, b = 5, 10
a, b = b, a                              # Tuple unpacking swap
print(f"Swapped: a={a}, b={b}")

print('======Tuple Operations========')
colors = ("red", "green", "blue", "red")

# Accessing elements
print("\nTuple Access:")
print(f"colors[0]: {colors[0]}")         # red
print(f"colors[-1]: {colors[-1]}")       # red
print(f"colors[1:3]: {colors[1:3]}")     # ('green', 'blue')

# Tuple methods
print(f"Count of 'red': {colors.count('red')}")
print(f"Index of 'green': {colors.index('green')}")

# Concatenation to add into a tuple
more_colors = colors + ("yellow", "purple") 
print(f"Concatenated: {more_colors}")

# Repetition
repeated = colors * 2
print(f"Repeated: {repeated}")


