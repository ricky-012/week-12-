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

#SETS AND TUPLES
#sets and tuples are also part of the collections
#family in python
set1 = {1, 2, 3, 4, 5}
set2 = {"apple", "banana", "cherry"}
print(set1)
print(set2)
print(type(set1))

sets_with_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(sets_with_duplicates)

print(3 in set1)
print(6 in set1)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = {"apple", "banana", "cherry"}
print(tuple1)
print(tuple2)
print(type(tuple1))
# tuples cannot be changed after
social_security_number = (123444, 4444445, 5676789)

#why use a list?
#instead of creating seperate variables
# for each item, we can store them in a list
# this makes our job easier
# this makes managing the complexity of our code easier
# when we need to manage multiple list of items
# performance task answer
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
list_of_food = ['tacos', 'pizza', 'seafood', 'burger', 'hotdog']
print(list_of_food)
# Print the second and last item.
print(list_of_food[1])
print(list_of_food[-1])

# Add a new item using .append().
list_of_food.append('fries')
# Remove the first item using .pop(0).
popped_item = list_of_food.pop()
print(popped_item)
print(list_of_food)
# Reverse your list using .reverse().
list_of_food.reverse()
print(list_of_food)
# Create a list of 3 lists (matrix), and access the middle element.\