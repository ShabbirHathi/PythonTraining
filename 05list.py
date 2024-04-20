#--------------------------------------------------- List ---------------------------------------------------
# A list in Python is a collection of items, which can be of different data types, enclosed within square brackets [].

# List Basic:
# Example: Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Accessing elements of a list:
# Indexing: Accessing elements by their index
first_element = numbers[0]  # Accessing the first element
last_element = numbers[-1]  # Accessing the last element
print("First element:", first_element)
print("Last element:", last_element)

# List Comprehensions / Slicing:
# List comprehensions provide a concise way to create lists.
# Example: Creating a list of squares of numbers from 1 to 5 using list comprehension
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# Slicing: Extracting a portion of a list
# Syntax: list[start_index:end_index:step]
# Example: Extracting elements from index 1 to 3
subset = numbers[1:4]  # [2, 3, 4]

# List Methods:
# Example: Adding an element to the end of the list using append() method
numbers.append(6)  # [1, 2, 3, 4, 5, 6]

# Example: Inserting an element at a specific position using insert() method
numbers.insert(2, 7)  # [1, 2, 7, 3, 4, 5, 6]

# Example: Removing an element by its value using remove() method
numbers.remove(3)  # [1, 2, 7, 4, 5, 6]

# Example: Removing an element by its index using pop() method
popped_element = numbers.pop(2)  # Removes and returns the element at index 2 (7)
# numbers: [1, 2, 4, 5, 6]

# Example: Finding the index of an element using index() method
index_of_4 = numbers.index(4)  # Returns the index of the first occurrence of 4 (2)

# Example: Reversing the elements of the list using reverse() method
numbers.reverse()  # [6, 5, 4, 2, 1]

# Example: Sorting the elements of the list using sort() method
numbers.sort()  # [1, 2, 4, 5, 6]

# Example: Counting the occurrences of an element using count() method
count_of_5 = numbers.count(5)  # Returns the count of occurrences of 5 (1)

# Example: Clearing all elements from the list using clear() method
numbers.clear()  # []

# Example: Extending the list by appending elements from another list using extend() method
numbers.extend([7, 8, 9])  # [7, 8, 9]

# Example: Checking if an element exists in the list using 'in' keyword
if 7 in numbers:
    print("7 exists in the list")

# Example: Getting the length of the list using len() function
length = len(numbers)  # Returns the length of the list (3)
