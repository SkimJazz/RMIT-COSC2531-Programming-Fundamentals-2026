import sys
# Week 2 - 2.3.1 Using logical operators: If
# If statements allow us to execute a block of code only if a certain condition is true.


# ## EG.1 - Basic If statement

# # Define a variable to represent whether the user is commuting or not set to True
# isCommuting = True
## If the user is commuting, print "You are employed"
# if isCommuting:
#     sys.stdout.write("You are employed" + "\n")


# ## EG.1a - What happens if the condition is false?

# # Define a variable to represent whether the user is commuting or not set to False
# isCommuting = False
# # If the user is commuting, print "You are employed"
# if isCommuting:
#     sys.stdout.write("You are employed" + "\n")


# ## EG.2 - If statement with an `and` operator

# Define a variable to represent whether the user is commuting, set to True
# isCommuting = True
# # Define a variable to represent whether there is heavy traffic, set to True
# isHeavyTraffic = True
# # If the user is commuting and there is heavy traffic, print "You are going to be late for work"
# if isCommuting and isHeavyTraffic:
#     sys.stdout.write("You are going to be late for work" + "\n")



# ## EG.3 - If statement with an `or` operator

## Define a variable to represent whether the user is commuting, set to False
isCommuting = False
## Define a variable to represent whether there is heavy traffic, set to True
isHeavyTraffic = True
## If user is commuting and there is heavy traffic, print "You are going to be late for work"
if isCommuting and isHeavyTraffic:
    sys.stdout.write("You are going to be late for work. " + "\n")
## If user is commuting or there is heavy traffic, print "You are in a car. "
if isCommuting or isHeavyTraffic:
    sys.stdout.write("You are in a car yet? " + "\n")
## If user is not commuting, print "You are not commuting. "
if not isCommuting:
    sys.stdout.write("You are not commuting. " + "\n")

"""
Logic Table for If Statements:

Variables:
- isCommuting: True or False
- isHeavyTraffic: True or False

If Statements:
1. if isCommuting and isHeavyTraffic:
       sys.stdout.write("You are going to be late for work. \n")
2. if isCommuting or isHeavyTraffic:
       sys.stdout.write("You are in a car yet? \n")
3. if not isCommuting:
       sys.stdout.write("You are not commuting. \n")

Combinations and Outputs:

| isCommuting | isHeavyTraffic| 1st if | 2nd if | 3rd if | Output(s)                                      |
|-------------|---------------|--------|--------|--------|------------------------------------------------|
|    True     |     True      |  Yes   |  Yes   |  No    | "You are going to be late for work."           |
|             |               |        |        |        | "You are in a car yet?"                        |
|    True     |     False     |  No    |  Yes   |  No    | "You are in a car yet?"                        |
|    False    |     True      |  No    |  Yes   |  Yes   | "You are in a car yet?"                        |
|             |               |        |        |        | "You are not commuting."                       |
|    False    |     False     |  No    |  No    |  Yes   | "You are not commuting."                       |

Notes:
- The first if statement only executes if both variables are True.
- The second if statement executes if either variable is True.
- The third if statement executes if isCommuting is False.
"""