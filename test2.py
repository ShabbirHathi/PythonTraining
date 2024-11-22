# --------------------------- Operators ---------------------------
# 1) Arithmetic Operators: Given two numbers, num1 = 12 and num2 = 5, perform the following operations and print the result for each:

        # Addition
        # Subtraction
        # Multiplication
        # Division
        # Floor Division
        # Modulus
        
# 2) Comparison Operators: Write code to compare if num1 is greater than, less than, or equal to num2, and print statements to indicate the result.

# 3) Problem: Passcode Checker
    # Write a program that checks if a person can access a secure system based on given conditions:

    # Condition A: The person must know the correct username and password.
    # Condition B: The person have admin privileges or not?
    
# username = "shabbir"
# password = "shabbir123"
# admin = True

# name = input("Please enter username:")
# password1 = input("Please enter password:")

# if password1==password and name==username:
#     print("Login Successfull")
    
# elif
    
# --------------------------- Conditional Statement ---------------------------


# 1) Problem: Ticket Price Calculator (Easy)
    # A cinema charges different ticket prices based on the age of the customer:

    # Children under 5 get free entry.
    # Children between 5 and 12 years get a child discount (50% off).
    # Adults between 13 and 59 pay full price.
    # Senior citizens (60 and above) get a senior discount (30% off).
    
    # Write a program that calculates the ticket price based on the customer's age. Assume the full price is $20.
    
# 2) Problem: Online Shopping Discount (Intermediate)
    # An online store offers discounts based on the total purchase amount:

    # If the total is $100 or more, the customer gets a 10% discount.
    # If the total is $200 or more, the customer gets a 20% discount.
    # If the total is $500 or more, the customer gets a 30% discount.
    # If the total is below $100, there’s no discount.
    
    # Write a program that calculates the final price after applying any discount based on the purchase total.

# --------------------------- While Loops ---------------------------

# 1 ) Problem: Write a program that asks the user for a positive integer N and calculates the sum of the numbers from 1 to N using a loop.

N = int(input("Enter a positive integer: "))
sum = 0 
i = 1
while i <= N: 
    sum += i 
    i += 1
print(f"The sum of numbers from 1 to {N} is {sum}")


# 2) Problem: Countdown Timer
    # Create a program that acts as a countdown timer. The program should start from a given number (e.g., 10) and count down to 1, printing each number along the way. When it reaches 0, it should print "Time's up!".
N = int(input("Enter a positive integer: ")) 
for i in range(1, N + 1):
    
    print(i)
print("time's up")

# 3) Problem: Collecting User Names
    # Write a program that asks the user to enter names. Keep adding names to a list until the user types "stop". Then, print the list of names.
    
# --------------------------- For Loops ---------------------------


# 1) Problem: Print Elements of a List
    # Write a program that takes a list of numbers and prints each element in the list using a for loop.

# 2) Problem:  Sum of List Elements
    # Write a program that calculates and prints the sum of all elements in a list using a for loop.

N = int(input("Enter a positive integer: ")) 
sum = 0 
for i in range(1, N + 1):
    sum += i  
print(f"The sum of numbers from 1 to {N} is {sum}")

# -----------------------------------Mix Loop----------------------------------

# 1) Problem: You're at a store, and you want to calculate the total cost of the items in your shopping cart.

    # Write a program that calculates the total cost of items in a list. Each item is represented by its price. 
    
# 2) Problem: A simple chatbot that keeps asking questions until the user says "bye".

    # Write a program that simulates a simple chatbot. The program should keep asking the user "How are you?" until the user types "bye". Once the user types "bye", the program should end.
    
# 3) Problem: Count Vowels in a String
    # Write a program that counts and prints the number of vowels (a, e, i, o, u) in a string input from the user.