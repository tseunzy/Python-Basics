print('\n======For loop=========')

# Basic range loop
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)
print('=====Example==========')

print("\nCounting 0 to 4:")
for i in range(5):
    print(i)
print('=====Example==========')

print("\nCounting with step:")
for i in range(0, 10, 2):
    print(i)  
print('=====Example==========')

print("\nCounting backwards:")
for i in range(5, 0, -1):
    print(i) 

print('=====Example==========')

# using the split function to calculate the number of words
sentence = "i alooking for the breath, where is it"
sum = 0
for i in sentence.split():
    sum += 1
print(f"sum: {sum}")

print('\n=====Example==========')

# Iterating through strings
word = "Python"

print("Characters in 'Python':")
for char in word:
    print(char)

print("\nWith index:")
for index, char in enumerate(word):
    print(f"Index {index}: {char}")

print('======For loop in Lists=========')

# Iterating through lists
fruits = ["apple", "banana", "cherry", "date"]

print("Fruits list:")
for fruit in fruits:
    print(f"- {fruit}")

print("\nWith index and value:")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Modifying list in loop
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(f"\nSquares: {squares}")

print('======For loop in Dictionaries=========')
# Iterating through dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

print("Dictionary keys:")
for key in student:
    print(f"Key: {key}")

print("\nDictionary values:")
for value in student.values():
    print(f"Value: {value}")

print("\nDictionary items (key-value pairs):")
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension with loop
student_lower = {}
for key, value in student.items():
    if isinstance(value, str):
        student_lower[key] = value.lower()
    else:
        student_lower[key] = value
print(f"\nLowercased strings: {student_lower}")

print('======While loop=========')


#while loop using the continue function to skip a number
i = 0
while i < 10:
    if i == 3 or i == 5:
        i += 1
        continue
    print(i, end=' ')
    i += 1

print('=====Example==========')

#using the break function to terminate the loop if found
languages = ['c##', 'python', 'c#', 'java']
i = 0
while i < len(languages):
    if languages[i] == 'c##':
        i += 1
        print('i like c##')
        break
else:
    print('coding is not my thing')

print('=====Example==========')

print("\nCountdown with else:")
count = 3
while count > 0:
    print(count)
    count -= 1
    if input("Stop? (y/n): ").lower() == 'y':
        print("Stopped early")
        break
else:
    print("Countdown completed!")

print('=====Example==========')
#from the FOR loop, the languages is already in str so it will print the str in the list
languages = ['c', 'python', 'c##', 'java']
for i in languages:
    print(i)

print('=====Example==========')
  