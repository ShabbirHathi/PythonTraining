#--------------------------------------------------- While Loop ---------------------------------------------------
# The while loop in Python is used to repeatedly execute a block of statements as long as the condition is True.

# While Loop Logic Building:
# Example: Printing numbers from 1 to 5 using a while loop
num = 1
while num <= 5:
    print(num)
    num += 1

# Series Based Question:
# Example: Sum of numbers from 1 to 10 using a while loop
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print("Sum of numbers from 1 to 10:", total)

# Break Statement:
# Example: Exiting the loop when a specific condition is met
num = 1
while num <= 10:
    if num == 5:
        # print("num is 5...")
        break  # Exit the loop if num equals 5
    print(num)
    num = num + 1

# Continue Statement:
# Example: Skipping even numbers using continue statement
num = 1
while num <= 10:
    if num % 2 == 0:
        num += 1
        continue  # Skip the rest of the loop body for even numbers
    print(num)
    num += 1

# Pass Statement:
# Example: Using pass statement as a placeholder
num = 1
while num <= 5:
    if num == 3:
        pass  # Placeholder, do nothing
    else:
        print(num)
    num += 1

# Nested While Loop:
# Example: Printing a pattern using nested while loops
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()  # Move to the next line after printing each row
    row += 1

# Loop Else:
# The else block is executed when the while condition becomes False.
num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("While loop finished without breaking")

