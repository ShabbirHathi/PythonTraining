#--------------------------------------------------- Operators ---------------------------------------------------
# In Python, operators are special symbols or keywords that are used to perform operations on variables and values.

# Arithmetic Operators:
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc.
# Addition
addition = 5 + 3        # Example: 5 + 3 = 8

# Subtraction
subtraction = 10 - 4    # Example: 10 - 4 = 6

# Multiplication
multiplication = 2 * 3  # Example: 2 * 3 = 6

# Division
division = 9 / 2        # Example: 9 / 2 = 4.5
# print("division",division)

# # Floor Division

floor_division = 9 // 2  # Example: 9 // 2 = 4 (Quotient of the division, rounded down to the nearest integer)
# print("floor_division",floor_division)


# # Modulus
modulus = 10 % 3       # Example: 10 % 3 = 1 (Remainder when 10 is divided by 3)
# print("modulus",modulus)


num = [ 1, 2, 3, 4, 5]

for i in num:
    if i % 2 == 0:
        print("even")



# # Exponentiation
exponentiation = 3 ** 5  # Example: 2 raised to the power of 3 = 8



# # Assignment Operators:
# # Assignment operators are used to assign values to variables.
x = 5                   # Assigns the value 5 to the variable x


# Comparison Operators:
# Comparison operators are used to compare values. They return True or False.

# Equal to
equal_to = (5 == 6)     # Example: 5 == 5 is True
# Example: 
password = "seb"
confirm_password = "Seb"
if password == confirm_password:
    print("Password is updated.")
else:
    print("Password didn't matched.")

# Not equal to
not_equal_to = (5 != 5) # Example: 5 != 3 is True
# print("not_equal_to: ",not_equal_to)
# Example:
age = 25
if age != 18:
    print("You are not 18 years old.")

# Greater than
greater_than = (5 > 3)  # Example: 5 > 3 is True
# print("greater_than:",greater_than)
# Example:
points = 60
passing_score = 70
if points > passing_score:
    print("Congratulations! You passed the exam.")

# Less than
less_than = (13 < 5)     # Example: 3 < 5 is True
# print("Less than: ", less_than)
# Example:
price = 50
budget = 30
if price < budget:
    print("You can afford this item.")
else:
    print("You can't afford this item.")



z=22
y=21
# Greater than or equal to
greater_than_or_equal_to = (z >= y)  # Example: 5 >= 5 is True
# print("greater_than_or_equal_to: ", greater_than_or_equal_to)
# Example:
current_age = 20
legal_age = 18
if current_age >= legal_age:
    print("You are legally allowed to vote.")


# Less than or equal to
less_than_or_equal_to = (z <= y)     # Example: 3 <= 5 is True
print("less_than_or_equal_to: ", less_than_or_equal_to)
# Example:
maximum_speed_limit = 60
current_speed = 60
if current_speed <= maximum_speed_limit:
    print("You are driving within the speed limit.")

# Logical Operators:
# Logical operators are used to combine conditional statements.


# Logical AND
logical_and = (True and False)  # Example: True and False is False
#Example :
username_db = "Seb"
password1 = "123"
username2 = "Seb"
password2 = "1234"



# condition-1 
# condition-2



if (username_db == username2) and (password1 == password2):
    #REDIRECT....
    print("welcome to the dashboard")
else:
    print("Please check the login credential")


# Logical OR
logical_or = (True or False)    # Example: True or False is True
#Example:
has_membership = False
is_student = False
if has_membership or is_student:
    print("You are eligible for a discount.")
else:
    print("Regular price applies.")


# Logical NOT
logical_not = not True    # Example: not True is False
# Example:
is_raining = False
if not is_raining:
    print("It's a sunny day, enjoy outdoors!")


# Membership Operators:
# Membership operators are used to test if a sequence is presented in an object.
# 1) in
membership_in = ("a" in "apple")  # Example: 'a' in 'apple' is True
# Example:
if "a" in "apple":
    print("The letter 'a' is present in the word 'apple'.")

#2) not in
membership_not_in = ("a" not in "apple")  # Example: 'z' not in 'apple' is True
# Example:
if "z" not in "apple":
    print("The letter 'z' is not present in the word 'apple'.")


# Identity Operators:
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
# 1) is
identity_is = (5 is 5)  # Example: 5 is 5 is True
#Example:
name1 = "alice"
name2 = "Alice"
if name1 is name2:
    print("name1 and name2 are the same object.")

# Another example for 'is'
a = [1, 2, 3]
b = a
if a is b:
    print("a and b refer to the same object in memory.")


#2) is not
identity_is_not = (5 is not 5)   # Example: 5 is not 6 is True

# Example
number1 = 10
number2 = 20
if number1 is not number2:
    print("number1 and number2 are different objects.")
