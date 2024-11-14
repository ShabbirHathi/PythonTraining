# Function Definition
def greet(name):
    """
    This function greets the user.
    """
    print("Hello,", name)


# Function Call
greet("Alice")  # Output: Hello, Alice


# Function Arguments
def add(x, y):
    return x + y


result = add(3, 4)  # Output: 7


# Default Arguments
def greet_default(name="World"):
    print("Hello,", name)


greet_default()  # Output: Hello, World
greet_default("Alice")  # Output: Hello, Alice


# Scope
x = 10  # Global variable

def func():
    y = 20  # Local variable
    print("Inside function:", y)

func()
print("Outside function:", x)

# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
