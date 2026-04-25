# Week 2 - Using Strings (str) and Comments

# Topics:
# - Using variables to store results
# - Using compound assignment operators
# - Using comments to explain code
import sys



# Variable `string (str)`
#   The `str` data type is used to represent text. It is a sequence of characters enclosed in 
#   quotes (single, double, or triple). Strings can contain letters, numbers, symbols, and 
#   whitespace.
#string variable (str)


# EG.1 - Using variables to Store Results
roleID = 7 # `int` variable to store the role ID
role = "agent" # `str` variable to store the role name
sys.stdout.write("Hello "+role+" 00"+str(roleID))
sys.stdout.flush()
# Output: Hello agent 007 => string

# EG.2 - Using variables to Store Results
# Using the `\` escape character to include a newline in the string
# The name's Bond, James Bond.
sys.stdout.write("The name\'s Bond, James Bond.\n")
sys.stdout.flush()
# Output: The name's Bond, James Bond. => string

# Whats happening here with the `\` escape character?
#   The `\` character is an escape character in Python, which allows you to include special
#   characters in a string that would otherwise be difficult to include. In this case, 
#   the `\'` sequence allows you to include a single quote character within the string without
#   ending the string. The `\n` sequence is used to include a newline character, which causes
#   the text to be printed on a new line when output.
#escape (\) chr 




