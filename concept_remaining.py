# Ternary Operator:
# Ternary operator provides a shorter syntax for if-else statements.
# Syntax: value_if_true if condition else value_if_false
a = 10
b = 20
max_value = a if a > b else b
print("The maximum value is:", max_value)

# List Comprehensions:
# List comprehensions provide a concise way to create lists.
# Example: Creating a list of squares of numbers from 1 to 5 using list comprehension
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]


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



# Function Definition
def greet(name):
    """
    This function greets the user.
    """
    print("Hello,", name)


# Function Call
greet("Alice")  # Output: Hello, Alice


# Docstring
print(greet.__doc__)  # Output: This function greets the user.

