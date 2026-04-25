# Week 2 - 2.3.4 Putting it together

# Task - Create a program

# Your program should:

# 1. Take at least one input from the user that is then displayed back to them
#   - The input should be of type int, float or str but NO `input()` function can be used.
#   - The input should be taken using `sys.stdin.readline()` function and the output should
#     be displayed using `sys.stdout.write()` function.
# 2. Feature a list of int data type
# 3. Use at least one if statement
# 4. Contain at least one comparison operator
# 5. Include at least three comments
# 6. Include at least one instance of the use of \n to start a new line.

# Skimboarding program that check if the Wave high dumping in the beach is sutable for skimboarding

# Display "welcome message to the user"
# import sys
# sys.stdout.write("Welcome to the Skimboarding Wave Checker!\n")


# import sys
# sys.stdout.write("What course are you studying? ")
# sys.stdout.flush()  # Flush the output buffer to ensure the prompt is displayed before waiting for input

# # User input - using the `sys.stdin.readline()` function to take input from the user and store it in a variable called `courseID`
# courseID = sys.stdin.readline().strip()  # Use .strip() to remove any leading/trailing whitespace characters, including the newline character

# sys.stdout.write("OK. It looks like you are taking the practice test for " + str(courseID) + "\n")
# sys.stdout.flush()  # Flush the output buffer to ensure the message is displayed before the program ends
# sys.stdout.write("Please make a small change to this program, save the file, then upload it in the test.\n")
# sys.stdout.flush()  # Flush the output buffer to ensure the message is displayed before the program ends

# user_id = int(input("Enter ID: "))

# import sys

# # Ask user for there ID => `.flush()` needed to output the prompt before waiting for input
# sys.stdout.write("Enter ID: ")
# sys.stdout.flush()

# # Save ID to variable `roleID` and convert it to an integer using the `int()` function
# roleID = int(sys.stdin.readline())

# # Output roleID back to user and ask for their role
# sys.stdout.write("Enter ID " + str(roleID) + "'s role: ")
# sys.stdout.flush()
# # Save role to variable `role` and .strip() leading /trailing whitespace from the input
# role = sys.stdin.readline().strip()

# # Output greating message to user using the role and roleID variables
# sys.stdout.write("Hello " + role + " 00" + str(roleID) + "\n")
# sys.stdout.flush()

# Task 2 - Wright a program that does the following:
# - Asks the user for their name
# - Ask the user for their year of birth
# - Outputs a message in the following format:
#   "Hello [name], you were born in [year of birth] and you are [age] years old."

# import sys

# # Ask user for their name
# sys.stdout.write("Enter your name: ")
# sys.stdout.flush()

# # Save name to variable `name` and .strip() leading /trailing whitespace from the input
# name = sys.stdin.readline().strip()

# # Ask user for their year of birth
# sys.stdout.write("Enter your year of birth: ")
# sys.stdout.flush()
# # Save year of birth to variable `year_of_birth` and convert it to an integer using the `int()` function
# year_of_birth = int(sys.stdin.readline())

# # Output message in the specified format
# sys.stdout.write("Hello " + name + ", you were born in " + str(year_of_birth) + " and you are " + str(2026 - year_of_birth) + " years old.\n")
# sys.stdout.flush()

