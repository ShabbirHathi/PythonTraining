#--------------------------------------------------- String ---------------------------------------------------
# A string in Python is a sequence of characters, enclosed within single ('') or double ("") quotes.

# String Basic:
# Example: Creating a string
name = "John Doe"

# Accessing characters in a string:
# Indexing: Accessing characters by their index
first_char = name[0]  # Accessing the first character
last_char = name[-1]  # Accessing the last character
print("First character:", first_char)
print("Last character:", last_char)

# String Concatenation:
# Example: Concatenating strings
greeting = "Hello"
message = greeting + ", " + name  # Hello, John Doe

# String Length:
# Example: Getting the length of a string using len() function
length = len(name)  # Returns the length of the string (8)

# String Methods:
# Example: Converting the case of a string using lower() and upper() methods
lower_case = name.lower()  # Converts the string to lowercase
upper_case = name.upper()  # Converts the string to uppercase

# Example: Checking if a string starts with or ends with a specific substring using startswith() and endswith() methods
starts_with_hello = message.startswith("Hello")  # Checks if the string starts with "Hello"
ends_with_doe = message.endswith("Doe")  # Checks if the string ends with "Doe"

# Example: Finding the index of a substring using find() method
index_of_space = name.find(" ")  # Returns the index of the first occurrence of space (3)

# Example: Splitting a string into a list of substrings using split() method
name_parts = name.split(" ")  # Splits the string at space and returns a list ['John', 'Doe']

# Example: Joining a list of strings into a single string using join() method
name = " ".join(name_parts)  # Joins the list elements with space as separator

# Example: Removing leading and trailing whitespace characters using strip() method
name_with_spaces = "   John Doe   "
stripped_name = name_with_spaces.strip()  # Removes leading and trailing spaces

# Example: Replacing occurrences of a substring with another substring using replace() method
formatted_message = message.replace("John", "Jane")  # Replaces "John" with "Jane"

# Example: Checking if all characters in a string are alphabetic or alphanumeric using isalpha() and isalnum() methods
is_alpha = name.isalpha()  # Checks if all characters are alphabetic
is_alphanumeric = name.isalnum()  # Checks if all characters are alphanumeric

# Example: Checking if all characters in a string are digits using isdigit() method
is_digit = "123".isdigit()  # Checks if all characters are digits

# Example: Checking if a string is titlecased using istitle() method
is_title = "Hello World".istitle()  # Checks if the string is titlecased

# Example: Formatting strings using format() method
formatted_string = "My name is {} and I am {} years old".format("John", 30)  # Formats the string with placeholders

# Example: Checking if a string contains a substring using 'in' keyword
contains_doe = "Doe" in name  # Checks if "Doe" is present in the string

# Example: Reversing a string using slicing
reversed_name = name[::-1]  # Reverses the string

# Example: Repeating a string using * operator
repeated_message = "Hello " * 3  # Repeats the string three times

# Example: Extracting a substring using slicing
substring = name[5:]  # Extracts substring starting from index 5 to the end

# Example: Checking if a string is empty using not operator and len() function
is_empty = not name  # Checks if the string is empty
is_non_empty = bool(name)  # Checks if the string is non-empty
