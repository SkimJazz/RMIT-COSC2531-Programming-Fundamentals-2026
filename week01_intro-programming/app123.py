# Week 01 Intro Programming
# 1.2.3 Examples of using Python


##### Case Sensitivity #####

# Print("3 Fuck my life")
"""Error: Case-sensitive function name

The line:
    Print("3 ...")

is incorrect because Python is a case-sensitive language. The built-in function for displaying
output is 'print', all lowercase. Using 'Print' with an uppercase 'P' will result in a NameError,
as Python does not recognize 'Print' as a valid function name. Always use 'print' (lowercase) 
to output text to the console.

Correct usage:
    print("3 ...")
"""


##### Quotations needed for string values #####

# print(4 Fuck my life)
"""Error: All string values must be enclosed in quotes

The line:
    print(4 Fuck my life)

is invalid because Python requires all string values to be enclosed in quotes (either single or double).
Additionally, if you want to print multiple values, they must be separated by commas. In this example,
'4 Fuck my life' is not a valid Python expression, as the text is not quoted and there are no commas 
separating values.

Correct usage:
    print("4 Fuck my life")
or
    print(4, "Fuck my life")
"""


##### Parentheses required for function calls #####

# print"5 fuck my life"
"""Error: Print function requires parentheses around its arguments

The line:
    print"5 fuck my life"

is invalid in Python 3 because 'print' is a function and requires parentheses around its arguments.
Omitting the parentheses will result in a SyntaxError. In Python 2, 'print' could be used as a 
statement without parentheses, but this is not allowed in Python 3 and later.

Correct usage:
    print("5 fuck my life")
"""