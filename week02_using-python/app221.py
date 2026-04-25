# Week02 - 2.2.1 Woring with Numbers

# Use Python as a Calculator
import sys


# # Eg.1 - Arithmetic Operators
# sys.stdout.write(str(2 + 2) + "\n")
# sys.stdout.flush()      # display output in termnial
# # Output: 4 => int

# # Eg.2 - Operator Precedence
# sys.stdout.write(str(50 - 5 * 6) + "\n")
# sys.stdout.flush()
# # Output: 20 => operator precedence, multiplication before subtraction => int

# # Eg.3 - Using Parentheses to Change Precedence
# sys.stdout.write(str((50 - 5 * 6) / 4) + "\n")
# sys.stdout.flush()
# # Output: 5.0 => float

# # Eg.4 - Division and Floor Division
# sys.stdout.write(str(8 / 5) + "\n")  # division always returns a floating point number
# sys.stdout.flush()
# # Output: 1.6 => float

# # Eg.5 - Floor Division and Modulo
# sys.stdout.write(str(17 / 3) + "\n")  # classic division returns a float
# sys.stdout.flush()
# # Output: 5.666666666666667 => float

# # Eg.6 - Floor Division and Modulo
# sys.stdout.write(str(17 // 3) + "\n")  # floor division discards the fractional part
# sys.stdout.flush()
# # Output: 5 => int

# # Eg.7 - Modulo Operator
# sys.stdout.write(str(17 % 3) + "\n")  # the % operator returns the remainder of the division
# sys.stdout.flush()
# # Output: 2 => int

# # Eg.8 - Combining Operators
# sys.stdout.write(str(5 * 3 + 2) + "\n")  # flooded quotient * divisor + remainder
# sys.stdout.flush()
# # Output: 17 => int

# # Eg.9 - Exponentiation
# sys.stdout.write(str(5 ** 2) + "\n")  # 5 squared
# sys.stdout.flush()
# # Output: 25 => int

# # Eg.10 - Floating Point Precision
# sys.stdout.write(str(1 / 3) + "\n")
# sys.stdout.flush()
# # Output: 0.3333333333333333 => float

# # Eg.11 - Floating Point Precision
# sys.stdout.write(str(3 * (1 / 3)) + "\n")
# sys.stdout.flush()
# # Output: 1.0 => float, not exactly 1 due to floating point precision issue in Python
"""Whats happeing here?
#
# 1. 1/3 is calculated first, which results in a floating point approximation of 0.3333333333333333.
# 2. Then, this approximation is multiplied by 3, which should ideally give us 1. However, due to the
#    nature of floating point arithmetic and how numbers are represented in binary (which can lead to
#    precision issues), the result is 1.0 instead of exactly 1. This is a common issue in programming
#    languages that use floating point arithmetic, and it highlights the importance of understanding 
#    how numbers are represented and calculated in computers.
"""

# # Eg.12 - Using variables to Store Results
# width = 20
# height = 5
# area = width * height
# sys.stdout.write(str(area) + "\n")
# sys.stdout.flush()
# # Output: 100 => int

# # Eg.13 FiNd Volume of rectangle
# width = 20
# height = 5
# length = 9
# volume = width * height * length
# sys.stdout.write(str(volume) + "\n")
# sys.stdout.flush()
# # Output: 900 => int

# # Eg.14 - Using variables to Store Results WHAT NOT TO DO!
# tax = 12.5 / 100
# price = 100.50
# price * tax
# sys.stdout.write(str(price * tax) + "\n")
# sys.stdout.flush()
# # Output: 12.5625 => float

# price + _   # `_` is undefined => Need interactive Python interpreter (REPL) to use.
# sys.stdout.write(str(price + _) + "\n")
# sys.stdout.flush()
# # Output: 113.0625 => float

# round(_, 2)
# sys.stdout.write(str(round(_, 2)) + "\n")
# sys.stdout.flush()
# # Output: 113.06 => float


# # Eg.14a - BETTER WAY to calculate total price with tax
# price = 100.50
# tax = 12.5 / 100
# tax_amount = price * tax
# sys.stdout.write(str(tax_amount) + "\n")
# sys.stdout.flush()

# total = price + tax_amount
# sys.stdout.write(str(total) + "\n")
# sys.stdout.flush()

# sys.stdout.write(str(round(total, 2)) + "\n")
# sys.stdout.flush()

cal = 567 + 789
print(cal)

num1 = 567
num2 = 789
ans = num1 + num2
print(ans)

a = 567 + 789
b = 989 - 123
c = a + b
print(c)

# sys.stdout.write("10" + "5" + "\n")
# sys.stdout.flush()
# # Output: 105 => string concatenation, not addition

# sys.stdout.write("10" + 5 + "\n")
# sys.stdout.flush()
# # Output: TypeError => cannot concatenate str and int

# sys.stdout.write(str(int("10") + 5) + "\n")
# sys.stdout.flush()
# # Output: 15 => int addition after converting string to int
