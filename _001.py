#---------------------------------------------- Type conversion ----------------------------------------------
#---------------------------------------------- Type conversion ----------------------------------------------







# Python converts integer to float before addition
# x = 5    # integer
# y = 2.5  # float
# z = x + y  
# print("x-Type: ",type(x)) 
# print("y-Type: ",type(y)) 
# print("z-Type: ",type(z)) 
# print(z) 

# # Convert string to integer
# x = 123
# y = (123)
# print("x...",x,type(x))
# print("y...",y, type(y))

# print(x+y)
# x = True
# print("Boolean", x,type(x))

x = 1
y = 2.3
#-----------------------------
# Values considered False
List_variable = [ 1, 2.1 , "3", "Shabbir"] # list

print(List_variable,"type", type(List_variable))
dict_variable = { }
set_variable = ( )



# Values considered True
true_values = []
false_values = []
values = [0, 0.0, '', None, [], {},1, -1, 3.14, 'Hello', [1, 2, 3], {'key': 'value'}]

for i in values:
    print("Data: ",i)

    if i:
        false_values.append(i)
    else:
        true_values.append(i)

# print("True Values:", true_values)
# print("Data Type of True Values:", type(true_values))


#---------------------------------------------- Operators ----------------------------------------------
#---------------------------------------------- Operators ----------------------------------------------
x = 10
y = 3

# Arithmetic Operators
# + (Addition)
# - (Subtraction)
# * (Multiplication)
# / (Division)
# % (Modulus)
# ** (Exponentiation)
# // (Floor Division)

# print(x + y)  # Output: 13
# print(x / y)  # Output: 3.3333333333333335

# Comparison Operators
# == (Equal to)
# != (Not equal to)
# < (Less than)
# > (Greater than)
# <= (Less than or equal to)
# >= (Greater than or equal to)
# print(x > y)  # Output: True
# print(x == y) # Output: False

# Logical Operators
# and (Logical AND)
# or (Logical OR)
# not (Logical NOT)
a = True
b = False
# print(a and b)  # Output: False
# print(a or b)   # Output: True

# Assignment Operators
# = (Assignment)
# += (Addition assignment)
# -= (Subtraction assignment)
# *= (Multiplication assignment)
# /= (Division assignment)
# %= (Modulus assignment)
# **= (Exponentiation assignment)
# //= (Floor division assignment)
z = 5
z += 2
# print(z)  # Output: 7

# Membership Operators
# in (True if value/variable is found in the sequence)
# not in (True if value/variable is not found in the sequence)
my_list = [1, 2, 3, 4]
# print(2 in my_list)  # Output: True

# Identity Operators
# is (True if the operands are identical)
# is not (True if the operands are not identical)
c = 10
d = 10
# print(c is d)  # Output: True
