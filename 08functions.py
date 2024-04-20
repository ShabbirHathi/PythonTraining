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


# Docstring
print(greet.__doc__)  # Output: This function greets the user.


# Scope
x = 10  # Global variable

def func():
    y = 20  # Local variable
    print("Inside function:", y)

func()
print("Outside function:", x)


# Lambda Function
add_lambda = lambda x, y: x + y
print(add_lambda(2, 3))  # Output: 5


# Map Function
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]


# Filter Function
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]


# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120


# Higher-Order Function
def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

result = apply_operation(add, 3, 4)  # Output: 7


# Loop Else
for num in range(2, 11):
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
