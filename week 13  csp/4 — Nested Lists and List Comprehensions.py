
list1 = [1, 2, 3]
print(list1[-1])  # output: 1
list2 = [4, 5, 6]
print(list2[0]) # output: 4
# nested list
nested_list = [list1, list2]
print(nested_list[0]) # 1, 2, 3
print(nested_list[1]) # 4, 5, 6
print(nested_list[0][1]) # 2
print(nested_list[1][1])
print(nested_list[1][0])


fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]
groceries = [fruits, vegetables, meats]
print(groceries[2][-1]) # turkey
print(groceries[1][1])
print(groceries[0][2])

for collection in groceries:
    for food in collection: 
        print(food, end=" ")
    print()


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()



# nested loops
# for i in range(1,10001):
#     for j in range(1,10001):
#         if i > 0 and j > 0:
#             for k in range(1,10001):
#                 print("The number is ", i, j, k)
# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix[0])
print(matrix[2][1])
sum_list = [row[-1] for row in matrix]
print(sum_list)

# print(matrix[1][2])    # 6

# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.

# Print the second item from the third list.

# Use a list comprehension to extract the last item from each sub-list.

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range(1,11)]
print(squares)