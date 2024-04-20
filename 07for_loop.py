#--------------------------------------------------- For Loop ---------------------------------------------------
# The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects.

# Range Function:
# The range function generates a sequence of numbers.
# Syntax: range(start, stop, step)
# Example: Generating numbers from 0 to 4
for num in range(5):
    print(num)  # Prints numbers from 0 to 4

# For Loop:
# Example: Iterating over elements of a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Prints each fruit in the list

# Nested For Loops:
# Example: Multiplication table using nested for loops
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print()  # Prints a blank line after each row of the table

# Pattern Based Questions:
# Example: Printing a triangle pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  # Moves to the next line after printing each row

# Loop Else:
# The else block is executed when the loop completes normally (i.e., without encountering a break statement).
# Example: Finding prime numbers between 1 and 10 using a for loop
for num in range(2, 11):
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")

# Note: In the example above, the else block is executed for each number if the inner loop doesn't encounter a break statement.