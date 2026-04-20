# Week 1: Introducing programming
# 1.2.5 Working with error messages

# Understanding problems in our programming

# What is a EOL Error?
# Most programming errors fall in to one of three main categories:
# 1. Syntax errors
# 2. Run-time errors
# 3. Logic errors


## ------------------- What is a EOL Error? ------------------- ##
"""
An EOL error in Python stands for "End Of Line" error. This error usually occurs when Python reaches
the end of a line (or the end of your code) but is still expecting more input to complete a statement. 
The most common cause is a missing closing quotation mark or parenthesis in your code.

print("Hello world)

Python will raise a `SyntaxError: EOL while scanning string literal` because it expected another quotation
mark before the end of the line.

EOL - Python was expecting something (like a quote, parenthesis, or bracket) before the line ended,
therefore checking your code for missing or unmatched symbols.
"""


## ------------------ Syntax errors ------------------ ##

""" 1. Syntax errors
Syntax errors are errors that produce an error message as a result of incorrectly written
instructions. They are detected by the language editor, interpreter or compiler when executed.

- Missing or mismatched parentheses, brackets, or braces
- Missing or mismatched quotation marks
- Incorrect indentation
- Using reserved keywords as variable names
- Using the wrong syntax for a particular programming construct (e.g., using an assignment operator
  instead of a comparison operator)
"""

# 1. Missing or mismatched parentheses
# print("Hello world"    # Missing closing parenthesis


# 2. Missing or mismatched quotation marks
# print("Hello world)    # Missing closing quotation mark


# 3. Incorrect indentation
# if True:
# print("Hello")         # Should be indented under the if statement


# 4. Using reserved keywords as variable names
# for = 5                # 'for' is a reserved keyword in Python


# 5. Missing colon after statements like if , for, while, def, class
# if True                # Missing colon
#     print("Hello")


# 6. Assignment instead of comparison in conditions
# if x = 5:              # Should use '==' for comparison, not '='
#     print("x is 5")


# 7. Extra or missing commas in lists, tuples, or function arguments
# numbers = [1, 2, 3 4, 5]   # Missing comma between 3 and 4


# 8. Using undefined variables
# print(name)            # 'name' is not defined


# 9. Unclosed brackets, braces, or parentheses
# my_list = [1, 2, 3     # Missing closing bracket


# 10. Incorrect function definition syntax
# def my_function     # Missing parentheses `()` and colon `:`
#     print("Hello")


# 11. Using print as a statement(Python 3)
# print "Hello"          # Missing parentheses in Python 3


## ------------------ Run-time errors ------------------ ##

"""2. Run-time errors
Run-time errors are mistakes that only show up when your program is running. They usually stop your
program and display an error message. These errors are not caught by Python before running your code,
so you need to test your programs to find and fix them. But they can be caused by things like:

- Division by zero
- Accessing an index that is out of range
- Using a variable that has not been defined
- Running out of memory
- Infinite loops -> These are fucked!

"""

# 1. Division by zero
# print(10 / 0)        # This will raise a ZeroDivisionError


# 2. Accessing an index that is out of range
# numbers = [1, 2, 3]
# print(numbers[5])    # This will raise an IndexError


# 3. Using a variable that has not been defined
# print(age)    # Causes NameError if 'age' was never assigned a value


# 4. Invalid type operations
# print("5" + 2)    # Causes TypeError (cannot add string and integer)


# 5. File not found
# open("nonexistent_file.txt")    # Causes FileNotFoundError


# 6. Infinite loop(program never stops)
# while True:
#     print("This will run forever!")     # Program keeps running until stopped manually


# 7. Value error(wrong type of value)
# num = int("hello")    # Causes ValueError (cannot convert 'hello' to integer)


# 8. Key not found in a dictionary
# my_dict = {"a": 1}
# print(my_dict["b"])  # Causes KeyError ('b' does not exist)


## ------------------ Logic errors ------------------ ##

"""3. Logic errors
Logic errors do not stop your program or show an error message, but they make your program produce 
the wrong result. They are often the hardest to find, so always check your logic and test your code 
carefully! But they can be caused by shit like the following:

- Using the wrong operator
- Using the wrong variable
- Using the wrong data type
- Using the wrong algorithm
- Using the wrong order of operations

"""

# 1. Using the wrong operator
# Intended to add, but accidentally subtracts
# result = 5 - 2  # Should be 5 + 2
# print(result)   # Output: 3 (but you wanted 7)


# 2. Using the wrong variable
# a = 10
# b = 20
# print(a + c)    # 'c' is not defined, or maybe you meant 'b'


# 3. Using the wrong data type
# age = "20"
# print(age + 1)  # This will cause a TypeError, but even if you wrote print(age + "1"), you'd get "201" instead of 21


# 4. Using the wrong algorithm
# Intended to calculate the average, but divides by the wrong number
# numbers = [2, 4, 6]
# average = sum(numbers) / 2  # Should divide by len(numbers), which is 3
# print(average)  # Output: 6.0 (but correct average is 4.0)


# 5. Using the wrong order of operations
# # Intended to multiply first, but adds first due to missing parentheses
# result = 2 + 3 * 4  # Output: 14 (because 3*4=12, then 2+12=14)
# # If you wanted (2+3)*4, you should use parentheses
# correct_result = (2 + 3) * 4  # Output: 20


# 6. Incorrect logic in conditions
# score = 85
# if score < 50:
#     print("Pass")  # This will not print "Pass" for 85, but maybe you meant '>'


# 7. Off-by-one errors(common in loops)
# for i in range(1, 5):  # This will loop for 1, 2, 3, 4 (not including 5)
#     print(i)
# # If you wanted to include 5, use range(1, 6)
