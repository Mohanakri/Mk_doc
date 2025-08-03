# Python Interview Programs Collection
# Categories: Integer, String, List (20 each)
# Multiple solutions using functions, loops, and comprehensions

print("=" * 80)
print("PYTHON INTERVIEW PROGRAMS COLLECTION")
print("=" * 80)

# ============================================================================
# INTEGER PROGRAMS (20)
# ============================================================================

print("\n" + "="*50)
print("INTEGER PROGRAMS")
print("="*50)

# 1. Check if number is prime
print("\n1. Check Prime Number")
def is_prime_func(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_prime_loop(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def is_prime_comp(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

num = 17
print(f"Function: {num} is prime: {is_prime_func(num)}")
print(f"Loop: {num} is prime: {is_prime_loop(num)}")
print(f"Comprehension: {num} is prime: {is_prime_comp(num)}")

# 2. Factorial of a number
print("\n2. Factorial")
def factorial_func(n):
    if n <= 1: return 1
    return n * factorial_func(n-1)

def factorial_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_comp(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n+1), 1)

num = 5
print(f"Function: {num}! = {factorial_func(num)}")
print(f"Loop: {num}! = {factorial_loop(num)}")
print(f"Comprehension: {num}! = {factorial_comp(num)}")

# 3. Fibonacci sequence
print("\n3. Fibonacci")
def fibonacci_func(n):
    if n <= 1: return n
    return fibonacci_func(n-1) + fibonacci_func(n-2)

def fibonacci_loop(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fibonacci_comp(n):
    fib_list = [0, 1]
    [fib_list.append(fib_list[-1] + fib_list[-2]) for _ in range(2, n+1)]
    return fib_list[n] if n < len(fib_list) else 0

num = 10
print(f"Function: Fib({num}) = {fibonacci_func(num)}")
print(f"Loop: Fib({num}) = {fibonacci_loop(num)}")
print(f"Comprehension: Fib({num}) = {fibonacci_comp(num)}")

# 4. Reverse a number
print("\n4. Reverse Number")
def reverse_func(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

def reverse_loop(n):
    result = 0
    temp = abs(n)
    while temp > 0:
        result = result * 10 + temp % 10
        temp //= 10
    return result * (-1 if n < 0 else 1)

def reverse_comp(n):
    digits = [int(d) for d in str(abs(n))]
    return int(''.join(map(str, digits[::-1]))) * (-1 if n < 0 else 1)

num = 12345
print(f"Function: Reverse of {num} = {reverse_func(num)}")
print(f"Loop: Reverse of {num} = {reverse_loop(num)}")
print(f"Comprehension: Reverse of {num} = {reverse_comp(num)}")

# 5. Check palindrome number
print("\n5. Palindrome Number")
def is_palindrome_func(n):
    return str(n) == str(n)[::-1]

def is_palindrome_loop(n):
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num

def is_palindrome_comp(n):
    digits = [int(d) for d in str(n)]
    return digits == digits[::-1]

num = 121
print(f"Function: {num} is palindrome: {is_palindrome_func(num)}")
print(f"Loop: {num} is palindrome: {is_palindrome_loop(num)}")
print(f"Comprehension: {num} is palindrome: {is_palindrome_comp(num)}")

# 6. Sum of digits
print("\n6. Sum of Digits")
def sum_digits_func(n):
    return sum(int(digit) for digit in str(abs(n)))

def sum_digits_loop(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

def sum_digits_comp(n):
    return sum([int(d) for d in str(abs(n))])

num = 12345
print(f"Function: Sum of digits of {num} = {sum_digits_func(num)}")
print(f"Loop: Sum of digits of {num} = {sum_digits_loop(num)}")
print(f"Comprehension: Sum of digits of {num} = {sum_digits_comp(num)}")

# 7. GCD of two numbers
print("\n7. GCD (Greatest Common Divisor)")
def gcd_func(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_loop(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def gcd_comp(a, b):
    return a if b == 0 else gcd_comp(b, a % b)

a, b = 48, 18
print(f"Function: GCD of {a} and {b} = {gcd_func(a, b)}")
print(f"Loop: GCD of {a} and {b} = {gcd_loop(a, b)}")
print(f"Comprehension: GCD of {a} and {b} = {gcd_comp(a, b)}")

# 8. LCM of two numbers
print("\n8. LCM (Least Common Multiple)")
def lcm_func(a, b):
    return abs(a * b) // gcd_func(a, b)

def lcm_loop(a, b):
    larger = max(a, b)
    while True:
        if larger % a == 0 and larger % b == 0:
            return larger
        larger += 1

def lcm_comp(a, b):
    return abs(a * b) // gcd_comp(a, b)

a, b = 12, 15
print(f"Function: LCM of {a} and {b} = {lcm_func(a, b)}")
print(f"Loop: LCM of {a} and {b} = {lcm_loop(a, b)}")
print(f"Comprehension: LCM of {a} and {b} = {lcm_comp(a, b)}")

# 9. Check Armstrong number
print("\n9. Armstrong Number")
def is_armstrong_func(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(digit) ** power for digit in digits)

def is_armstrong_loop(n):
    original = n
    power = len(str(n))
    result = 0
    while n > 0:
        digit = n % 10
        result += digit ** power
        n //= 10
    return original == result

def is_armstrong_comp(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return n == sum([d ** power for d in digits])

num = 153
print(f"Function: {num} is Armstrong: {is_armstrong_func(num)}")
print(f"Loop: {num} is Armstrong: {is_armstrong_loop(num)}")
print(f"Comprehension: {num} is Armstrong: {is_armstrong_comp(num)}")

# 10. Perfect number check
print("\n10. Perfect Number")
def is_perfect_func(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_perfect_loop(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def is_perfect_comp(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

num = 28
print(f"Function: {num} is perfect: {is_perfect_func(num)}")
print(f"Loop: {num} is perfect: {is_perfect_loop(num)}")
print(f"Comprehension: {num} is perfect: {is_perfect_comp(num)}")

# 11. Count digits in a number
print("\n11. Count Digits")
def count_digits_func(n):
    return len(str(abs(n)))

def count_digits_loop(n):
    count = 0
    n = abs(n)
    if n == 0: return 1
    while n > 0:
        count += 1
        n //= 10
    return count

def count_digits_comp(n):
    return len([d for d in str(abs(n))])

num = 12345
print(f"Function: Digits in {num} = {count_digits_func(num)}")
print(f"Loop: Digits in {num} = {count_digits_loop(num)}")
print(f"Comprehension: Digits in {num} = {count_digits_comp(num)}")

# 12. Binary to decimal conversion
print("\n12. Binary to Decimal")
def binary_to_decimal_func(binary):
    return int(binary, 2)

def binary_to_decimal_loop(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal

def binary_to_decimal_comp(binary):
    return sum([int(digit) * (2 ** i) for i, digit in enumerate(reversed(binary))])

binary = "1010"
print(f"Function: Binary {binary} to decimal = {binary_to_decimal_func(binary)}")
print(f"Loop: Binary {binary} to decimal = {binary_to_decimal_loop(binary)}")
print(f"Comprehension: Binary {binary} to decimal = {binary_to_decimal_comp(binary)}")

# 13. Decimal to binary conversion
print("\n13. Decimal to Binary")
def decimal_to_binary_func(n):
    return bin(n)[2:]

def decimal_to_binary_loop(n):
    if n == 0: return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def decimal_to_binary_comp(n):
    if n == 0: return "0"
    bits = []
    temp = n
    while temp > 0:
        bits.append(str(temp % 2))
        temp //= 2
    return ''.join(reversed(bits))

num = 10
print(f"Function: Decimal {num} to binary = {decimal_to_binary_func(num)}")
print(f"Loop: Decimal {num} to binary = {decimal_to_binary_loop(num)}")
print(f"Comprehension: Decimal {num} to binary = {decimal_to_binary_comp(num)}")

# 14. Find factors of a number
print("\n14. Find Factors")
def find_factors_func(n):
    return [i for i in range(1, n+1) if n % i == 0]

def find_factors_loop(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def find_factors_comp(n):
    return [i for i in range(1, n+1) if n % i == 0]

num = 12
print(f"Function: Factors of {num} = {find_factors_func(num)}")
print(f"Loop: Factors of {num} = {find_factors_loop(num)}")
print(f"Comprehension: Factors of {num} = {find_factors_comp(num)}")

# 15. Power of a number
print("\n15. Power of Number")
def power_func(base, exp):
    return base ** exp

def power_loop(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def power_comp(base, exp):
    from functools import reduce
    return reduce(lambda x, y: x * base, range(exp), 1)

base, exp = 2, 5
print(f"Function: {base}^{exp} = {power_func(base, exp)}")
print(f"Loop: {base}^{exp} = {power_loop(base, exp)}")
print(f"Comprehension: {base}^{exp} = {power_comp(base, exp)}")

# 16. Square root using Newton's method
print("\n16. Square Root")
def sqrt_func(n):
    return n ** 0.5

def sqrt_loop(n):
    if n == 0: return 0
    x = n
    while True:
        root = 0.5 * (x + (n / x))
        if abs(root - x) < 0.000001:
            break
        x = root
    return root

def sqrt_comp(n):
    import math
    return math.sqrt(n)

num = 25
print(f"Function: √{num} = {sqrt_func(num)}")
print(f"Loop: √{num} = {sqrt_loop(num)}")
print(f"Comprehension: √{num} = {sqrt_comp(num)}")

# 17. Check if number is even or odd
print("\n17. Even or Odd")
def is_even_func(n):
    return n % 2 == 0

def is_even_loop(n):
    return (n // 2) * 2 == n

def is_even_comp(n):
    return not bool(n & 1)

num = 7
print(f"Function: {num} is even: {is_even_func(num)}")
print(f"Loop: {num} is even: {is_even_loop(num)}")
print(f"Comprehension: {num} is even: {is_even_comp(num)}")

# 18. Sum of first n natural numbers
print("\n18. Sum of First N Natural Numbers")
def sum_natural_func(n):
    return n * (n + 1) // 2

def sum_natural_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum_natural_comp(n):
    return sum([i for i in range(1, n+1)])

num = 10
print(f"Function: Sum of first {num} natural numbers = {sum_natural_func(num)}")
print(f"Loop: Sum of first {num} natural numbers = {sum_natural_loop(num)}")
print(f"Comprehension: Sum of first {num} natural numbers = {sum_natural_comp(num)}")

# 19. Find largest digit in a number
print("\n19. Largest Digit")
def largest_digit_func(n):
    return max(int(digit) for digit in str(abs(n)))

def largest_digit_loop(n):
    largest = 0
    n = abs(n)
    while n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n //= 10
    return largest

def largest_digit_comp(n):
    return max([int(d) for d in str(abs(n))])

num = 78342
print(f"Function: Largest digit in {num} = {largest_digit_func(num)}")
print(f"Loop: Largest digit in {num} = {largest_digit_loop(num)}")
print(f"Comprehension: Largest digit in {num} = {largest_digit_comp(num)}")

# 20. Check if number is positive, negative, or zero
print("\n20. Sign Check")
def check_sign_func(n):
    return "positive" if n > 0 else "negative" if n < 0 else "zero"

def check_sign_loop(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def check_sign_comp(n):
    signs = {True: "positive", False: "negative"}
    return signs.get(n > 0, "zero") if n != 0 else "zero"

num = -5
print(f"Function: {num} is {check_sign_func(num)}")
print(f"Loop: {num} is {check_sign_loop(num)}")
print(f"Comprehension: {num} is {check_sign_comp(num)}")

# ============================================================================
# STRING PROGRAMS (20)
# ============================================================================

print("\n\n" + "="*50)
print("STRING PROGRAMS")
print("="*50)

# 1. Reverse a string
print("\n1. Reverse String")
def reverse_string_func(s):
    return s[::-1]

def reverse_string_loop(s):
    result = ""
    for char in s:
        result = char + result
    return result

def reverse_string_comp(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

string = "hello"
print(f"Function: Reverse of '{string}' = '{reverse_string_func(string)}'")
print(f"Loop: Reverse of '{string}' = '{reverse_string_loop(string)}'")
print(f"Comprehension: Reverse of '{string}' = '{reverse_string_comp(string)}'")

# 2. Check if string is palindrome
print("\n2. String Palindrome")
def is_palindrome_string_func(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_palindrome_string_loop(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_string_comp(s):
    s = s.lower().replace(" ", "")
    return all(s[i] == s[-(i+1)] for i in range(len(s)//2))

string = "A man a plan a canal Panama"
print(f"Function: '{string}' is palindrome: {is_palindrome_string_func(string)}")
print(f"Loop: '{string}' is palindrome: {is_palindrome_string_loop(string)}")
print(f"Comprehension: '{string}' is palindrome: {is_palindrome_string_comp(string)}")

# 3. Count vowels and consonants
print("\n3. Count Vowels and Consonants")
def count_vowels_func(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count

def count_vowels_loop(s):
    vowels = "aeiouAEIOU"
    v_count = c_count = 0
    for char in s:
        if char in vowels:
            v_count += 1
        elif char.isalpha():
            c_count += 1
    return v_count, c_count

def count_vowels_comp(s):
    vowels = "aeiouAEIOU"
    v_count = len([c for c in s if c in vowels])
    c_count = len([c for c in s if c.isalpha() and c not in vowels])
    return v_count, c_count

string = "Hello World"
print(f"Function: Vowels and consonants in '{string}': {count_vowels_func(string)}")
print(f"Loop: Vowels and consonants in '{string}': {count_vowels_loop(string)}")
print(f"Comprehension: Vowels and consonants in '{string}': {count_vowels_comp(string)}")

# 4. Remove duplicates from string
print("\n4. Remove Duplicates")
def remove_duplicates_func(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

def remove_duplicates_loop(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

def remove_duplicates_comp(s):
    seen = set()
    return ''.join([char for char in s if not (char in seen or seen.add(char))])

string = "programming"
print(f"Function: Remove duplicates from '{string}': '{remove_duplicates_func(string)}'")
print(f"Loop: Remove duplicates from '{string}': '{remove_duplicates_loop(string)}'")
print(f"Comprehension: Remove duplicates from '{string}': '{remove_duplicates_comp(string)}'")

# 5. Find longest word in string
print("\n5. Longest Word")
def longest_word_func(s):
    words = s.split()
    return max(words, key=len)

def longest_word_loop(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def longest_word_comp(s):
    words = s.split()
    return max([word for word in words], key=len)

string = "The quick brown fox jumps"
print(f"Function: Longest word in '{string}': '{longest_word_func(string)}'")
print(f"Loop: Longest word in '{string}': '{longest_word_loop(string)}'")
print(f"Comprehension: Longest word in '{string}': '{longest_word_comp(string)}'")

# 6. Count frequency of each character
print("\n6. Character Frequency")
def char_frequency_func(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def char_frequency_loop(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def char_frequency_comp(s):
    return {char: s.count(char) for char in set(s)}

string = "hello"
print(f"Function: Character frequency in '{string}': {char_frequency_func(string)}")
print(f"Loop: Character frequency in '{string}': {char_frequency_loop(string)}")
print(f"Comprehension: Character frequency in '{string}': {char_frequency_comp(string)}")

# 7. Check if two strings are anagrams
print("\n7. Check Anagrams")
def are_anagrams_func(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def are_anagrams_loop(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1.lower():
        count[char] = count.get(char, 0) + 1
    for char in s2.lower():
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return all(val == 0 for val in count.values())

def are_anagrams_comp(s1, s2):
    return sorted([c.lower() for c in s1]) == sorted([c.lower() for c in s2])

s1, s2 = "listen", "silent"
print(f"Function: '{s1}' and '{s2}' are anagrams: {are_anagrams_func(s1, s2)}")
print(f"Loop: '{s1}' and '{s2}' are anagrams: {are_anagrams_loop(s1, s2)}")
print(f"Comprehension: '{s1}' and '{s2}' are anagrams: {are_anagrams_comp(s1, s2)}")

# 8. Convert string to title case
print("\n8. Title Case")
def title_case_func(s):
    return s.title()

def title_case_loop(s):
    result = ""
    capitalize_next = True
    for char in s:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char.lower()
        else:
            result += char
            capitalize_next = True
    return result

def title_case_comp(s):
    words = s.split()
    return ' '.join([word.capitalize() for word in words])

string = "hello world python"
print(f"Function: Title case of '{string}': '{title_case_func(string)}'")
print(f"Loop: Title case of '{string}': '{title_case_loop(string)}'")
print(f"Comprehension: Title case of '{string}': '{title_case_comp(string)}'")

# 9. Replace substring in string
print("\n9. Replace Substring")
def replace_substring_func(s, old, new):
    return s.replace(old, new)

def replace_substring_loop(s, old, new):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result

def replace_substring_comp(s, old, new):
    parts = s.split(old)
    return new.join(parts)

string = "Hello World World"
old, new = "World", "Python"
print(f"Function: Replace '{old}' with '{new}' in '{string}': '{replace_substring_func(string, old, new)}'")
print(f"Loop: Replace '{old}' with '{new}' in '{string}': '{replace_substring_loop(string, old, new)}'")
print(f"Comprehension: Replace '{old}' with '{new}' in '{string}': '{replace_substring_comp(string, old, new)}'")

# 10. Count words in string
print("\n10. Count Words")
def count_words_func(s):
    return len(s.split())

def count_words_loop(s):
    count = 0
    in_word = False
    for char in s:
        if char != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count

def count_words_comp(s):
    return len([word for word in s.split() if word])

string = "The quick brown fox"
print(f"Function: Word count in '{string}': {count_words_func(string)}")
print(f"Loop: Word count in '{string}': {count_words_loop(string)}")
print(f"Comprehension: Word count in '{string}': {count_words_comp(string)}")

# 11. Find first non-repeating character
print("\n11. First Non-Repeating Character")
def first_non_repeating_func(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

def first_non_repeating_loop(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

def first_non_repeating_comp(s):
    char_counts = {char: s.count(char) for char in set(s)}
    non_repeating = [char for char in s if char_counts[char] == 1]
    return non_repeating[0] if non_repeating else None

string = "abccba"
print(f"Function: First non-repeating in '{string}': {first_non_repeating_func(string)}")
print(f"Loop: First non-repeating in '{string}': {first_non_repeating_loop(string)}")
print(f"Comprehension: First non-repeating in '{string}': {first_non_repeating_comp(string)}")

# 12. Check if string contains only digits
print("\n12. Check Only Digits")
def is_only_digits_func(s):
    return s.isdigit()

def is_only_digits_loop(s):
    if not s:
        return False
    for char in s:
        if not char.isdigit():
            return False
    return True

def is_only_digits_comp(s):
    return len(s) > 0 and all(char.isdigit() for char in s)

string = "12345"
print(f"Function: '{string}' contains only digits: {is_only_digits_func(string)}")
print(f"Loop: '{string}' contains only digits: {is_only_digits_loop(string)}")
print(f"Comprehension: '{string}' contains only digits: {is_only_digits_comp(string)}")

# 13. Remove spaces from string
print("\n13. Remove Spaces")
def remove_spaces_func(s):
    return s.replace(" ", "")

def remove_spaces_loop(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

def remove_spaces_comp(s):
    return ''.join([char for char in s if char != " "])

string = "Hello World Python"
print(f"Function: Remove spaces from '{string}': '{remove_spaces_func(string)}'")
print(f"Loop: Remove spaces from '{string}': '{remove_spaces_loop(string)}'")
print(f"Comprehension: Remove spaces from '{string}': '{remove_spaces_comp(string)}'")

# 14. Convert string to lowercase/uppercase
print("\n14. Case Conversion")
def convert_case_func(s, to_upper=True):
    return s.upper() if to_upper else s.lower()

def convert_case_loop(s, to_upper=True):
    result = ""
    for char in s:
        if to_upper:
            result += char.upper()
        else:
            result += char.lower()
    return result

def convert_case_comp(s, to_upper=True):
    return ''.join([char.upper() if to_upper else char.lower() for char in s])

string = "Hello World"
print(f"Function: Uppercase '{string}': '{convert_case_func(string, True)}'")
print(f"Loop: Lowercase '{string}': '{convert_case_loop(string, False)}'")
print(f"Comprehension: Uppercase '{string}': '{convert_case_comp(string, True)}'")

# 15. Find substring in string
print("\n15. Find Substring")
def find_substring_func(s, sub):
    return s.find(sub)

def find_substring_loop(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1

def find_substring_comp(s, sub):
    indices = [i for i in range(len(s) - len(sub) + 1) if s[i:i+len(sub)] == sub]
    return indices[0] if indices else -1

string = "Hello World"
substring = "World"
print(f"Function: Index of '{substring}' in '{string}': {find_substring_func(string, substring)}")
print(f"Loop: Index of '{substring}' in '{string}': {find_substring_loop(string, substring)}")
print(f"Comprehension: Index of '{substring}' in '{string}': {find_substring_comp(string, substring)}")

# 16. Capitalize first letter of each word
print("\n16. Capitalize Words")
def capitalize_words_func(s):
    return ' '.join(word.capitalize() for word in s.split())

def capitalize_words_loop(s):
    words = s.split()
    result = []
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:].lower())
    return ' '.join(result)

def capitalize_words_comp(s):
    return ' '.join([word.capitalize() for word in s.split()])

string = "hello world python programming"
print(f"Function: Capitalize words in '{string}': '{capitalize_words_func(string)}'")
print(f"Loop: Capitalize words in '{string}': '{capitalize_words_loop(string)}'")
print(f"Comprehension: Capitalize words in '{string}': '{capitalize_words_comp(string)}'")

# 17. Reverse words in string
print("\n17. Reverse Words")
def reverse_words_func(s):
    return ' '.join(s.split()[::-1])

def reverse_words_loop(s):
    words = s.split()
    result = []
    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])
    return ' '.join(result)

def reverse_words_comp(s):
    return ' '.join([word for word in reversed(s.split())])

string = "Hello World Python"
print(f"Function: Reverse words in '{string}': '{reverse_words_func(string)}'")
print(f"Loop: Reverse words in '{string}': '{reverse_words_loop(string)}'")
print(f"Comprehension: Reverse words in '{string}': '{reverse_words_comp(string)}'")

# 18. Check if string is empty or whitespace
print("\n18. Check Empty/Whitespace")
def is_empty_or_whitespace_func(s):
    return not s.strip()

def is_empty_or_whitespace_loop(s):
    for char in s:
        if char != ' ' and char != '\t' and char != '\n':
            return False
    return True

def is_empty_or_whitespace_comp(s):
    return all(char in ' \t\n' for char in s) if s else True

string = "   "
print(f"Function: '{string}' is empty/whitespace: {is_empty_or_whitespace_func(string)}")
print(f"Loop: '{string}' is empty/whitespace: {is_empty_or_whitespace_loop(string)}")
print(f"Comprehension: '{string}' is empty/whitespace: {is_empty_or_whitespace_comp(string)}")

# 19. Extract numbers from string
print("\n19. Extract Numbers")
def extract_numbers_func(s):
    import re
    return re.findall(r'\d+', s)

def extract_numbers_loop(s):
    numbers = []
    current_num = ""
    for char in s:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                numbers.append(current_num)
                current_num = ""
    if current_num:
        numbers.append(current_num)
    return numbers

def extract_numbers_comp(s):
    result = []
    current = ""
    for char in s:
        if char.isdigit():
            current += char
        elif current:
            result.append(current)
            current = ""
    if current:
        result.append(current)
    return result

string = "I have 10 apples and 25 oranges"
print(f"Function: Extract numbers from '{string}': {extract_numbers_func(string)}")
print(f"Loop: Extract numbers from '{string}': {extract_numbers_loop(string)}")
print(f"Comprehension: Extract numbers from '{string}': {extract_numbers_comp(string)}")

# 20. Count occurrences of substring
print("\n20. Count Substring Occurrences")
def count_substring_func(s, sub):
    return s.count(sub)

def count_substring_loop(s, sub):
    count = 0
    start = 0
    while start < len(s):
        pos = s.find(sub, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count

def count_substring_comp(s, sub):
    return len([i for i in range(len(s) - len(sub) + 1) if s[i:i+len(sub)] == sub])

string = "abababa"
substring = "aba"
print(f"Function: Count '{substring}' in '{string}': {count_substring_func(string, substring)}")
print(f"Loop: Count '{substring}' in '{string}': {count_substring_loop(string, substring)}")
print(f"Comprehension: Count '{substring}' in '{string}': {count_substring_comp(string, substring)}")

# ============================================================================
# LIST PROGRAMS (20)
# ============================================================================

print("\n\n" + "="*50)
print("LIST PROGRAMS")
print("="*50)

# 1. Find maximum element in list
print("\n1. Find Maximum")
def find_max_func(lst):
    return max(lst) if lst else None

def find_max_loop(lst):
    if not lst:
        return None
    maximum = lst[0]
    for num in lst[1:]:
        if num > maximum:
            maximum = num
    return maximum

def find_max_comp(lst):
    return max([num for num in lst]) if lst else None

numbers = [3, 7, 2, 9, 1, 5]
print(f"Function: Maximum in {numbers}: {find_max_func(numbers)}")
print(f"Loop: Maximum in {numbers}: {find_max_loop(numbers)}")
print(f"Comprehension: Maximum in {numbers}: {find_max_comp(numbers)}")

# 2. Find minimum element in list
print("\n2. Find Minimum")
def find_min_func(lst):
    return min(lst) if lst else None

def find_min_loop(lst):
    if not lst:
        return None
    minimum = lst[0]
    for num in lst[1:]:
        if num < minimum:
            minimum = num
    return minimum

def find_min_comp(lst):
    return min([num for num in lst]) if lst else None

numbers = [3, 7, 2, 9, 1, 5]
print(f"Function: Minimum in {numbers}: {find_min_func(numbers)}")
print(f"Loop: Minimum in {numbers}: {find_min_loop(numbers)}")
print(f"Comprehension: Minimum in {numbers}: {find_min_comp(numbers)}")

# 3. Sum of all elements
print("\n3. Sum of Elements")
def sum_elements_func(lst):
    return sum(lst)

def sum_elements_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total

def sum_elements_comp(lst):
    return sum([num for num in lst])

numbers = [1, 2, 3, 4, 5]
print(f"Function: Sum of {numbers}: {sum_elements_func(numbers)}")
print(f"Loop: Sum of {numbers}: {sum_elements_loop(numbers)}")
print(f"Comprehension: Sum of {numbers}: {sum_elements_comp(numbers)}")

# 4. Reverse a list
print("\n4. Reverse List")
def reverse_list_func(lst):
    return lst[::-1]

def reverse_list_loop(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

def reverse_list_comp(lst):
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]

numbers = [1, 2, 3, 4, 5]
print(f"Function: Reverse of {numbers}: {reverse_list_func(numbers)}")
print(f"Loop: Reverse of {numbers}: {reverse_list_loop(numbers)}")
print(f"Comprehension: Reverse of {numbers}: {reverse_list_comp(numbers)}")

# 5. Remove duplicates from list
print("\n5. Remove Duplicates")
def remove_duplicates_list_func(lst):
    return list(set(lst))

def remove_duplicates_list_loop(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates_list_comp(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"Function: Remove duplicates from {numbers}: {remove_duplicates_list_func(numbers)}")
print(f"Loop: Remove duplicates from {numbers}: {remove_duplicates_list_loop(numbers)}")
print(f"Comprehension: Remove duplicates from {numbers}: {remove_duplicates_list_comp(numbers)}")

# 6. Find second largest element
print("\n6. Second Largest")
def second_largest_func(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[-2]

def second_largest_loop(lst):
    if len(lst) < 2:
        return None
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

def second_largest_comp(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None

numbers = [1, 3, 4, 5, 5, 2]
print(f"Function: Second largest in {numbers}: {second_largest_func(numbers)}")
print(f"Loop: Second largest in {numbers}: {second_largest_loop(numbers)}")
print(f"Comprehension: Second largest in {numbers}: {second_largest_comp(numbers)}")

# 7. Check if list is sorted
print("\n7. Check Sorted")
def is_sorted_func(lst):
    return lst == sorted(lst)

def is_sorted_loop(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True

def is_sorted_comp(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

numbers = [1, 2, 3, 4, 5]
print(f"Function: {numbers} is sorted: {is_sorted_func(numbers)}")
print(f"Loop: {numbers} is sorted: {is_sorted_loop(numbers)}")
print(f"Comprehension: {numbers} is sorted: {is_sorted_comp(numbers)}")

# 8. Merge two sorted lists
print("\n8. Merge Sorted Lists")
def merge_sorted_func(lst1, lst2):
    return sorted(lst1 + lst2)

def merge_sorted_loop(lst1, lst2):
    result = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

def merge_sorted_comp(lst1, lst2):
    merged = lst1 + lst2
    return sorted([x for x in merged])

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(f"Function: Merge {list1} and {list2}: {merge_sorted_func(list1, list2)}")
print(f"Loop: Merge {list1} and {list2}: {merge_sorted_loop(list1, list2)}")
print(f"Comprehension: Merge {list1} and {list2}: {merge_sorted_comp(list1, list2)}")

# 9. Find intersection of two lists
print("\n9. List Intersection")
def intersection_func(lst1, lst2):
    return list(set(lst1) & set(lst2))

def intersection_loop(lst1, lst2):
    result = []
    for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
    return result

def intersection_comp(lst1, lst2):
    return [x for x in lst1 if x in lst2]

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(f"Function: Intersection of {list1} and {list2}: {intersection_func(list1, list2)}")
print(f"Loop: Intersection of {list1} and {list2}: {intersection_loop(list1, list2)}")
print(f"Comprehension: Intersection of {list1} and {list2}: {intersection_comp(list1, list2)}")

# 10. Rotate list by k positions
print("\n10. Rotate List")
def rotate_list_func(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]

def rotate_list_loop(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    result = []
    for i in range(k, len(lst)):
        result.append(lst[i])
    for i in range(k):
        result.append(lst[i])
    return result

def rotate_list_comp(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return [lst[i] for i in range(k, len(lst))] + [lst[i] for i in range(k)]

numbers = [1, 2, 3, 4, 5]
k = 2
print(f"Function: Rotate {numbers} by {k}: {rotate_list_func(numbers, k)}")
print(f"Loop: Rotate {numbers} by {k}: {rotate_list_loop(numbers, k)}")
print(f"Comprehension: Rotate {numbers} by {k}: {rotate_list_comp(numbers, k)}")

# 11. Find missing number in sequence
print("\n11. Find Missing Number")
def find_missing_func(lst):
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

def find_missing_loop(lst):
    n = len(lst) + 1
    for i in range(1, n + 1):
        if i not in lst:
            return i
    return None

def find_missing_comp(lst):
    n = len(lst) + 1
    full_set = set(range(1, n + 1))
    list_set = set(lst)
    missing = list(full_set - list_set)
    return missing[0] if missing else None

numbers = [1, 2, 4, 5]  # Missing 3
print(f"Function: Missing number in {numbers}: {find_missing_func(numbers)}")
print(f"Loop: Missing number in {numbers}: {find_missing_loop(numbers)}")
print(f"Comprehension: Missing number in {numbers}: {find_missing_comp(numbers)}")

# 12. Check if list is palindrome
print("\n12. List Palindrome")
def is_palindrome_list_func(lst):
    return lst == lst[::-1]

def is_palindrome_list_loop(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_list_comp(lst):
    return all(lst[i] == lst[-(i+1)] for i in range(len(lst)//2))

numbers = [1, 2, 3, 2, 1]
print(f"Function: {numbers} is palindrome: {is_palindrome_list_func(numbers)}")
print(f"Loop: {numbers} is palindrome: {is_palindrome_list_loop(numbers)}")
print(f"Comprehension: {numbers} is palindrome: {is_palindrome_list_comp(numbers)}")

# 13. Flatten nested list
print("\n13. Flatten List")
def flatten_func(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_func(item))
        else:
            result.append(item)
    return result

def flatten_loop(lst):
    result = []
    stack = lst[:]
    while stack:
        item = stack.pop(0)
        if isinstance(item, list):
            stack = item + stack
        else:
            result.append(item)
    return result

def flatten_comp(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend([x for sublist in [item] for x in flatten_comp([sublist])])
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Function: Flatten {nested}: {flatten_func(nested)}")
print(f"Loop: Flatten {nested}: {flatten_loop(nested)}")
print(f"Comprehension: Flatten {nested}: {flatten_comp(nested)}")

# 14. Find pairs with given sum
print("\n14. Find Pairs with Sum")
def find_pairs_func(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

def find_pairs_loop(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

def find_pairs_comp(lst, target):
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst)) if lst[i] + lst[j] == target]

numbers = [1, 2, 3, 4, 5, 6]
target = 7
print(f"Function: Pairs with sum {target} in {numbers}: {find_pairs_func(numbers, target)}")
print(f"Loop: Pairs with sum {target} in {numbers}: {find_pairs_loop(numbers, target)}")
print(f"Comprehension: Pairs with sum {target} in {numbers}: {find_pairs_comp(numbers, target)}")

# 15. Count frequency of elements
print("\n15. Element Frequency")
def count_frequency_func(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

def count_frequency_loop(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def count_frequency_comp(lst):
    return {item: lst.count(item) for item in set(lst)}

numbers = [1, 2, 2, 3, 3, 3, 4]
print(f"Function: Frequency in {numbers}: {count_frequency_func(numbers)}")
print(f"Loop: Frequency in {numbers}: {count_frequency_loop(numbers)}")
print(f"Comprehension: Frequency in {numbers}: {count_frequency_comp(numbers)}")

# 16. Split list into chunks
print("\n16. Split into Chunks")
def split_chunks_func(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def split_chunks_loop(lst, size):
    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i+size])
    return chunks

def split_chunks_comp(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print(f"Function: Split {numbers} into chunks of {chunk_size}: {split_chunks_func(numbers, chunk_size)}")
print(f"Loop: Split {numbers} into chunks of {chunk_size}: {split_chunks_loop(numbers, chunk_size)}")
print(f"Comprehension: Split {numbers} into chunks of {chunk_size}: {split_chunks_comp(numbers, chunk_size)}")

# 17. Find common elements in multiple lists
print("\n17. Common Elements")
def common_elements_func(*lists):
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return list(common)

def common_elements_loop(*lists):
    if not lists:
        return []
    common = []
    for item in lists[0]:
        if all(item in lst for lst in lists[1:]) and item not in common:
            common.append(item)
    return common

def common_elements_comp(*lists):
    if not lists:
        return []
    return [item for item in lists[0] if all(item in lst for lst in lists[1:])]

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]
list3 = [3, 4, 5, 6]
print(f"Function: Common in {list1}, {list2}, {list3}: {common_elements_func(list1, list2, list3)}")
print(f"Loop: Common in {list1}, {list2}, {list3}: {common_elements_loop(list1, list2, list3)}")
print(f"Comprehension: Common in {list1}, {list2}, {list3}: {common_elements_comp(list1, list2, list3)}")

# 18. Remove element at specific index
print("\n18. Remove at Index")
def remove_at_index_func(lst, index):
    if 0 <= index < len(lst):
        return lst[:index] + lst[index+1:]
    return lst

def remove_at_index_loop(lst, index):
    if not (0 <= index < len(lst)):
        return lst
    result = []
    for i, item in enumerate(lst):
        if i != index:
            result.append(item)
    return result

def remove_at_index_comp(lst, index):
    return [item for i, item in enumerate(lst) if i != index] if 0 <= index < len(lst) else lst

numbers = [1, 2, 3, 4, 5]
index = 2
print(f"Function: Remove index {index} from {numbers}: {remove_at_index_func(numbers, index)}")
print(f"Loop: Remove index {index} from {numbers}: {remove_at_index_loop(numbers, index)}")
print(f"Comprehension: Remove index {index} from {numbers}: {remove_at_index_comp(numbers, index)}")

# 19. Find unique elements (elements that appear only once)
print("\n19. Find Unique Elements")
def find_unique_func(lst):
    from collections import Counter
    counts = Counter(lst)
    return [item for item, count in counts.items() if count == 1]

def find_unique_loop(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    unique = []
    for item, count in counts.items():
        if count == 1:
            unique.append(item)
    return unique

def find_unique_comp(lst):
    return [item for item in set(lst) if lst.count(item) == 1]

numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"Function: Unique elements in {numbers}: {find_unique_func(numbers)}")
print(f"Loop: Unique elements in {numbers}: {find_unique_loop(numbers)}")
print(f"Comprehension: Unique elements in {numbers}: {find_unique_comp(numbers)}")

# 20. Sort list of tuples by second element
print("\n20. Sort Tuples by Second Element")
def sort_tuples_func(lst):
    return sorted(lst, key=lambda x: x[1])

def sort_tuples_loop(lst):
    # Simple bubble sort implementation
    result = lst[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j][1] > result[j + 1][1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def sort_tuples_comp(lst):
    return sorted([item for item in lst], key=lambda x: x[1])

tuples = [('a', 3), ('b', 1), ('c', 2), ('d', 4)]
print(f"Function: Sort tuples by second element {tuples}: {sort_tuples_func(tuples)}")
print(f"Loop: Sort tuples by second element {tuples}: {sort_tuples_loop(tuples)}")
print(f"Comprehension: Sort tuples by second element {tuples}: {sort_tuples_comp(tuples)}")

print("\n" + "="*80)
print("INTERVIEW PROGRAMS COLLECTION COMPLETED!")
print("Total: 60 programs (20 each for Integer, String, List)")
print("Each with 3 different approaches: Functions, Loops, and Comprehensions")
print("="*80)