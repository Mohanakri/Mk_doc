# Python Functions, Generators, Modules & Packages - Complete Guide

## 📚 Table of Contents

### Function Questions (Questions 1-17)
### Generator Questions (Questions 18-25)
### Module & Package Questions (Questions 26-40)
### Advanced Concepts (Questions 41-50)

---

## 🔧 Function Questions

??? question "Q1: How do you define a function in Python?"

    ```python
    def function_name(parameters):
        """Optional docstring"""
        # Function body
        return value  # Optional
    
    # Example
    def greet(name):
        """Greets a person with their name"""
        return f"Hello, {name}!"
    
    print(greet("Alice"))  # Output: Hello, Alice!
    
    # Function with multiple parameters
    def calculate_area(length, width, height=None):
        """Calculate area or volume"""
        if height:
            return length * width * height  # Volume
        return length * width  # Area
    
    print(calculate_area(5, 3))     # Output: 15
    print(calculate_area(5, 3, 2))  # Output: 30
    ```

??? question "Q2: What are the different types of function arguments?"

    ```python
    def example_function(pos_arg, default_arg="default", *args, **kwargs):
        """
        pos_arg: Positional argument (required)
        default_arg: Default argument (optional)
        *args: Variable positional arguments (tuple)
        **kwargs: Variable keyword arguments (dictionary)
        """
        print(f"Positional: {pos_arg}")
        print(f"Default: {default_arg}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
    
    # Usage examples
    example_function("required")
    # Output: Positional: required, Default: default, Args: (), Kwargs: {}
    
    example_function("required", "custom", 1, 2, 3, key="value")
    # Output: Positional: required, Default: custom, Args: (1, 2, 3), Kwargs: {'key': 'value'}
    
    # Keyword-only arguments (Python 3+)
    def keyword_only(a, b, *, c, d=10):
        return a + b + c + d
    
    print(keyword_only(1, 2, c=3))     # Output: 16
    # keyword_only(1, 2, 3)  # Error: c must be keyword argument
    ```

??? question "Q3: How do you use lambda functions effectively?"

    ```python
    # Basic lambda syntax
    square = lambda x: x ** 2
    print(square(5))  # Output: 25
    
    # Lambda with multiple arguments
    add = lambda x, y: x + y
    print(add(3, 4))  # Output: 7
    
    # Lambda with conditional logic
    max_val = lambda a, b: a if a > b else b
    print(max_val(10, 5))  # Output: 10
    
    # Lambda with higher-order functions
    numbers = [1, 2, 3, 4, 5, 6]
    
    # With map
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16, 25, 36]
    
    # With filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4, 6]
    
    # With sorted
    students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
    sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
    print(sorted_by_grade)  # Output: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
    ```

??? question "Q4: What is function scope and the LEGB rule?"

    ```python
    # Global scope
    global_var = "I'm global"
    
    def outer_function():
        # Enclosing scope
        enclosing_var = "I'm in enclosing scope"
        
        def inner_function():
            # Local scope
            local_var = "I'm local"
            print(f"Local: {local_var}")
            print(f"Enclosing: {enclosing_var}")
            print(f"Global: {global_var}")
            # print(f"Built-in: {len}")  # Built-in scope
        
        inner_function()
        
        # Modifying enclosing scope
        def modify_enclosing():
            nonlocal enclosing_var
            enclosing_var = "Modified enclosing"
        
        modify_enclosing()
        print(f"After modification: {enclosing_var}")
    
    outer_function()
    
    # Global vs local
    x = "global x"
    
    def test_scope():
        x = "local x"  # Creates new local variable
        print(f"Inside function: {x}")
    
    test_scope()
    print(f"Outside function: {x}")
    
    # Using global keyword
    count = 0
    
    def increment():
        global count
        count += 1
        return count
    
    print(increment())  # Output: 1
    print(increment())  # Output: 2
    ```

??? question "Q5: How do decorators work in Python?"

    ```python
    # Basic decorator
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Before function execution")
            result = func(*args, **kwargs)
            print("After function execution")
            return result
        return wrapper
    
    # Using decorator with @ syntax
    @my_decorator
    def greet(name):
        print(f"Hello, {name}!")
        return f"Greeting for {name}"
    
    result = greet("Alice")
    # Output: Before function execution
    #         Hello, Alice!
    #         After function execution
    
    # Decorator with parameters
    def repeat(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    
    @repeat(3)
    def say_hello():
        print("Hello!")
    
    say_hello()  # Prints "Hello!" 3 times
    
    # Timing decorator
    import time
    import functools
    
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.4f} seconds")
            return result
        return wrapper
    
    @timer
    def slow_function():
        time.sleep(1)
        return "Done"
    
    slow_function()  # Output: slow_function took 1.0001 seconds
    ```

??? question "Q6: What are closures and how are they used?"

    ```python
    # Basic closure
    def outer_function(x):
        # This variable is captured by the closure
        outer_var = x
        
        def inner_function(y):
            # Inner function has access to outer_var
            return outer_var + y
        
        return inner_function
    
    # Creating closures
    add_10 = outer_function(10)
    add_20 = outer_function(20)
    
    print(add_10(5))  # Output: 15
    print(add_20(5))  # Output: 25
    
    # Practical example: Counter closure
    def make_counter(start=0, step=1):
        count = start
        
        def counter():
            nonlocal count
            count += step
            return count
        
        def reset():
            nonlocal count
            count = start
        
        def get_current():
            return count
        
        # Return multiple functions
        counter.reset = reset
        counter.current = get_current
        return counter
    
    counter1 = make_counter()
    counter2 = make_counter(100, 5)
    
    print(counter1())  # Output: 1
    print(counter1())  # Output: 2
    print(counter2())  # Output: 105
    print(counter1.current())  # Output: 2
    
    # Closure with configuration
    def create_multiplier(factor):
        def multiply(number):
            return number * factor
        return multiply
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(double(5))  # Output: 10
    print(triple(5))  # Output: 15
    ```

??? question "Q7: How do you use *args and **kwargs?"

    ```python
    # *args - variable positional arguments
    def sum_all(*args):
        return sum(args)
    
    print(sum_all(1, 2, 3))        # Output: 6
    print(sum_all(1, 2, 3, 4, 5))  # Output: 15
    
    # **kwargs - variable keyword arguments
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    print_info(name="Alice", age=30, city="New York")
    # Output: name: Alice
    #         age: 30
    #         city: New York
    
    # Combining all argument types
    def complex_function(pos_arg, *args, default_arg="default", **kwargs):
        print(f"Positional: {pos_arg}")
        print(f"Args: {args}")
        print(f"Default: {default_arg}")
        print(f"Kwargs: {kwargs}")
    
    complex_function("first", "second", "third", default_arg="custom", key="value")
    
    # Unpacking arguments
    def greet(first_name, last_name, age):
        return f"Hello {first_name} {last_name}, you are {age} years old"
    
    # Unpacking list/tuple
    person_info = ["John", "Doe", 25]
    print(greet(*person_info))  # Output: Hello John Doe, you are 25 years old
    
    # Unpacking dictionary
    person_dict = {"first_name": "Jane", "last_name": "Smith", "age": 30}
    print(greet(**person_dict))  # Output: Hello Jane Smith, you are 30 years old
    ```

??? question "Q8: How do you create and use higher-order functions?"

    ```python
    # Function that takes another function as argument
    def apply_operation(numbers, operation):
        """Apply operation to each number in the list"""
        return [operation(num) for num in numbers]
    
    # Function that returns another function
    def create_multiplier(factor):
        """Create a function that multiplies by factor"""
        def multiplier(x):
            return x * factor
        return multiplier
    
    # Usage examples
    numbers = [1, 2, 3, 4, 5]
    
    # Using built-in functions
    squared = apply_operation(numbers, lambda x: x**2)
    print(squared)  # Output: [1, 4, 9, 16, 25]
    
    # Using created functions
    double = create_multiplier(2)
    doubled = apply_operation(numbers, double)
    print(doubled)  # Output: [2, 4, 6, 8, 10]
    
    # Function composition
    def compose(f, g):
        """Compose two functions: f(g(x))"""
        return lambda x: f(g(x))
    
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    
    # Compose functions
    composed = compose(multiply_by_two, add_one)
    print(composed(5))  # Output: 12 (5+1)*2
    
    # Advanced: Function pipeline
    def pipeline(*functions):
        """Create a pipeline of functions"""
        def apply_pipeline(value):
            for func in functions:
                value = func(value)
            return value
        return apply_pipeline
    
    # Create pipeline
    process = pipeline(
        lambda x: x * 2,      # Double
        lambda x: x + 10,     # Add 10
        lambda x: x ** 2      # Square
    )
    
    print(process(3))  # Output: 256 ((3*2+10)^2)
    ```

??? question "Q9: How do you use functools for function utilities?"

    ```python
    from functools import partial, reduce, wraps, lru_cache, singledispatch
    
    # partial - create partial functions
    def multiply(x, y, z):
        return x * y * z
    
    # Create partial function
    double = partial(multiply, 2)  # Fix x=2
    triple = partial(multiply, 3)  # Fix x=3
    
    print(double(4, 5))  # Output: 40 (2*4*5)
    print(triple(4, 5))  # Output: 60 (3*4*5)
    
    # reduce - apply function cumulatively
    numbers = [1, 2, 3, 4, 5]
    sum_all = reduce(lambda x, y: x + y, numbers)
    product_all = reduce(lambda x, y: x * y, numbers)
    print(sum_all)     # Output: 15
    print(product_all) # Output: 120
    
    # wraps - preserve function metadata in decorators
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    @my_decorator
    def example_function():
        """This is an example function"""
        pass
    
    print(example_function.__name__)  # Output: example_function
    print(example_function.__doc__)   # Output: This is an example function
    
    # lru_cache - memoization decorator
    @lru_cache(maxsize=128)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(fibonacci(10))  # Output: 55 (cached for efficiency)
    print(fibonacci.cache_info())  # Show cache statistics
    
    # singledispatch - function overloading
    @singledispatch
    def process_data(arg):
        print(f"Processing generic data: {arg}")
    
    @process_data.register
    def _(arg: int):
        print(f"Processing integer: {arg * 2}")
    
    @process_data.register
    def _(arg: str):
        print(f"Processing string: {arg.upper()}")
    
    @process_data.register
    def _(arg: list):
        print(f"Processing list of {len(arg)} items")
    
    process_data(42)        # Output: Processing integer: 84
    process_data("hello")   # Output: Processing string: HELLO
    process_data([1,2,3])   # Output: Processing list of 3 items
    ```

??? question "Q10: What are pure functions and why are they important?"

    ```python
    # Pure function - always returns same output for same input, no side effects
    def pure_add(a, b):
        """Pure function - same input always gives same output"""
        return a + b
    
    # Impure function - has side effects
    counter = 0
    def impure_increment():
        """Impure function - modifies global state"""
        global counter
        counter += 1
        return counter
    
    # Pure function benefits
    def calculate_discount(price, discount_percent):
        """Pure function for calculating discount"""
        return price * (1 - discount_percent / 100)
    
    # Easy