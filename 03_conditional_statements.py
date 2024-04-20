#--------------------------------------------------- Conditional Statements ---------------------------------------------------
# Conditional statements are used to make decisions in a program based on certain conditions.

# If Statement:
# The if statement is used to execute a block of code if a specified condition is True.
x = 5
if x > 0:
    print("x is positive")

# If-Else Statement:
# The if-else statement is used to execute one block of code if the condition is True, and another block if the condition is False.
z = 0
if z > 0:
    print("z is positive")
else:
    print("z is non-positive")

# Elif Statement:
# The elif statement allows you to check multiple conditions. It is short for "else if".
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("D")

# Ternary Operator:
# Ternary operator provides a shorter syntax for if-else statements.
# Syntax: value_if_true if condition else value_if_false
a = 10
b = 20
max_value = a if a > b else b
print("The maximum value is:", max_value)
