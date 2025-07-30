# Python Fundamentals - Complete Reference Guide

## Table of Contents
1. [Data Types](#data-types)
2. [Variables and Basic Operations](#variables-and-basic-operations)
3. [Loops](#loops)
4. [Lists](#lists)
5. [Dictionaries](#dictionaries)
6. [List and Dictionary Comprehensions](#comprehensions)
7. [Essential Programs](#essential-programs)

---

## Data Types

### Basic Data Types

```python
# Numbers
integer_num = 42
float_num = 3.14
complex_num = 3 + 4j

# Strings
single_quote = 'Hello'
double_quote = "World"
multiline = """This is a
multiline string"""

# Boolean
is_true = True
is_false = False

# None type
nothing = None

# Type checking
print(type(integer_num))  # <class 'int'>
print(isinstance(float_num, float))  # True
```

### String Operations

```python
text = "Python Programming"

# String methods
print(text.lower())        # python programming
print(text.upper())        # PYTHON PROGRAMMING
print(text.split())        # ['Python', 'Programming']
print(text.replace('Python', 'Java'))  # Java Programming

# String formatting
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")
print("My name is {} and I'm {} years old".format(name, age))
print("My name is %s and I'm %d years old" % (name, age))

# String slicing
print(text[0:6])    # Python
print(text[:6])     # Python
print(text[7:])     # Programming
print(text[-11:])   # Programming
```

---

## Variables and Basic Operations

### Variable Assignment

```python
# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0

# Swapping variables
a, b = b, a

# Augmented assignment
count = 10
count += 5    # count = count + 5
count -= 3    # count = count - 3
count *= 2    # count = count * 2
count //= 4   # count = count // 4
```

### Arithmetic Operations

```python
# Basic operations
a, b = 10, 3

addition = a + b      # 13
subtraction = a - b   # 7
multiplication = a * b # 30
division = a / b      # 3.333...
floor_division = a // b # 3
modulus = a % b       # 1
exponentiation = a ** b # 1000

# Math functions
import math
print(math.sqrt(16))    # 4.0
print(math.ceil(3.2))   # 4
print(math.floor(3.8))  # 3
print(abs(-5))          # 5
```

---

## Loops

### For Loops

```python
# Basic for loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range with start, stop, step
for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8

# Iterating over strings
for char in "Hello":
    print(char)  # H, e, l, l, o

# Iterating over lists
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# Enumerate for index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

### While Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with else
num = 10
while num > 0:
    if num == 5:
        break
    print(num)
    num -= 1
else:
    print("Loop completed without break")

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

### Loop Control

```python
# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)      # 0, 1, 2, 4, 5, 6

# Pass statement
for i in range(5):
    if i == 2:
        pass  # Placeholder, do nothing
    print(i)
```

---

## Lists

### Creating and Accessing Lists

```python
# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# Accessing elements
print(numbers[0])     # 1 (first element)
print(numbers[-1])    # 5 (last element)
print(numbers[1:4])   # [2, 3, 4] (slicing)
print(numbers[:3])    # [1, 2, 3]
print(numbers[2:])    # [3, 4, 5]
```

### List Methods and Operations

```python
fruits = ['apple', 'banana']

# Adding elements
fruits.append('orange')           # ['apple', 'banana', 'orange']
fruits.insert(1, 'grape')         # ['apple', 'grape', 'banana', 'orange']
fruits.extend(['mango', 'kiwi'])  # Add multiple elements

# Removing elements
fruits.remove('banana')  # Remove first occurrence
popped = fruits.pop()    # Remove and return last element
deleted = fruits.pop(0)  # Remove and return element at index
del fruits[1]            # Delete element at index

# Other useful methods
fruits_copy = fruits.copy()        # Create a copy
fruits.reverse()                   # Reverse in place
fruits.sort()                      # Sort in place
count = fruits.count('apple')      # Count occurrences
index = fruits.index('orange')     # Find index of element

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2          # [1, 2, 3, 4, 5, 6]
repeated = list1 * 3              # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Working with Lists

```python
# List unpacking
coordinates = [10, 20]
x, y = coordinates

# Multiple assignment with lists
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers  # first=1, middle=[2,3,4], last=5

# List as stack (LIFO)
stack = []
stack.append(1)    # Push
stack.append(2)
item = stack.pop() # Pop (returns 2)

# List as queue (FIFO) - better to use collections.deque
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)         # Add to right
item = queue.popleft()  # Remove from left
```

---

## Dictionaries

### Creating and Accessing Dictionaries

```python
# Creating dictionaries
empty_dict = {}
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
dict_from_tuples = dict([('a', 1), ('b', 2), ('c', 3)])
dict_comprehension = {x: x**2 for x in range(5)}

# Accessing values
print(person['name'])           # Alice
print(person.get('age'))        # 25
print(person.get('phone', 'N/A'))  # N/A (default value)

# Modifying dictionaries
person['age'] = 26              # Update existing key
person['phone'] = '123-456'     # Add new key
```

### Dictionary Methods

```python
student = {'name': 'Bob', 'grade': 'A', 'subject': 'Math'}

# Dictionary methods
keys = student.keys()           # dict_keys(['name', 'grade', 'subject'])
values = student.values()       # dict_values(['Bob', 'A', 'Math'])
items = student.items()         # dict_items([('name', 'Bob'), ...])

# Removing elements
removed = student.pop('grade')          # Remove and return value
student.popitem()                       # Remove and return last item
del student['subject']                  # Delete key
student.clear()                         # Remove all items

# Other useful methods
student_copy = student.copy()           # Shallow copy
student.update({'age': 20, 'city': 'LA'})  # Update with another dict
student.setdefault('phone', 'N/A')     # Set if key doesn't exist
```

### Working with Dictionaries

```python
# Iterating over dictionaries
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}

# Iterate over keys
for name in scores:
    print(name)

# Iterate over values
for score in scores.values():
    print(score)

# Iterate over key-value pairs
for name, score in scores.items():
    print(f"{name}: {score}")

# Dictionary operations
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}  # Merge dictionaries (Python 3.5+)

# Check if key exists
if 'Alice' in scores:
    print("Alice is in the dictionary")

# Nested dictionaries
students = {
    'Alice': {'grade': 'A', 'subjects': ['Math', 'Science']},
    'Bob': {'grade': 'B', 'subjects': ['English', 'History']}
}
print(students['Alice']['subjects'])  # ['Math', 'Science']
```

---

## Comprehensions

### List Comprehensions

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
# Equivalent to:
# squares = []
# for x in range(10):
#     squares.append(x**2)

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# List comprehension with if-else
abs_values = [x if x >= 0 else -x for x in [-3, -1, 0, 1, 3]]

# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
# Creates: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Flattening a nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Working with strings
words = ['hello', 'world', 'python']
lengths = [len(word) for word in words]
uppercase = [word.upper() for word in words if len(word) > 4]
```

### Dictionary Comprehensions

```python
# Basic dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Swapping keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}

# Creating dictionary from two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}

# Filtering dictionary
scores = {'Alice': 95, 'Bob': 67, 'Charlie': 89, 'David': 78}
high_scores = {name: score for name, score in scores.items() if score >= 80}
```

### Set Comprehensions

```python
# Basic set comprehension
unique_squares = {x**2 for x in range(-5, 6)}

# Set comprehension with condition
even_numbers = {x for x in range(20) if x % 2 == 0}

# Removing duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
```

### Generator Expressions

```python
# Generator expression (memory efficient)
squares_gen = (x**2 for x in range(1000000))  # Doesn't create list in memory

# Using generator in functions
sum_of_squares = sum(x**2 for x in range(100))
max_even = max(x for x in range(20) if x % 2 == 0)

# Generator vs List comprehension
list_comp = [x**2 for x in range(10)]    # Creates list immediately
gen_exp = (x**2 for x in range(10))      # Creates generator object
```

---

## Essential Programs

### 1. Basic Input/Output Programs

```python
# Simple calculator
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")

# Temperature converter
def temp_converter():
    temp = float(input("Enter temperature: "))
    scale = input("Enter scale (C for Celsius, F for Fahrenheit): ").upper()
    
    if scale == 'C':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C = {fahrenheit}°F")
    elif scale == 'F':
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F = {celsius}°C")
    else:
        print("Invalid scale")
```

### 2. Number Programs

```python
# Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Factorial calculation
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Find GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Check if number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Sum of digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
```

### 3. String Programs

```python
# Check if string is palindrome
def is_string_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

# Count vowels and consonants
def count_vowels_consonants(text):
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

# Reverse words in a sentence
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

# Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Remove duplicates from string
def remove_duplicates(s):
    return ''.join(dict.fromkeys(s))

# Count character frequency
def char_frequency(text):
    return {char: text.count(char) for char in set(text)}
```

### 4. List Programs

```python
# Find second largest number
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

# Remove duplicates while preserving order
def remove_duplicates_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Find common elements in two lists
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Rotate list by n positions
def rotate_list(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]

# Find missing number in sequence
def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

# Merge two sorted lists
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged
```

### 5. Dictionary Programs

```python
# Count word frequency in text
def word_frequency(text):
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}

# Group anagrams
def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]
    return list(anagram_groups.values())

# Dictionary operations
def dict_operations():
    # Merge dictionaries
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged = {**dict1, **dict2}
    
    # Find key with maximum value
    scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
    max_key = max(scores, key=scores.get)
    
    # Invert dictionary (swap keys and values)
    inverted = {v: k for k, v in scores.items()}
    
    return merged, max_key, inverted

# Student grade management
class GradeBook:
    def __init__(self):
        self.grades = {}
    
    def add_grade(self, student, subject, grade):
        if student not in self.grades:
            self.grades[student] = {}
        self.grades[student][subject] = grade
    
    def get_average(self, student):
        if student in self.grades:
            grades = self.grades[student].values()
            return sum(grades) / len(grades)
        return None
    
    def get_top_student(self):
        averages = {student: self.get_average(student) 
                   for student in self.grades}
        return max(averages, key=averages.get)
```

### 6. Pattern Programs

```python
# Print various patterns
def print_patterns():
    # Right triangle
    def right_triangle(n):
        for i in range(1, n + 1):
            print('*' * i)
    
    # Pyramid
    def pyramid(n):
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
    
    # Diamond
    def diamond(n):
        # Upper half
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
        # Lower half
        for i in range(n - 1, 0, -1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
    
    # Number pattern
    def number_pattern(n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()

# Pascal's triangle
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
```

### 7. Sorting and Searching

```python
# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Linear search
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
```

### 8. File Operations

```python
# Read and write files
def file_operations():
    # Write to file
    def write_file(filename, content):
        with open(filename, 'w') as file:
            file.write(content)
    
    # Read from file
    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"
    
    # Count lines, words, characters
    def file_stats(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                lines = content.count('\n') + 1
                words = len(content.split())
                chars = len(content)
                return {'lines': lines, 'words': words, 'characters': chars}
        except FileNotFoundError:
            return "File not found"
    
    # Copy file
    def copy_file(source, destination):
        try:
            with open(source, 'r') as src, open(destination, 'w') as dest:
                dest.write(src.read())
            return "File copied successfully"
        except FileNotFoundError:
            return "Source file not found"

# CSV operations (basic)
def csv_operations():
    # Write CSV
    def write_csv(filename, data):
        with open(filename, 'w') as file:
            for row in data:
                file.write(','.join(map(str, row)) + '\n')
    
    # Read CSV
    def read_csv(filename):
        data = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data.append(line.strip().split(','))
            return data
        except FileNotFoundError:
            return "File not found"
```

---

## Usage Examples and Tips

### Best Practices

```python
# Use meaningful variable names
student_score = 95  # Good
s = 95             # Bad

# Use list comprehensions for simple transformations
squares = [x**2 for x in range(10)]  # Good
squares = []                         # Less efficient
for x in range(10):
    squares.append(x**2)

# Use f-strings for string formatting (Python 3.6+)
name, age = "Alice", 25
message = f"Hello, {name}! You are {age} years old."  # Good
message = "Hello, {}! You are {} years old.".format(name, age)  # OK
message = "Hello, " + name + "! You are " + str(age) + " years old."  # Bad

# Use enumerate() when you need both index and value
items = ['a', 'b', 'c']
for i, item in enumerate(items):  # Good
    print(f"{i}: {item}")

# Don't do this:
for i in range(len(items)):       # Less Pythonic
    print(f"{i}: {items[i]}")
```

### Common Patterns

```python
# Safe dictionary access
data = {'name': 'Alice'}
age = data.get('age', 0)  # Returns 0 if 'age' key doesn't exist

# Multiple conditions
x = 10
if 5 < x < 15:  # Pythonic way
    print("x is between 5 and 15")

# Swapping variables
a, b = 5, 10
a, b = b, a  # Now a=10, b=5

# Working with files
with open('file.txt', 'r') as f:  # Automatically closes file
    content = f.read()

# List slicing tricks
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]    # [5, 4, 3, 2, 1]
every_second = numbers[::2]      # [1, 3, 5]
last_three = numbers[-3:]        # [3, 4, 5]
```

This comprehensive guide covers all the Python fundamentals you requested. Each section includes practical examples and common use cases that you'll encounter in real programming scenarios.