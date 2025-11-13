# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:
#score/grade calculator
grade = int(input("What is your score?"))
if 90 <= grade <= 100:
    print("You got an A!")
elif 80 <= grade <= 89:
    print("You got a B!")
elif 70 <= grade <= 79:
    print("You got a C.")
elif 60 <= grade <= 69:
    print("You got a D.")
elif grade <= 59:
    print("You got a F.")

#if score 90-100 print A

#if score 80-89 print B

#if score 70-79 print C

#if score below 70, F



# Write an expression that checks if a number is between 50 and 100 (inclusive).

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:

