# Week 2 - 2.3.2 Using comparison operators

# Comparison operators are used to compare values and return a boolean result (True or False).

# Comparing operands within `if` statements

"""
Comparison Operators in Python

| Operator | Description                                                                                  |
|----------|----------------------------------------------------------------------------------------------|
| <        | True if the value of the left operand is less than the value of the right operand.           |
| <=       | True if the value of the left operand is less than or equal to the value of the right operand|
| >        | True if the value of the left operand is greater than the value of the right operand.        |
| >=       | True if the value of the left operand is greater than or equal to the right operand.         |
| !=       | True if the value of the two operands are not equal.                                         |
| ==       | True if the values of the two operands are equal.                                            |
| in       | True if the left operand is a member of the right operand (e.g., in a list).                 |
| not in   | True if the left operand is not a member of the right operand (e.g., in a list).             |
| is       | True if the left operand is the same object as the right operand.                            |
| is not   | True if the left operand is not the same object as the right operand.                        |

NOTE:
`is` and `is not` reads as the same as `==` and `!=` but are used for equality between objects.
"""


## EG.1
# import sys
# # Ask user to enter there age:
# user_age = int(input("Please enter your age: "))
# # user_age = int(sys.stdin.readline().strip())
# # Check if the user is old enough to enter the nightclub:
# if user_age >= 18:
#     # print("Access into the nightclub has been granted")
#     sys.stdout.write("Access into the nightclub has been granted" + "\n")
# if user_age < 18:
#     sys.stdout.write("Access into the nightclub has been denied" + "\n")

import sys


user_age = int(input("Welcome to the new Age Restriction Laws enforced by the United States." + "\n" + "Please enter your age: "))

if user_age < 16:
    sys.stdout.write("Sorry you can't even have Facebook" + "\n")
if user_age >= 16:
    if user_age < 18:
        sys.stdout.write("You can have Facebook but you can't have Instagram - Too many bikini photos" + "\n")
if user_age >= 18:
    sys.stdout.write("You can have Facebook, Instagram and OnlyFans" + "\n")
