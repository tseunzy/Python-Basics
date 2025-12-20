print('=======String Creation========')

# Different ways to create strings
str1 = 'Hello, World!'  # Single quotes
str2 = "Python Programming"  # Double quotes
str3 = '''This is a 
multi-line string'''  # Triple quotes for multi-line
str4 = """Another way to
write multi-line strings"""

# String with escape sequences
str5 = "He said, \"Python is awesome!\""  # Escaping quotes
str6 = "Line 1\nLine 2\tTabbed text"  # \n for newline, \t for tab

print("String Examples:")
print(str1)
print(str3)
print(str5)
print(str6)

print('======String Indexing and Slicing========')

text = "Python Programming"

# Indexing
print("Indexing Examples:")
print(f"text[0]: {text[0]}")      # First character: 'P'
print(f"text[7]: {text[7]}")      # 'P' in Programming
print(f"text[-1]: {text[-1]}")    # Last character: 'g'
print(f"text[-3]: {text[-3]}")    # Third from last: 'i'

# Slicing [start:end:step]
print("\nSlicing Examples:")
print(f"text[0:6]: '{text[0:6]}'")       # 'Python'
print(f"text[7:]: '{text[7:]}'")         # 'Programming'
print(f"text[:6]: '{text[:6]}'")         # 'Python'
print(f"text[::2]: '{text[::2]}'")       # Every 2nd char: 'Pto rgamn'
print(f"text[::-1]: '{text[::-1]}'")     # Reverse: 'gnimmargorP nohtyP'
print(f"text[-5:-2]: '{text[-5:-2]}'")   # 'mmin'


print('======Case Conversion Methods========')
name = "Timothy seun"

print("Case Conversion:")
print(f"Original: '{name}'")
print(f"Upper: '{name.upper()}'")          # JOHN DOE TIMOTHY SEUN
print(f"Lower: '{name.lower()}'")          # john doe timothy seun
print(f"Title: '{name.title()}'")          # John Doe Timothy Seun
print(f"Capitalize: '{name.capitalize()}'") # John doe   Timothy seun


print('======Searching and Checking========')

sentence = "Python is powerful and Python is easy"

print("\nSearching Methods:")
print(f"Starts with 'Py': {sentence.startswith('Py')}")  # True
print(f"Ends with 'easy': {sentence.endswith('easy')}")  # True
print(f"Find 'is': {sentence.find('is')}")  # 7 (first occurrence)
print(f"Find 'Java': {sentence.find('Java')}")  # -1 (not found)
print(f"Count 'Python': {sentence.count('Python')}")  # 2
print(f"'powerful' in sentence: {'powerful' in sentence}")  # True

print("\nChecking Methods:")
print(f"'123'.isdigit(): {'123'.isdigit()}")  # True
print(f"'abc'.isalpha(): {'abc'.isalpha()}")  # True
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")  # True
print(f"'   '.isspace(): {'   '.isspace()}")  # True
print(f"'Hello'.istitle(): {'Hello'.istitle()}")  # True


print('======Searching and Checking========')
text = "   Hello, World!   "
email = "user@example.com"

print("\nModification Methods:")
print(f"Strip whitespace: '{text.strip()}'")  # 'Hello, World!'
print(f"Strip left: '{text.lstrip()}'")      # 'Hello, World!   '
print(f"Strip right: '{text.rstrip()}'")     # '   Hello, World!'

# Replace
message = "I like Java. Java is good."
print(f"Replace 'Java' with 'Python': {message.replace('Java', 'Python')}")

# Split and Join
csv_data = "apple,banana,cherry,dates"
print(f"Split by comma: {csv_data.split(',')}")
print(f"Split by comma (first 2): {csv_data.split(',', 2)}")

words = ['Python', 'is', 'awesome']
print(f"Join words: {' '.join(words)}")  # 'Python is awesome'
print(f"Join with dash: {'-'.join(words)}")  # 'Python-is-awesome'

# Partition
filename = "document.pdf"
print(f"Partition by dot: {filename.partition('.')}")  # ('document', '.', 'pdf')

print('======Formatting Methods========')

# Alignment
text = "Python"
print("\nAlignment Methods:")
print(f"Center(10): '{text.center(10)}'")      # '  Python  '
print(f"Center(10, '*'): '{text.center(10, '*')}'")  # '**Python**'
print(f"Left justify: '{text.ljust(10, '-')}'")    # 'Python----'
print(f"Right justify: '{text.rjust(10, '-')}'")   # '----Python'

# Zfill (zero fill)
number = "42"
print(f"Zfill(5): '{number.zfill(5)}'")  # '00042'

# Expand tabs
tab_text = "Name:\tJohn\tAge:\t25"
print(f"Expand tabs (4 spaces): '{tab_text.expandtabs(4)}'")


print('====== String Formatting========')
name = "Alice"
age = 30
salary = 50000.50

print("\nString Formatting:")
# Old style common in C- language 
print("Old style: %s is %d years old" % (name, age))

# .format() method
print(".format(): {} is {} years old".format(name, age))
print(".format(): {0} earns ${1:,.2f}".format(name, salary))
print(".format(): {n} is {a} years old".format(n=name, a=age))

# f-strings (Python 3.6+)
print(f"f-string: {name} is {age} years old")
print(f"f-string: Salary: ${salary:,.2f}")
print(f"f-string: Age in binary: {age:b}")
print(f"f-string: Hex value: {age:#x}")
print(f"f-string: {name.upper()} has {len(name)} letters")