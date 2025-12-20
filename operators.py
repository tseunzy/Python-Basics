print('=======Basic arithmetic========')
# Basic arithmetic operations
x = 15
y = 4

print("Arithmetic Operations:")
print(f"Addition (x + y): {x} + {y} = {x + y}")
print(f"Subtraction (x - y): {x} - {y} = {x - y}")
print(f"Multiplication (x * y): {x} × {y} = {x * y}")
print(f"Division (x / y): {x} ÷ {y} = {x / y}")
print(f"Floor Division (x // y): {x} // {y} = {x // y}")
print(f"Modulus (x % y): {x} % {y} = {x % y}")
print(f"Exponentiation (x ** y): {x}^{y} = {x ** y}")


print('=======Comparison Operators========')
# Comparing values
a = 10
b = 20
c = 10

print("\nComparison Operations:")
print(f"Equal (a == c): {a} == {c} → {a == c}")
print(f"Not Equal (a != b): {a} != {b} → {a != b}")
print(f"Greater Than (b > a): {b} > {a} → {b > a}")
print(f"Less Than (a < b): {a} < {b} → {a < b}")
print(f"Greater or Equal (a >= c): {a} >= {c} → {a >= c}")
print(f"Less or Equal (a <= b): {a} <= {b} → {a <= b}")

# String comparison
name1 = "Alice"
name2 = "Bob"
print(f"\nString comparison: '{name1}' == '{name2}' → {name1 == name2}")
print(f"String comparison: '{name1}' < '{name2}' → {name1 < name2}")


print('=======Logical Operators========')
# Logical operations
is_student = True
has_permission = False
age = 18
grade = 85

print("\nLogical Operations:")
print(f"AND (is_student AND age >= 18): {is_student} AND {age >= 18} → {is_student and age >= 18}")
print(f"OR (has_permission OR grade > 80): {has_permission} OR {grade > 80} → {has_permission or grade > 80}")
print(f"NOT (NOT has_permission): NOT {has_permission} → {not has_permission}")

# Complex logical expression
can_enter = (age >= 18) and (has_permission or grade > 80)
print(f"\nComplex condition: (age >= 18) AND (has_permission OR grade > 80)")
print(f"can_enter = {can_enter}")


print('=======Boolean Variable========')

is_student = True  # Boolean type
has_permission = False
print(f"Is student? {is_student}, Type: {type(is_student)}")


print('=======Basic precedence========')
# P: Parentheses
# E: Exponents
# MD: Multiplication and Division (left to right)
# AS: Addition and Subtraction (left to right)

# Then remember:
# Comparisons (>, <, ==, etc.)
# not
# and
# or