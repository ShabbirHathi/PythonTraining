#--------------------------------------------------- Variable ---------------------------------------------------
# A variable in programming is a named storage location in a computer's memory where data can be stored and retrieved during the execution of a program. Variables are used to store different types of information such as numbers, strings, lists, and more.


#--------------------------------------------------- Data Types ---------------------------------------------------

# Integer (int): An integer is a whole number without decimal points. Declared using the int keyword.
integer = 1             #Example: 1.

# Float (float): A float is a decimal number. Declared using the float keyword.
float1 = 2.1            # Example: 2.1.

# String (str): A string is a sequence of characters, enclosed within single (') or double (") quotes. Declared using the str keyword.
string = "python"       # Example: "python".

# Boolean (bool): A boolean represents one of two values: True or False.  Declared using the bool keyword.
boolean_True = True     # Example: True.
boolean_False = False   # Example: False.


None_var = None         # This represents absence of value or null

# List (list): A list is an ordered collection of items, enclosed within square brackets [ ]. Declared using the list keyword or square brackets [ ].
list_var = [ ]        # Example: [] (an empty list).

# Set (set): A set is an unordered collection of unique items, enclosed within curly braces { }. Declared using the set keyword or curly braces { }.
set_var = ( )            # Example: () (an empty set). 

# Dictionary (dict): A dictionary is a collection of key-value pairs, enclosed within curly braces { }. Declared using the dict keyword or curly braces { }.
dict_var = {"key": "values"}   # Example: {"key": "values"}.


list_into_set = ( [1,2,3,("set")], "test", )


student_data = {
    "set data": list_into_set,
    "name":"shabbir",
    "roll no.":21,
    "contact":"87473"
}

print(student_data)