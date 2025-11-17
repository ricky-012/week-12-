# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# collections are used to store multiple items in a single variable
# lists are ordeed collections of items
# lists are mutable, meaning you can change their content
# lists are created using square brackets []

list_of_fruits = ['apple', 'banana', 'cherry', 'date']
print(list_of_fruits)
print(type(list_of_fruits))
print(list_of_fruits[0])
print(list_of_fruits[1])
print(list_of_fruits[-1])
print(list_of_fruits[1:3])
list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1])
list_of_fruits.append('Mango')
list_of_fruits.append('blueberry')
print(list_of_fruits)
popped_item = list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)
list_of_fruits.insert(1, 'orange')
print(list_of_fruits)
list_of_fruits.remove('banana')
list_of_fruits.insert(3, 'peach')
list_of_fruits.sort()
print(list_of_fruits)
list_of_items = list(range(1001, 2001))
print(list_of_items)
print(len(list_of_items))
# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.\