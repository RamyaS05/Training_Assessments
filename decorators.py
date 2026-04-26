#section 1: Basics of Decorators
#t1: Use decorator to print a message.
def my_deco(func):
    def wrapper():
        print("Function started.")
        func()
    return wrapper
@my_deco
def say_hello():
    print("Hello\n")
say_hello()


#t2: Modify the decorator to print a message and aaplying decorator to a function.
def my_deco(func):
    def wrapper():
        print("Function started.")
        func()
        print("Function Ended.\n")
    return wrapper
    
@my_deco
def say_hello():
    print("Hello")
say_hello()


#t3
def my_deco(func):
    def wrapper():
        print("Function started.")
        func()
        print("Function Ended.\n")
    return wrapper
    
@my_deco
def say_hello():
    print("Hello World")
say_hello()


#section 2: Decorator with Arguments
#t4: Decorator that takes arguments and applying it to a function using *args and **kwargs.
def my_decor(func):
    def wrapper(*args, **kwargs):
        print("Before Execution.")
        result = func(*args, **kwargs)
        print("Arguments Recieved.")
        print("After Execution.\n")
    return wrapper
@my_decor
def add(a, b):
    return a + b
result = add(2, 3)


#t5
def my_decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
@my_decor
def add(a, b):
    return a + b
result = add(2, 3)
print("\nResult: ", result)

#t6
def my_decor(func):
    def wrapper(*args, **kwargs):
        print("\nBefore execution.")
        result = func(*args, **kwargs)
        print("After execution.")
        return result
    return wrapper
@my_decor
def add(a, b):
    return a + b
result = add(2, 3)
print("Result: ", result)

#section 3: Multiple Decorators
#t7: Create 2 decorators one to print a message Decorator1 and another as Decorator2 and apply both function.
def my_decorator1(func):
    def wrapper():
        print("\nDecorator 1: Function started.")
        func()
        print("Decorator 1: Function ended.")
    return wrapper 
def my_decorator2(func):
    def wrapper():
        print("Decorator 2: Function started.")
        func()
        print("Decorator 2: Function ended.")
    return wrapper
@my_decorator1
@my_decorator2
def new():
    print("Function executing")
new()
print("\n")

#Section 4: Decorators with Parameters
#t8 & t9:Create a decorator that takes parameter and apply it to a function.
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def print_text(text):
    print(text)
print_text("python")
print('\n')

#Section 5: Real-world use cases
#t10:create a decorator that logs function name before execution 
def log_name(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG]: Executing function: {func.__name__} ")
        return func(*args, **kwargs)
    return wrapper

@log_name
def greet():
    print("Hello\n")
greet()

#t11: create a decorator that measures execution time of a function 

import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time for {func.__name__}: {end - start:.4f} seconds\n")
        return result
    return wrapper

@measure_time
def computation():
    time.sleep(1.5)  # Simulating a delay
    return "Done!"

computation()

#t12:create a decorator that checks if a user is "admin" before running a function
def admin_required(func):
    def wrapper(user_role, *args, **kwargs):
        if user_role.lower() == "admin":
            print("Access Granted")
            print("Welcome Admin")
            return func(user_role, *args, **kwargs)
        else:
            print("Access Denied")
            return None
    return wrapper

@admin_required
def view_dashboard(user_role):
    pass

print("User 1 Attempt:")
view_dashboard("guest")

print("\nUser 2 Attempt:")
view_dashboard("admin")
print("\n")


#section6: functiontools.wraps
#t13 & t14: Create a decorator that uses functools.wraps to preserve the original function's metadata
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(f"Function Name: {add.__name__}")
print(f"Docstring: {add.__doc__}\n")


from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(f"Function Name: {add.__name__}")
print(f"Docstring: {add.__doc__}")
print("result:",add(5,1))