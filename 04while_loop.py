#--------------------------------------------------- While Loop ---------------------------------------------------
# The while loop in Python is used to repeatedly execute a block of statements as long as the condition is True.

# While Loop Logic Building:
# Example: Printing numbers from 1 to 5 using a while loop
num = 1
while num <= 8:
    print("inside  the loop")
    print("num:",num)
    num += 1
    # num = num + 1
print("out of the loop")


# Series Based Question:
# Example: Sum of numbers from 1 to 10 using a while loop
total = 0
num = 1
while num <= 1000000:
    total += num
    num += 1
print("Sum of numbers from 1 to 1000000 =", total)

limit_token = 10
user_used_token = 1
while user_used_token <= limit_token:
    # chatting
    # print(input("Enter message:"))
    print("user_used_token:",user_used_token)
    user_used_token +=1
    
    print("doing chatting with AI")

print("Token limit over!")
    
# Break Statement:
# Example: Exiting the loop when a specific condition is met
num = 1
while num <= 10:
    
    if num == 7:
        print("num is 7...")
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
     
fruits = ["apple", "banana", "cherry", "apple", "banana", "cherry",]
for fruit in fruits:
    if fruit=="cherry":
        print("continue")
        continue
    print(fruit)  # Prints each fruit in the list
    
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

